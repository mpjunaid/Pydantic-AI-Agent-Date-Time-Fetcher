# Pydantic AI Agent: Date & Time Fetcher

This repository provides an example of a **Pydantic AI agent** that uses tools to retrieve and format real-time date and time information. It demonstrates how to overcome a common limitation of locally run Large Language Models (LLMs)—their inability to access current, dynamic data—by integrating them with external tools.



##  How It Works

This project showcases two distinct implementations:

- **Local LLM with Ollama**:  
  A Pydantic AI agent that uses the `llama3.1:latest` model, powered by Ollama.  
  It executes a Python tool (`get_current_date`) to fetch the current date.

- **Google Gemini Model**:  
  A similar agent using the `gemini-2.0-flash` model.  
  It leverages a different tool (`get_current_datetime`) to get both the date and time.

The core principle is **tool-based execution**. Instead of trying to generate the information from its static training data, the LLM determines that it needs the current date and/or time and then calls a designated tool. This tool, a standard Python function, executes the request and returns the data, which the agent then presents in a structured format.



### Comparing the Outputs

The difference between the two implementations highlights the advantage of the Gemini model in this specific use case.

### Gemini
The **Gemini** model is able to access and return a more detailed output, including the date, hour, minutes, and seconds.

**Output:**
```
The current date and time is: 2025-08-30 09:28:38
{'day': 30, 'month': 'August', 'year': 2025, 'hour': 9, 'minutes': 28, 'seconds': 38}
AgentRunResult(output={'day': 30, 'month': 'August', 'year': 2025, 'hour': 9, 'minutes': 28, 'seconds': 38})
```

### Local Llama3.1
The **Llama3.1** model, while successful in using the tool to get the date, does not access the time details.

**Output:**
```
Today's date is: 2025-08-30
{'day': 30, 'month': 'August', 'year': 2025}
AgentRunResult(output={'day': 30, 'month': 'August', 'year': 2025})
```


### Features & Advantages
**Tool-Based Execution**: The agent uses a tool to perform a specific, real-time task, demonstrating how to ground an LLM's response in up-to-date, external data.

**Structured Output**: The output is strictly formatted according to a Pydantic TypedDict, ensuring reliable and predictable data for downstream applications.

**Overcoming LLM Limitations**: This approach solves a common problem with locally hosted LLMs, which are trained on static data and cannot access dynamic information like the current time.