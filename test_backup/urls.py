from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
        # test
        path('tests/<int:pk>/info', GetTestInfo_APIView.as_view()),
        path('tests/<int:pk>/delete', DeleteTest_APIView.as_view()),
        path('tests/create', CreateTest_APIView.as_view()),
        path('tests/<int:pk>/update', UpdateTest_APIView.as_view()),

        # task
        path('tests/<int:pk>/get_tasks', GetTestTasks_APIView.as_view()),
        path('tests/<int:pk>/create_task', CreateTask_APIView.as_view()),
        path('tests/<int:pk>/<int:task_id>/delete_task', DeleteTest_APIView.as_view()),
]

"""
# tests

# tasks
path('tests/<int:pk>/edit_task', DeleteTest_APIView.as_view()),

# for user
path('tests/<int:pk>/savetest', DeleteTest_APIView.as_view()),
path('tests/<int:pk>/shoresult', DeleteTest_APIView.as_view()),
path('tests/<int:pk>/user_gettasks', DeleteTest_APIView.as_view()),
"""




#path('tests/<int:pk>/', GetTestInfo.as_view()),
#path('', include(router.urls)),
#path('tests', include(router.urls)),

#router = routers.DefaultRouter()
#router.register(r'tests', TestsViewSet)
