"""
This is a simple chatbot which use chatlit as UI and langgraph as backend.
This chatbot has streaming capabilities.
"""

from dotenv import load_dotenv

load_dotenv()
import uuid
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
import chainlit as cl


def generate_chat_session_id():
    return str(uuid.uuid4())


graph = StateGraph(state_schema=MessagesState)
llm = ChatOpenAI(model="gpt-4o-mini", streaming=True)


# Define the function that calls the llm
def call_llm(state: MessagesState):
    system_prompt = (
        "You are a helpful assistant. "
        "Answer all questions to the best of your ability."
    )
    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": response}


# Define the node and edge
graph.add_node("llm", call_llm)
graph.add_edge(START, "llm")

# Add simple in-memory checkpointer
memory = MemorySaver()
graph_compiled = graph.compile(checkpointer=memory)


@cl.on_chat_start
async def on_chat_start():
    thread_id = generate_chat_session_id()
    cl.user_session.set("thread_id", thread_id)


# # No streaming version
# @cl.on_message
# async def on_message(message: cl.Message):
#     thread_id = cl.user_session.get("thread_id")
#     result = graph_compiled.invoke(
#         {"messages": [HumanMessage(content=message.content)]},
#         config={"configurable": {"thread_id": thread_id}},
#     )
#     await cl.Message(content=result["messages"][-1].content).send()


# Streaming version
@cl.on_message
async def on_message(message: cl.Message):
    thread_id = cl.user_session.get("thread_id")
    msg = cl.Message(content="")
    async for event in graph_compiled.astream_events(
        {"messages": [HumanMessage(content=message.content)]},
        config={"configurable": {"thread_id": thread_id}},
        version="v1",
    ):
        if event["event"] == "on_chat_model_stream":
            await msg.stream_token(event["data"]["chunk"].content)

    await msg.send()
