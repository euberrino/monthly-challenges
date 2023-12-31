from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string 

# Create your views here.
monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 minutes every day',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for the entire month',
    'may': "Be greatful for 5 things",
    'june': 'Walk for at least 20 minutes',
    'july': 'Learn Django for at least 20 minutes every day!',
    'august': 'Eat no meat for the entire month',
    'september': 'Eat no meat for the entire month',
    'october': 'Eat no meat for the entire month',
    'november': 'Eat no meat for the entire month',
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges_definition/index.html', {'months': months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)) or (month <= 0):
        return HttpResponseNotFound("<h1>This month is not suppported!</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges_definition/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
