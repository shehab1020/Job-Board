from django.urls import path
from . import views,api

app_name = 'job'

urlpatterns = [
    # path('',views.job),
    path('',views.job_list, name="list"),
    path('post',views.job_post, name = "post"),
    path('search', views.search, name='search'),
    path('<str:slug>',views.job_info, name="info"),

    path('api/list/', api.JobList , name='api'),
    path('api/list/<str:id>', api.get_job , name='api'),
    path('api/addjob/', api.AddJob , name='addjob'),

]

