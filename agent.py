import json
import requests
from cmd2 import Cmd
import argparse
import time
import itertools
import threading

API_URL = "http://127.0.0.1:7437/api/agent"

def thinking_animation():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if stop_thinking:  # stop_thinking is a global or class variable you need to set when the response arrives
            break
        print(c, end='\r')
        time.sleep(0.1)

class AgentCLI(Cmd):
    def __init__(self):
        super().__init__()
        self.intro = "Welcome to the Agent CLI! Type 'help' to list commands."
        self.prompt = 'agent-cli> '

    def do_list(self, _):
        """Lists all agents. Usage: list"""
        response = requests.get(API_URL)
        print(json.dumps(response.json(), indent=2))

    def do_add(self, agent_name):
        """Adds a new agent. Usage: add agent_name"""
        response = requests.post(API_URL, json={"name": agent_name})
        print(response.json())

    def do_config(self, agent_name):
        """Fetches the configuration of a specific agent. Usage: get config agent_name"""
        response = requests.get(f"{API_URL}/{agent_name}")
        print(json.dumps(response.json(), indent=2))

    def do_update_settings(self, args):
        """Updates the settings of a specific agent. Usage: update settings agent_name setting value"""
        agent_name, setting, value = args.split()
        response = requests.put(f"{API_URL}/{agent_name}", json={"settings": {setting: value}})
        print(response.json())

    def do_delete(self, agent_name):
        """Deletes a specific agent. Usage: delete agent_name"""
        confirm = input("Are you sure you want to delete this agent? (yes/no) ")
        if confirm.lower() == "yes":
            response = requests.delete(f"{API_URL}/{agent_name}")
            print(response.json())

    def do_rename(self, args):
        """Renames a specific agent. Usage: rename agent_name new_agent_name"""
        agent_name, new_agent_name = args.split()
        response = requests.patch(f"{API_URL}/{agent_name}", json={"new_name": new_agent_name})
        print(response.json())

    def do_chat_history(self, agent_name):
        """Fetches the chat history of a specific agent. Usage: get chat history agent_name"""
        response = requests.get(f"{API_URL}/{agent_name}/chat")
        print(json.dumps(response.json(), indent=2))

    def do_wipe_mem(self, agent_name):
        """Wipes the memory of a specific agent. Usage: wipe mem agent_name"""
        confirm = input("Are you sure you want to wipe this agent's memories? (yes/no) ")
        if confirm.lower() == "yes":
            response = requests.delete(f"{API_URL}/{agent_name}/memory")
            print(response.json())

    def do_instruct(self, args):
        """Instructs a specific agent. Usage: instruct agent_name prompt"""
        try:
            agent_name, prompt = args.split(maxsplit=1)
            response = requests.post(f"{API_URL}/{agent_name}/instruct", json={"prompt": prompt})
            print(response.json())
        except json.JSONDecodeError:
            print('Error: The server did not return a valid JSON response.')

    def do_chat(self, agent_name):
            """Chats with a specific agent. Usage: chat agent_name"""
            print(f"You are now chatting with {agent_name} agent.")
            while True:
                try:
                    prompt = input('>')
                    if prompt.lower() == 'bye':
                        print(f"Exiting chat with {agent_name}")
                        break
                    # Start thinking animation
                    global stop_thinking
                    stop_thinking = False
                    animation = threading.Thread(target=thinking_animation)
                    animation.start()
                    response = requests.post(f'{API_URL}/{agent_name}/chat', json={'prompt': prompt})
                    # Stop thinking animation
                    stop_thinking = True
                    response_json = response.json()
                    chat_message = response_json.get('response')
                    if chat_message:
                        print(f'{agent_name}: {chat_message}')
                except json.JSONDecodeError:
                    print('Error: The server did not return a valid JSON response.')


    
    def do_smart_chat(self, args):
        """Starts a smart chat with a specific agent. Usage: smart chat agent_name"""
        agent_name = args
        self.prompt = f'agent-cli>smart chat {agent_name}> '

    def do_get_commands(self, agent_name):
        """Fetches the commands of a specific agent. Usage: get commands agent_name"""
        response = requests.get(f"{API_URL}/{agent_name}/command")
        print(json.dumps(response.json(), indent=2))

    def do_toggle_command(self, args):
        """Toggles a command of a specific agent. Usage: toggle command agent_name command_name on|off"""
        agent_name, command_name, status = args.split()
        response = requests.patch(f"{API_URL}/{agent_name}/command", json={"command_name": command_name, "enable": status == 'on'})
        print(response.json())

    def do_get_task(self, agent_name):
        """Fetches the task output of a specific agent. Usage: get task agent_name"""
        response = requests.get(f"{API_URL}/{agent_name}/task")
        print(json.dumps(response.json(), indent=2))

    def do_start_task(self, args):
        """Starts a task for a specific agent. Usage: start task agent_name prompt"""
        agent_name, prompt = args.split(maxsplit=1)
        response = requests.post(f"{API_URL}/{agent_name}/task", json={"prompt": prompt})
        print(response.json())

    def do_task_status(self, agent_name):
        """Fetches the task status of a specific agent. Usage: task status agent_name"""
        response = requests.get(f"{API_URL}/{agent_name}/task/status")
        print(response.json())

if __name__ == "__main__":
    AgentCLI().cmdloop()
