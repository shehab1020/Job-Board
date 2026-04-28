from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job, Apply
from django.core.paginator import Paginator
from .forms import Login_form
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery




def job(request):
    Job_objects =Job.objects.all()
    context = {'Job_objects': Job_objects}
    return render(request, 'shosh.html',context)

def job_list(request):
    jobs = Job.objects.all()

    paginator = Paginator(jobs,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj,'count': jobs}
    return render(request, 'job\job_list.html', context)

def job_info(request, slug):
    name = request.POST.get("name")
    email = request.POST.get("email")
    cv = request.POST.get("cv")
    website = request.POST.get("website")
    cover_letter = request.POST.get("cover_letter")
    job = get_object_or_404(Job, slug=slug)
    context = {'job':job}

    data = Apply(name=name, email= email, cv=cv, website=website, cover_letter=cover_letter, job=job)
    if request.method == "POST":
        data.save()
    return render(request, 'job\job_info.html', context)


@login_required
def job_post(request):
    
    if request.method == "POST":
        form = Login_form(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect(reverse("job:list"))
    else:
        form = Login_form()
    context = {'form':form}
    
    return render(request, 'job\job_post.html', context)




def search(request):
    query = None
    results = []

    if 'query' in request.GET:
        query = request.GET.get('query')
        search_vector = SearchVector('title', 'description')
        search_query = SearchQuery(query)
        results = Job.objects.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
            ).filter(search=query).order_by('-rank')
        
    context = {
        'query':query,
        'results':results,
    }
    
    return render(request, 'job\search.html', context)
