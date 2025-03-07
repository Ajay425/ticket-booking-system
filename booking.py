from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used for flashing messages

@app.route("/", methods=["GET", "POST"])
def index():
    cities = ["Bangalore", "Chennai", "Goa", "Pune", "Hyderabad", "Mumbai"]
    bus_services = ["RedBus", "VRL Travels", "KSRTC"]
    
    if request.method == "POST":
        session["booking_details"] = request.form.to_dict()
        return redirect(url_for("select_seats"))

    return render_template("index.html", cities=cities, bus_services=bus_services)

@app.route("/select-seats", methods=["GET", "POST"])
def select_seats():
    if "booking_details" not in session:
        return redirect(url_for("index"))  # Redirect if no booking details

    if request.method == "POST":
        session["selected_seats"] = request.form.getlist("selected_seats")
        flash("Seats selected successfully!", "success")
        return redirect(url_for("thank_you"))

    return render_template("select_seats.html")

@app.route("/thank-you")
def thank_you():
    if "booking_details" not in session or "selected_seats" not in session:
        return redirect(url_for("index"))  # Redirect if no booking details

    return render_template("thank_you.html", booking=session["booking_details"], seats=session["selected_seats"])

if __name__ == "__main__":
    app.run(debug=True)
