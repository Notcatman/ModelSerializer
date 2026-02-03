from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import ReviewSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save()
            return Response({'id': review.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def review_view(request, pk):
    yes = get_object_or_404(Review, pk=pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(yes)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        yes.delete()
        return Response(
            {"message": "Review deleted successfully."},
            status=status.HTTP_200_OK
        )
    
