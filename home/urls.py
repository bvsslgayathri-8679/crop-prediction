from django.urls import path


from . import views

urlpatterns = [
    path('', views.home,name='home'), 
    path('result.html',views.predict,name='results'),
    path('predict',views.predict,name='predict')
]
