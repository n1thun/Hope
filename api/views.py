# from api.models import Foreclosure
# from api.serializers import ForeclosureSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class ForeclosureList(APIView):
#     """
#     List all Foreclosures, or create a new Foreclosure.
#     """
#     def get(self, request, format=None):
#         snippets = Foreclosure.objects.all()
#         serializer = ForeclosureSerializer(Foreclosure, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ForeclosureSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from api.models import Foreclosure, Person
from api.serializers import ForeclosureSerializer, PersonSerializer
from documentcreation.document import make_tex


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def foreclosure_list(request):
    """
    List all code foreclosures, or create a new foreclosure.
    """
    if request.method == 'GET':
        snippets = Foreclosure.objects.all()
        serializer = ForeclosureSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ForeclosureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def person_list(request):
    """
    List all code foreclosures, or create a new foreclosure.
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ForeclosureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def create_letters(request):
    make_tex()
    return JSONResponse("Success", status=200)
