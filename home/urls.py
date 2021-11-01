from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('main/',views.main,name='main'),
    path('logout/',views.logout,name='logout'),
    path('add/',views.add,name='add'),
    path('main/team/<int:myid>',views.teaminfo,name='teaminfo'),
    path('main/team/main/team/<int:myid>/update',views.update,name='update'),
    path('main/team/main/team/<int:myid>/delete',views.delete,name='delete'),
]