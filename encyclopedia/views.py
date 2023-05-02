from django import forms
from django.shortcuts import render
from . import util
import markdown2
import random

class NewEntryForm(forms.Form): #form class that inherits built in form lib from Django
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={"rows":5, "cols":20}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    try: 
        entry = markdown2.markdown(util.get_entry(title))

    except:
        entry = f"<h1>404: {title} was not found.</h1>"
        title = "404: Page not found."
    
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "title": title
    })

def add(request):

    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid(): 
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return entry(request, title)

        else: #server side validation
            return render (request, "encyclopedia/add_page.html", {
                "form": form
            })
    return render(request, "encyclopedia/add_page.html",{ 
        "form": NewEntryForm() #creates a blank form
    })
    
def edit(request, title):
    form = NewEntryForm({
            "content":util.get_entry(title),
            "title": title
    })

    form.fields['title'].widget.attrs['readonly'] = True
    form.fields['title'].widget.attrs['class'] = 'gray-out'
    
    return render (request, "encyclopedia/add_page.html", {
        "form": form
    })


def random_page(request):
    title = (random.choice(util.list_entries()))
    return entry(request, title)


def search_page(request):
    search_str = request.POST.get('q') #same with request.POST['q'] ->minor difference
    entries = util.list_entries()
    search_list = [entry for entry in entries if search_str.upper() in entry.upper()]
    
    if search_str in entries:
        return entry(request, search_str)
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": search_list
        })