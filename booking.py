from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

def save_ticket(name, email, phone, from_location, to_location, date, return_date, ticket_type, tickets, bus_service):
    with open("tickets.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, from_location, to_location, date, return_date, ticket_type, tickets, bus_service])

@app.route("/", methods=["GET", "POST"])
def index():
    cities = ["Bangalore", "Chennai", "Hyderabad", "Delhi", "Mumbai", "Kolkata", "Pune"]
    bus_services = ["RedBus", "VRL Travels", "KSRTC"]
    
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
        
        if not all([name, email, phone, from_location, to_location, date, ticket_type, tickets, bus_service]):
            return render_template("index.html", error="All fields are required!", cities=cities, bus_services=bus_services)
        
        if from_location == to_location:
            return render_template("index.html", error="Departure and destination cities cannot be the same!", cities=cities, bus_services=bus_services)
        
        save_ticket(name, email, phone, from_location, to_location, date, return_date, ticket_type, tickets, bus_service)
        return redirect(url_for("success"))
    
    return render_template("index.html", cities=cities, bus_services=bus_services)

@app.route("/success")
def success():
    return "<h1>Ticket booked successfully!</h1><a href='/'>Go back</a>"

if __name__ == "__main__":
    app.run(debug=True)