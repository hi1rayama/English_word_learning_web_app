from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('user_home/',views.UserHomeView.as_view(),name="UserHome"),
    path('user_home/resister_word/',views.ResisterWordView.as_view(),name="ResisterWord"),
    path('user_home/learning_home/',views.LearningHomeView.as_view(),name="LearningHome"),
    path('user_home/learning_home/learning/<str:value>/',views.LearningView.as_view(),name="Learning"),
    path('user_home/learning_home/result',views.ResultView.as_view(),name="Result"),
    path('user_home/weak_list/',views.WeakListView.as_view(),name="WeakList"),
    path('user_home/weak_list/edit/',views.WeakListEdit,name="WeakListEdit"),
    path('accounts/login/', views.MyLoginView.as_view(), name="login"),
    path('accounts/logout/', views.MyLogoutView.as_view(), name="logout"),
    path('accounts/index/',views.IndexView.as_view(), name="index"),
    path('accounts/create/',views.UserCreateView.as_view(),name="create"),
]

