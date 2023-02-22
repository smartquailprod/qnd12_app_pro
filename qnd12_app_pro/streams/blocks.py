
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Agregar un titulo")
    text = blocks.TextBlock(required=True, help_text="Agregar un texto adicional")


class Meta:
    template = "streams/title_and_text_block.html"
    icon = "edit"
    label = "title & Text"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Escribir el titulo")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="Si el boto es seleccionado arriba de la pagina")),
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"


class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "full_richtext"

class SimpleRichtextBlock(blocks.RichTextBlock):
    
    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "simple_richtext"

