#Tax Calculator
import html
from flask import Flask, request, render_template

app = Flask(__name__)
COST = 1159/12
#app.add_url_rule('/favicon.ico',
 #                redirect_to=url_for('static', filename='favicon.ico'))

@app.route('/')
def myform():
    return render_template("input.html")

@app.route('/', methods=['POST', 'GET'])
def myform_post():
    #get form input
    value = request.form['money']
    route = int(request.form['route'])
    #do calculations on tax
    annual_incr = calculate_tax(value)
    monthly_incr = annual_incr/12
    monthly_return = COST - monthly_incr
    nroute=0
    ctime=0
    dist=0
    gtime=0 
    btime=0
    gcost=0
    nroute, ctime, dist, gtime, btime, gcost = calculate_route(route)
    tweet = prep_tweet(gtime, btime, gcost)
    #return new info
    return render_template("output.html", route = route, tweet = tweet, commute_distance=dist, current_time=ctime, bad_time = btime, new_time=gtime, ann_inc=annual_incr, month_inc = monthly_incr, net_cost=gcost)

def calculate_tax(property_value):
    annual_tax = (int(property_value)//100) * .0225
    return annual_tax 

def calculate_route(route):
    time=0
    dist=0
    gtime=0 
    btime=0
    gcost=0
    if route == 1:
        time = 60
        dist = 7.3
        gtime = time*.49
        btime = time*1.13
        gcost = 1159*.51

    if route == 2:
        time = 18 
        dist = 5.6
        gtime = time*.8
        btime = time*1.4
        gcost = 1159*.8

    if route == 3:
        time = 28
        dist = 5.5
        gtime = time*.49
        btime = time*1.13
        gcost = time*.49

    return route, time, dist, gtime, btime, gcost

def prep_tweet(gtime, btime, gcost):
    base = "https://twitter.com/intent/tweet?"
    text = "&text="+"Proposition%201%20saves%20me%20"+str((btime-gtime)*2)+"%20minutes%20per%20day,%20and%20$"+str(gcost)+"%20per%20month!"
    htag = "&hashtags="+"MoveAustinForward,ATX,Prop1" 
    
    tweet = base+text+htag
    return tweet


app.run()