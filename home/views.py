from django.shortcuts import render,redirect
from home.models import qu
from django.template import loader
from django.http import HttpResponse
from home.forms import VoteForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@ login_required
# return all qus
def all_qus(request):
    all_qus = qu.objects.all()
    # to display on main page
    context = {
        'all_qus':all_qus,
    }
    template = loader.get_template('all_qus.html')

    return HttpResponse(template.render(context,request))

# @login_required
# open qu link
def qu_detail(request,qu_id):
    req_qu = qu.objects.get(id=qu_id)
    # if user has voted
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choice']

            if selected_choice == '1':
                req_qu.vote1+=1
            elif selected_choice == '2':
                req_qu.vote2+=1
            elif selected_choice == '3':
                req_qu.vote3+=1
        
            req_qu.save()
            return redirect(f'/home/qus/{qu_id}/')
    else:
        form=VoteForm()

    context = {
        'req_qu':req_qu,
        'form':form,
    }

    template = loader.get_template('qu_detail.html')

    return HttpResponse(template.render(context,request))