from django import template
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, name):
    request = context['request']
    menu = MenuItem.objects.filter(name=name).first()
    return render_menu(menu, request.path)

def render_menu(menu, current_path):
    if not menu:
        return ''

    menu_html = ''

    for item in menu.children.all():
        menu_html += render_menu_item(item, current_path)

    return f'<ul>{menu_html}</ul>'

def render_menu_item(item, current_path):
    active_class = 'active' if item.url and item.url == current_path else ''
    named_url = item.named_url if item.named_url else ''
    children = render_menu(item, current_path)

    return f'<li class="{active_class}"><a href="{named_url}">{item.name}</a>{children}</li>'