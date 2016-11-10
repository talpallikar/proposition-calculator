#Tax Calculator
import html
from flask import Flask, request, render_template

app = Flask(__name__)
COST = 1159/12

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
    #return new info
    return render_template("output.html", commute_distance=dist, current_time=ctime, bad_time = btime, new_time=gtime, ann_inc=annual_incr, month_inc = monthly_incr, net_cost=gcost)

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

        #https://www.google.com/maps/dir/Texas+Capitol/Western+Trail+Apartments,+2422+Western+Trails+Blvd,+Austin,+TX+78745/@30.2317009,-97.8062928,13z/data=!4m18!4m17!1m5!1m1!1s0x0:0xcb6f5722a795d039!2m2!1d-97.7403505!2d30.2746652!1m5!1m1!1s0x865b4b39d05f0529:0xa75830de1b8c30d3!2m2!1d-97.7966319!2d30.2302436!2m3!1b1!7e2!8j1478452800!3e0

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


app.run()