import asyncio
from langgraph_sdk import get_client


LANGGRAPH_URL = "http://localhost:2024" 
ASSISTANT_ID = "brain"  

class RemoteLangGraphAssistant:
    def __init__(self):
        self.client = None
        self.thread_id = None

    async def _get_client(self):
        if self.client is None:
            self.client = get_client(url=LANGGRAPH_URL)
        return self.client

    async def run_query(self, text):
        client = await self._get_client()
        if self.thread_id is None:
            thread = await client.threads.create()
            self.thread_id = thread["thread_id"]
           
        print("Thread id", self.thread_id)
        input_data = {"messages": [{"role": "user", "content": text}]}
        
        response = await client.runs.wait(
            self.thread_id,
            ASSISTANT_ID,
            input=input_data,
        )

        print("Response", response)
        
        final_message = response.get("messages", [])[-1].get("content", "") if response.get("messages") else ""
        
        print("Final message", final_message)
        return final_message

lg_assistant = RemoteLangGraphAssistant()