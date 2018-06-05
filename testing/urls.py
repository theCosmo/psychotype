from django.conf.urls import url

from . import views


urlpatterns = [
    url('test/', views.ProfChoiceView.as_view(), name='test'),
    url('ege_points', views.GetEgePoints.as_view(), name='ege_points'),
]
