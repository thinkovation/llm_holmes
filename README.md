# Learning how to work with LLMs
This repo is a play repository to explore how to work with LLMs

## Setup

### Environment
You don't have to create a specific environment, but when it comes to managing packages etc etc I find it easier to maintain separate python environments for each project.

By default I name the environment "myenv" and create it using the venv feature, thusly:
```
python -m venv myenv  
```

When I want to work with the code I initialise the environment by calling:
```
myenv/Scripts/activate
```

### Packages to install
Make sure the following packages are pip-installed:
- numexpr
- python-dotenv (This is so we can maintain a local private environment file to contain things like API keys)
- llama-index (This is crammed with llm goodness - Don't worry if it takes a while to install, it's mahoosive)
- openai (This may have already been schnuffled by llama-index so you may just get loads of "requirements already satisfied" messages. Noice.)