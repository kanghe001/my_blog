from django.shortcuts import render
from django.conf import settings
import logging
from my_blog.models import *
from django.core.paginator import PageNotAnInteger, EmptyPage, InvalidPage, Paginator

# Create your views here.

logger = logging.getLogger('test2')


def global_data(request):
    archive_list = Artical.objects.distinct_date()
    return {
        'archive_list': archive_list,
        'WEB_TITLE': settings.WEB_TITLE,
        'WEB_SITE': settings.WEB_SITE,
    }


def get_page(request, object_list):
    paginator = Paginator(object_list, 1)
    try:
        page = int(request.GET.get('page', 1))
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        object_list = paginator.page(1)
    return object_list


def index(request):
    try:
        artical_list = get_page(request, Artical.objects.all())
    except Exception as e:
        logger.warn(e)
    return render(request, 'base.html', locals())


def archive(request):
    try:
        year = request.GET.get('year', None)
        mouth = request.GET.get('mouth', None)
        artical_list = Artical.objects.filter(date_publish__icontains=year+"-"+mouth)
        artical_list = get_page(request, artical_list)

    except Exception as e:
        logger.warn(e)

    return render(request, 'archive.html', locals())