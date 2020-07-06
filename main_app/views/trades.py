from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main_app.models import Crazybone, TradeRequest
from django.contrib.auth.models import User

# Create your views here.
def index(req):
    return render(req, 'trades/form.html')

def result(req):
    user_crazybones = User.objects.get(username=req.user).profile.cb.all()
    print(user_crazybones)

    search_method = req.GET['search-method']
    search_query = req.GET['search-query']
    if search_method == "cb-name":
        try:
            profiles = Crazybone.objects.get(name=search_query).profile_set.all()
            if(len(profiles) != 0):
                results = []
                for profile in profiles:
                    results.append({
                        "user": profile.user.username,
                        "cb": search_query
                    })
            else:
                results = "No user has that Crazy Bone Yet"
        except:
            results = None
    else:
        try:
            crazybones = User.objects.get(username=search_query).profile.cb.all()
            results = []
            for crazybone in crazybones:
                results.append({
                    "user": search_query,
                    "cb": crazybone.name
                })
        except:
            results = None

    return render(req, 'trades/results.html', {'results': results, 'user_crazybones':user_crazybones, 'search_method':search_method})

def create(req):
    selected_values = req.POST['selected'].split('-')
    print(selected_values)
    try:
        new_user_from = req.user.profile
        new_user_to = User.objects.get(username=selected_values[0]).profile
        new_cb_offered = new_user_from.cb.get(name=req.POST['offered'])
        new_cb_wanted = new_user_to.cb.get(name=selected_values[1])
        new_trade = TradeRequest.objects.create(user_from=new_user_from, user_to=new_user_to, cb_wanted=new_cb_wanted, cb_offered=new_cb_offered)
        return HttpResponse("<h1>Hello World </h1>")
    except Exception as err:
        print(err)
        return HttpResponse("Something went wrong")