# Agent-LLM-CLI

Agent-LLM-CLI is a CLI for interacting with https://github.com/Josh-XT/Agent-LLM.

It's built with Python and uses the `cmd2` library for building the CLI, and `requests` for making HTTP requests to the Agent-LLM API.

## Features

- Listing all agents
- Adding a new agent
- Fetching the configuration of a specific agent
- Updating the settings of a specific agent
- Deleting a specific agent
- Renaming a specific agent
- Fetching the chat history of a specific agent
- Wiping the memory of a specific agent
- Instructing a specific agent
- Chatting with a specific agent
- Starting a smart chat with a specific agent
- Fetching the commands of a specific agent
- Toggling a command of a specific agent
- Fetching the task output of a specific agent
- Starting a task for a specific agent
- Fetching the task status of a specific agent

## Setup


## Clone the repository using the following command:
```
git clone https://github.com/namastex888/Agent-LLM-CLI.git
```
```
cd Agent-LLM-CLI
```
```
pip install -r requirements.txt
```
## Finally, run Agent-LLM-CLI with the following command:
```
python agent.py
```

## Usage

The application starts in an interactive shell. You can type `help -v` to get a list of available commands. Each command has its own help message, which can be viewed by typing `help <command>`. Here are some examples of how you can use each command:

- **list**: Lists all agents. Usage: `list`
  ```
  agent-cli> list
  ```
  
- **add**: Adds a new agent. Usage: `add agent_name`
  ```
  agent-cli> add namastex
  ```
  
- **config**: Fetches the configuration of a specific agent. Usage: `config agent_name`
  ```
  agent-cli> config namastex
  ```
  
- **update_settings**: Updates the settings of a specific agent. Usage: `update_settings agent_name setting value`
  ```
  agent-cli> update_settings namastex max_response_time 1000
  ```
  
- **delete**: Deletes a specific agent. Usage: `delete agent_name`
  ```
  agent-cli> delete namastex
  ```
  
- **rename**: Renames a specific agent. Usage: `rename agent_name new_agent_name`
  ```
  agent-cli> rename namastex namastex2
  ```
  
- **chat_history**: Fetches the chat history of a specific agent. Usage: `chat_history agent_name`
  ```
  agent-cli> chat_history namastex
  ```
  
- **wipe_mem**: Wipes the memory of a specific agent. Usage: `wipe_mem agent_name`
  ```
  agent-cli> wipe_mem namastex
  ```
  
- **instruct**: Instructs a specific agent. Usage: `instruct agent_name prompt`
  ```
  agent-cli> instruct namastex "tell me a joke"
  ```
  
- **chat**: Chats with a specific agent. Usage: `chat agent_name`
  ```
  agent-cli> chat namastex
  ```
  
- **smart_chat**: Starts a smart chat with a specific agent. Usage: `smart_chat agent_name`
  ```
  agent-cli> smart_chat namastex
  ```
  
- **get_commands**: Fetches the commands of a specific agent. Usage: `get_commands agent_name

  ```
  agent-cli> get_commands namastex
  ```
  
- **toggle_command**: Toggles a command of a specific agent. Usage: `toggle_command agent_name command_name on|off`
  ```
  agent-cli> toggle_command namastex task on
  ```
  
- **get_task**: Fetches the task output of a specific agent. Usage: `get_task agent_name`
  ```
  agent-cli> get_task namastex
  ```
  
- **start_task**: Starts a task for a specific agent. Usage: `start_task agent_name prompt`
  ```
  agent-cli> start_task namastex "write a report on climate change"
  ```
  
- **task_status**: Fetches the task status of a specific agent. Usage: `task_status agent_name`
  ```
  agent-cli> task_status namastex
  ```

## Contributing

Contributions are welcome! Open issues and/or send pull requests :)

## License

This project is licensed under the terms of the MIT license.

## Thanks

@Josh for the amazing job with https://github.com/Josh-XT/Agent-LLM 
