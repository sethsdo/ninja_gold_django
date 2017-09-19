from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'current_activity' not in request.session:
        request.session['current_activity'] = []
    print "hello"
    return render(request, 'temp/index.html')


def process_money(request):
    print "hello"
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    print time
    earn_type = request.POST['building']
    # print choice
    current_gold = 0
    if earn_type == 'farm':
        current_gold = random.randint(10, 20)
        #print session['gold']
    elif earn_type == 'cave':
        current_gold = random.randint(5, 10)
        #print session['gold']
    elif earn_type == 'house':
        current_gold = random.randint(2, 5)
        #print session['gold']
    elif earn_type == 'casino':
        current_gold = random.randint(-50, 50)
        print request.session['current_activity']
        #print session['gold']
        request.session['gold'] += current_gold
        print current_gold
        if current_gold < 0:
            if request.session['gold'] > 0:
                request.session['current_activity'].append(
                    "Entered a {} and You lost {} golds... Ouch.. {}".format(earn_type, current_gold, time))
                print request.session['current_activity']
            else:
                request.session['current_activity'].append(
                    "You enterd a {} are in dept {} golds... Ouch.. {}".format(earn_type, current_gold, time))
                return redirect('/')
        else:
            request.session['current_activity'].append("Entered a {} and won {} golds... Feeling Lucky.. ({})".format(
                earn_type, current_gold, time))
        return redirect('/')

    request.session['gold'] += current_gold

    request.session['current_activity'].append("Earned {} golds from the {}! ({})".format(
        current_gold, earn_type, time))

    return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')


 
