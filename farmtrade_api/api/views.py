from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import UserProfile, Product
from api.serializers import UserProfileSerializer, ProductSerializer, ProductDetailSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            # Retain the existing photo if 'photo' field is not present in the request data
            if 'photo' not in request.data:
                serializer.validated_data['photo'] = instance.photo

            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

# @csrf_exempt
# def profile_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         profile = UserProfile.objects.all()
#         serializer = UserProfileSerializer(profile, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = UserProfileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# def profile_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         profile = UserProfile.objects.get(pk=pk)
#     except UserProfile.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = UserProfileSerializer(profile)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = UserProfileSerializer(profile, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         profile.delete()
#         return HttpResponse(status=204)




