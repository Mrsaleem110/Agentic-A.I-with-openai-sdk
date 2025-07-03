import chainlit as cl

@cl.on_message
async def main(message:cl.message):
    await cl.message(
        content=f"Received:{message.content}",
    ).send()