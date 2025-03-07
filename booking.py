from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

def save_ticket(name, email, phone, from_location, to_location, date, return_date, ticket_type, tickets, bus_service, return_time):
    with open("tickets.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, from_location, to_location, date, return_date, ticket_type, tickets, bus_service, return_time])

@app.route("/", methods=["GET", "POST"])
def index():
    cities = ["Bangalore", "Chennai", "Hyderabad", "Delhi", "Mumbai", "Kolkata", "Pune"]
    bus_services = {
        "RedBus": ["08:00 AM", "12:00 PM", "06:00 PM"],
        "VRL Travels": ["09:30 AM", "03:00 PM", "09:00 PM"],
        "KSRTC": ["07:15 AM", "01:30 PM", "10:30 PM"]
    }
    return_bus_services = {
        "RedBus": ["07:00 AM", "11:00 AM", "05:00 PM"],
        "VRL Travels": ["10:00 AM", "04:00 PM", "08:00 PM"],
        "KSRTC": ["06:30 AM", "02:00 PM", "09:30 PM"]
    }
    
    today = datetime.today().strftime('%Y-%m-%d')
    
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        from_location = request.form.get("from_location")
        to_location = request.form.get("to_location")
        date = request.form.get("date")
        return_date = request.form.get("return_date") if request.form.get("ticket_type") == "return" else "N/A"
        ticket_type = request.form.get("ticket_type")
        tickets = request.form.get("tickets")
        bus_service = request.form.get("bus_service")
        return_time = request.form.get("return_time") if request.form.get("ticket_type") == "return" else "N/A"
        
        if not all([name, email, phone, from_location, to_location, date, ticket_type, tickets, bus_service]):
            return render_template("index.html", error="All fields are required!", cities=cities, bus_services=bus_services, return_bus_services=return_bus_services, today=today)
        
        if from_location == to_location:
            return render_template("index.html", error="Departure and destination cities cannot be the same!", cities=cities, bus_services=bus_services, return_bus_services=return_bus_services, today=today)
        
        if date < today:
            return render_template("index.html", error="You cannot book a ticket for a past date!", cities=cities, bus_services=bus_services, return_bus_services=return_bus_services, today=today)
        
        if ticket_type == "return" and (return_date < date or return_date < today):
            return render_template("index.html", error="Return date cannot be in the past or before the departure date!", cities=cities, bus_services=bus_services, return_bus_services=return_bus_services, today=today)
        
        save_ticket(name, email, phone, from_location, to_location, date, return_date, ticket_type, tickets, bus_service, return_time)
        return redirect(url_for("success"))
    
    return render_template("index.html", cities=cities, bus_services=bus_services, return_bus_services=return_bus_services, today=today)

@app.route("/success")
def success():
    return "<h1>Ticket booked successfully!</h1><a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(debug=True)
