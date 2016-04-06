from django.shortcuts import render, redirect
from .forms import AddResponseForm

def add_response(request):
    if request.method == "POST":
        form = AddResponseForm(request.POST)
        if form.is_valid():
            response = form.save()
            response.save()
            return redirect('testapp.views.add_response')
    else:
        form = AddResponseForm()
    return render(request, 'add_response.html', {'form': form})
