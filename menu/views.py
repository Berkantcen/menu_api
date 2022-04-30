from django.http import JsonResponse
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(["GET", "POST"])
def menu_list(request):
    if request.method == "GET":
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return JsonResponse({"menu":serializer.data})
    if request.method == "POST":
        serializer =MenuSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def menu_item(request,id):
    try:
       menu_item = Menu.objects.get(pk=id)
    except Menu.DoesNotExist:
        return  JsonResponse( {"error": "Not Found"},status=status.HTTP_404_NOT_FOUND)


    if request.method == "GET":
        serializer = MenuSerializer(menu_item)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        serializer = MenuSerializer(menu_item, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        menu_item.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)
