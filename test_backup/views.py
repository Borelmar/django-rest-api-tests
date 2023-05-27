from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from django.db import transaction
from django.views import View

from .serializers import *
from .models import *
from .permissions import *


# *** TEST ***
# /tests/create
class CreateTest_APIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    serializer_class = CreateTestSerializer
    queryset = Test.objects.all()

# /tests/<test_id>/delete
class DeleteTest_APIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    queryset = Test.objects.all()


# /tests/<int:pk>/update
class UpdateTest_APIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    serializer_class = TestSerializer
    queryset = Test.objects.all()

# /tests/<int:pk>/info
class GetTestInfo_APIView(generics.RetrieveAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()


# *** TASK ***
# /tests/<int:pk>/get_tasks
class GetTestTasks_APIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    serializer_class = TaskSerializer
    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        if not pk:
            raise ParseError(code=400)
        return Task.objects.filter(test=pk)


class CreateTask_APIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    serializer_class = CreateTaskSerializer
    queryset = Task.objects.all()

class DeleteTask_APIView(View):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]

    def delete(self):
        test_id = self.kwargs.get("pk", None)
        task_id = self.kwargs.get("task_id", None)
        if not test_id or not task_id:
            raise ParseError(code=400)

        test = Test.objects.get(id=test_id)

        if not test:
            raise NotFound(f"Not found test {test_id}")

        if not test.owner == self.request.user:
            raise PermissionDenied("Access denied")

        task = Task.objects.get(id=task_id, test=test)

        if not task:
            raise NotFound(f"Not found task {task_id}")

        # delete a options
        #TaskOption.objects.filter(task=task).delete()

        #print(opts)
        #if opts:
        #    opts.delete()
        #print(task)
        #task.delete()

        return Response(status=200)

"""
class DeleteTask_APIView(APIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]

    def delete(self):
        test_id = self.kwargs.get("pk", None)
        task_id = self.kwargs.get("task_id", None)
        if not test_id or not task_id:
            raise ParseError(code=400)

        test = Test.objects.get(id=test_id)

        if not test:
            raise NotFound(f"Not found test {test_id}")

        if not test.owner == self.request.user:
            raise PermissionDenied("Access denied")

        task = Task.objects.get(id=task_id, test=test)

        if not task:
            raise NotFound(f"Not found task {task_id}")

        # delete a options
        opts = TaskOption.objects.get(task=task)

        print(opts)
        #if opts:
        #    opts.delete()
        #task.delete()
        print(task)

        return Response(status=200)
"""

"""
# /tests/<int:pk>/create_task
class CreateTask_APIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsTutorOrAdmin]
    serializer_class = CreateTaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        #serializer = CreateTaskSerializer(data=self.request.data)
        test_id = self.kwargs.get("pk")

        if not pk:
            raise ParseError(code=400)

        opt_data_len = len(self.request.data["options"])
        opt_data = self.request.data.pop("options")

        options = TaskOptionsSerializer(data=opt_data)

        test = Test.objects.get(id=test_id)
        serializer.test = test
        task = CreateTestSerializer(self.request.data)

        raise NotFound(f"serializer {}")

        #options.task = 

        if not test:
            raise NotFound(f"not found test {pk}")

        if not test.owner == self.request.user:
            raise PermissionDenied(f"not allowed test {test.id}")

        if serializer.is_valid():
            options_count = len(self.request.data['options'])
            answer = int(self.request.data['correct_answer'])

            if answer > options_count:
                raise ParseError(code=400)

            serializer.test = test
            serializer.options_count = options_count
            serializer.save()
            test.tasks_count += 1
            test.save()
"""
