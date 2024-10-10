# app.py
from models import EmailViewModel
from renderer import Renderer
from services import EmailReportGenerator

def main():
    # Set up the view model
    model = EmailViewModel(
        user_name="Test User",
        sender_name="Contoso",
        user_data1=1,
        user_data2=2
    )
    
    # Instantiate services and renderer
    report_generator = EmailReportGenerator()
    renderer = Renderer()

    # Generate the report using the service
    report = report_generator.generate_report(model.user_data1, model.user_data2)

    # Create context to be passed to the template
    context = {
        'user_name': model.user_name,
        'sender_name': model.sender_name,
        'report': report
    }

    # Render the main email template to a string
    email_content = renderer.render_template_to_string('email_template.html', context)
    
    # Print the rendered content to console (mimicking the C# example)
    print(email_content)

if __name__ == "__main__":
    main()
