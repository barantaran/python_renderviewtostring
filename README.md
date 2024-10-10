
# Python Razor View to String Renderer

This is a Python port of a .NET Core application that renders HTML views to strings using templates, mimicking Razor view rendering in ASP.NET Core.

## Project Structure
```
python_renderviewtostring/
├── app.py               # Entry point for the Python application
├── models.py            # Data models for email content
├── renderer.py          # Rendering logic to convert templates to strings
├── services.py          # Email generation and other services
└── templates/           # Directory for Jinja2 HTML templates
    ├── base.html        # Base layout template
    ├── email_template.html # Main email template
    └── email_partial.html  # Partial view template
```

## Running the Application
1. Install [Python 3.11+](https://www.python.org/downloads/) if not already installed.
2. Install the necessary dependencies:
    ```bash
    pip install jinja2
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. The output will be printed to the console, displaying the rendered HTML content.

## Used prompts
I started a custom GPT session to avoid losing the connection to the virtual environment in a regular chat.
I provided ChatGPT with the following brief instructions:
```
You're acting as a middle developer. 
Unpack & examine project files (except csproj, unless otherwise stated), then follow chat instruction.
```

After that, I began **constructing the context** for the porting procedure using the following prompts directly in the chat.
First, examine the project structure and its purpose:
```
Examine project, explain its composition and purpose.
```

Then, analyze the project code in detail, not just by summarizing headings: 
```
Examine each file completely in detail.
```

Next, provide ChatGPT with the output of the application:
```
There is an output of console app after build & run procedure:

<!DOCTYPE html>...
```

Plan the porting procedure:
```
Lets find the way to port this app into Python console app, preserving its purpose,
functionality and structure as max as possible in Python environment.
```

Now we have the source code, project structure, purpose, runtime output, and a porting plan.
We can **proceed with the porting** process:
```
Provide me with archive of Python port and complete instrutction how to run it under windows.
Focus on maintaining the core functionality and logic flow while adapting to Python's syntax and conventions.
Do not include any references to APIs or external resources unless necessary for basic functionality.
```

In the end, we can **compare the resulting output** with the original one, **generate test cases** to compare flow logic, and create a README file to **describe ported project**:

```
Compare my output with original provided earlier:
<!DOCTYPE html>...
```
```
Propose a test case to compare original model logic and  transpiled one.
```
```
Provide me with very short README.md file download for resulted code
``` 
