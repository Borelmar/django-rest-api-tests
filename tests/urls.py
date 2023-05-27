from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
        # test
        path('tests/create/', CreateTest_APIView.as_view()),
        path('tests/<int:pk>/info/', GetTestInfo_APIView.as_view()),
        path('tests/<int:pk>/detail/', GetTestDetail_APIView.as_view()),
        path('tests/<int:pk>/delete/', DeleteTest_APIView.as_view()),
        path('tests/<int:pk>/create_result/', UserResultCreateView.as_view(), name='user-result-create'),
        path('tests/<int:pk>/result_detail/',  UserResultInfoView.as_view()),

        path('tests/<int:pk>/get_user_results/', GetUserResultsView.as_view()),
        path('tests/<int:pk>/detail_for_user/',GetTestDetailForUser_APIView.as_view()),

        path('tests/<int:test_id>/statistic/', GetTestStatisticAPIView.as_view(), name='user-test-statistics'),

        #path('tests/<int:pk>/update', UpdateTest_APIView.as_view()),
        #path('tests/<int:pk>/info', GetTestInfo_APIView.as_view()),
        #path('tests/<int:pk>/delete', DeleteTest_APIView.as_view()),
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
