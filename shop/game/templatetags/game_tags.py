from django import template

register = template.Library()


@register.filter(name='game_shorten_text')
def game_shorten_text(bodytext, length):
    if len(bodytext) > length:
        text = '%s ...' % bodytext[1:length]
    else:
        text = bodytext
    return text

