from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resource
		fields = ('id',)


class ResourceViewSet(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		serializer = ResourceSerializer(Resource.objects.filter(profile=request.user), many=True)
		return Response(serializer.data)

	def put(self, request):
		try:
			resource = Resource.objects.create(profile=request.user)
		except Exception as e:
			return Response(str(e))
		return Response(ResourceSerializer(resource).data)

	def delete(self, request):
		try:
			Resource.objects.get(id=request.data.get('id')).delete()
		except Exception as e:
			return Response(str(e))
		return Response({'id':request.data.get('id')})