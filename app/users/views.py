from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseNotAllowed, HttpResponse


# Create your views here.
def home_page(requests):
    return HttpResponse('<h1>Home</h1>')


def get_all_users(requests):
    if requests.method != 'GET':
        raise HttpResponseNotAllowed("Method is not allowed")

    query_set = User.objects.all()
    serializable = serializers.serialize('json', query_set)

    return HttpResponse(serializable)
