from django import template
from django.template.loader import get_template

register = template.Library()
 
@register.tag
def slider(parser, token):
    nodelist = parser.parse(('endslider',))
    parser.delete_first_token()
    return SliderNode(nodelist)
 
class SliderNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output

@register.tag
def header(parser, token):
    try:
        tag_name, modal_id, title = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("%r takes two arguments: the modal id and title" % token.contents.split()[0])
 
    nodelist = parser.parse(('endheader',))
    parser.delete_first_token()
    return headerNode(modal_id, title, nodelist)
 
@register.tag
def header(parser, token):
    nodelist = parser.parse(('endheader',))
    parser.delete_first_token()
    return HeaderNode(nodelist)


class HeaderNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context(**kwargs))
        t = template.loader.get_template('webapp_0/header.html')
        c = template.Context({'body': output})
        return t.render(c)

@register.tag
def portfolio(parser, token):
    nodelist = parser.parse(('endportfolio',))
    parser.delete_first_token()
    return portfolioNode(nodelist)
 
class portfolioNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output

@register.tag
def tearsheeting(parser, token):
    nodelist = parser.parse(('endtearsheeting',))
    parser.delete_first_token()
    return tearsheetingNode(nodelist)
 
class tearsheetingNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output

@register.tag
def noticias(parser, token):
    nodelist = parser.parse(('endnoticias',))
    parser.delete_first_token()
    return noticiasNode(nodelist)
 
class noticiasNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output

@register.tag
def contact(parser, token):
    nodelist = parser.parse(('endcontact',))
    parser.delete_first_token()
    return contactNode(nodelist)
 
class contactNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output

@register.tag
def footer(parser, token):
    nodelist = parser.parse(('endfooter',))
    parser.delete_first_token()
    return footerNode(nodelist)
 
class footerNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
 
    def render(self, context):
        output = self.nodelist.render(context)
        return output