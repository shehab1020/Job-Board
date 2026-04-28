from django.shortcuts import get_object_or_404
from .serializers import JobSerializer
from .models import Job
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .filters import JobFilter
from rest_framework.pagination import PageNumberPagination




@api_view(['GET'])
def JobList(request):
    all_jobs = Job.objects.all()
    # all_jobs = JobFilter(request.GET, queryset= Job.objects.all().order_by('id'))
    paginator = PageNumberPagination()
    paginator.page_size = 2
    queryset = paginator.paginate_queryset(all_jobs, request)
    data = JobSerializer(queryset, many=True).data

    return Response({'data':data})


@api_view(['GET'])
def get_job(request, id):
    job = get_object_or_404(Job, id=id)
    data = JobSerializer(job).data

    return Response({'data':data})



@api_view(["POST"])
def AddJob(request):
    data = request.data
    job = JobSerializer(data=data)
    print("=====================================================================")
    if job.is_valid():
        Job.objects.create(
            title = request.data.get('title'),
            salary = request.data.get('salary')
        )
    else:
        return Response({'error':'data is not vaild'})