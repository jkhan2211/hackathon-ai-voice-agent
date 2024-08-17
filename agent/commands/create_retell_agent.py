from django.core.management.base import BaseCommand
from retell import Retell

class Command(BaseCommand):
    help = 'Create a Retell AI voice agent'

    def handle(self, *args, **kwargs):
        retell_client = Retell(api_key="")
        agent_response = retell_client.agent.create(
            llm_websocket_url="wss://api.retellai.com/retell-llm-new/llm_0fe2daf1c64b952dd5be9c40a6a3",
            voice_id="11labs-Adrian",
        )
        agent_id = agent_response.agent_id
        print(f"Agent created with ID: {agent_id}")

        # Optional: Store the agent_id in a file for future use
        with open('agent_id.txt', 'w') as f:
            f.write(agent_id)
