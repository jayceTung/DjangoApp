# -*- coding: utf-8 -*-

# @Author  : super
# @Time    : 2018/1/24
# @desc    :
from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()


# 这是定义模板标签要用到的

@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    left = 3
    right = 3

    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')

    try:
        object_lis = paginator.page(page)
        context['current_page'] = int(page)
        pages = get_left(context['current_page'], left, paginator.num_pages) + get_right(context['current_page'], right,
                                                                                         paginator.num_pages)

    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
        pages = get_right(context['current_page'], right, paginator.num_pages)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages
        pages = get_left(context['current_page'], left, paginator.num_pages)

    context['article_list'] = object_list
    context['pages'] = pages
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1

    try:
        context['pages_first'] = page[0]
        context['page_last'] = page[-1] + 1

    except IndexError:
        context['page_first'] = 1
        context['page_last'] = 2

    return ''


def get_left(current_page, left, num_page):
    """
    get left Number
    :param current_page:
    :param left:
    :param num_page:
    :return:
    """
    if current_page == 1:
        return []
    elif current_page == num_page:
        l = [i - 1 for i in range(current_page, current_page - left, -1) if i - 1 > 1]
        l.sort()
        return l
    l = [i for i in range(current_page, current_page - left, -1) if i > 1]
    l.sort()
    return l


def get_right(current_page, right, num_pages):
    """
    get right Number
    :param current_page:
    :param right:
    :param num_pages:
    :return:
    """
    if current_page == num_pages:
        return []
    return [i + 1 for i in range(current_page, current_page + right - 1) if i < num_pages - 1]
