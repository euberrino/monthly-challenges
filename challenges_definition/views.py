from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    'december': 'Eat no meat for the entire month'
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    response_data = f"""<h1>Choose your month</h1>
                    <ul>{list_items}</ul>"""
    return HttpResponse(response_data)


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
        response_data = f'<h1>{challenge_text}</h1>'
    except:
        return HttpResponseNotFound("<h1>This month is not suppported!</h1>")
    return HttpResponse(response_data)
