from django import template

register = template.Library()

@register.filter
def count_likes(likes, post_id):
    return sum(1 for like in likes if like.post_id == post_id)
