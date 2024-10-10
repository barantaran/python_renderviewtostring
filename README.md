
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
