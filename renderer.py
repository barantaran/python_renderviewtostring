# renderer.py
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Renderer:
    def __init__(self, template_dir='templates'):
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def render_template_to_string(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)
