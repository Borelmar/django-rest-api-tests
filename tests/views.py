from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
from .models import *
from .permissions import *

class CreateTest_APIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    serializer_class = CreateTestSerializer
    queryset = Test.objects.all()

class GetTestInfo_APIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class GetTestDetail_APIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin, IsTestOwner]
    serializer_class = GetTestDetailSerializer
    queryset = Test.objects.all()

class DeleteTest_APIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin, IsTestOwner]
    serializer_class = TestSerializer
    queryset = Test.objects.all()

class UserResultCreateView(APIView):
    def post(self, request, pk,format=None):
        #test_id = self.kwargs.get("pk")
        test = Test.objects.get(id=pk)
        if not test:
            return Response({'status': 'invalid'}, code=400)
        serializer = UserResultSerializer(data=request.data, context={'request': request, 'test': test})
        if serializer.is_valid():
            user_result = serializer.save()
            return Response({'status': 'success',
                'user_result_id': user_result.id,
                'correct_count': user_result.correct_count,
                'incorrect_count': user_result.incorrect_count})
        return Response(serializer.errors, status=400)

class UserResultInfoView(generics.RetrieveAPIView):
    queryset = UserTest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserResultInfoViewSerializer

class GetUserResultsView(generics.ListAPIView):
    #queryset = UserTest.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserResultInfoViewSerializer
    def get_queryset(self):
        user_id = self.kwargs.get("pk", None)
        if not user_id:
            raise ValidationError(detail='Invalid Params')
        user = User.objects.get(id=user_id)
        if not user:
            raise ValidationError(detail='Invalid user id')
        return UserTest.objects.filter(user=user)


class GetTestDetailForUser_APIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin, IsTestOwner]
    serializer_class = GetTestDetailForUserSerializer
    queryset = Test.objects.all()

class GetTestStatisticAPIView(APIView):
    def get(self, request, test_id):
        user_results = UserTest.objects.filter(test_id=test_id)
        serializer = GetTestStatisticSerializer(user_results, many=True)
        return Response(serializer.data)
