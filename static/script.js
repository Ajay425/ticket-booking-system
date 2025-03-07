document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("ticket_type").addEventListener("change", toggleReturnOptions);
    document.getElementById("bus_service").addEventListener("change", updateBusTimings);
    document.getElementById("bus_time").addEventListener("change", updateReturnTimings);
    document.getElementById("adults").addEventListener("input", calculatePrice);
    document.getElementById("kids").addEventListener("input", calculatePrice);
    document.getElementById("seniors").addEventListener("input", calculatePrice);
    document.querySelectorAll("input[name='selected_seats']").forEach(seat => {
        seat.addEventListener("change", calculatePrice);
    });
});

function toggleReturnOptions() {
    var ticketType = document.getElementById("ticket_type").value;
    var returnDateInput = document.getElementById("return_date_input");
    var returnTimeDropdown = document.getElementById("return_time");

    if (ticketType === "return") {
        returnDateInput.style.display = "block";
        returnTimeDropdown.style.display = "block";
    } else {
        returnDateInput.style.display = "none";
        returnTimeDropdown.style.display = "none";
    }
}

function updateBusTimings() {
    var busTimeDropdown = document.getElementById("bus_time");
    var busService = document.getElementById("bus_service").value;

    var busTimings = {
        "RedBus": ["06:00 AM", "10:00 AM", "02:00 PM", "06:00 PM", "10:00 PM"],
        "VRL Travels": ["07:30 AM", "11:30 AM", "03:30 PM", "07:30 PM", "11:30 PM"],
        "KSRTC": ["05:00 AM", "09:00 AM", "01:00 PM", "05:00 PM", "09:00 PM"]
    };

    busTimeDropdown.innerHTML = '<option value="" disabled selected>Select Departure Time</option>';
    
    if (busService in busTimings) {
        busTimings[busService].forEach(time => {
            var option = document.createElement("option");
            option.value = time;
            option.textContent = time;
            busTimeDropdown.appendChild(option);
        });
    }
}

function updateReturnTimings() {
    var returnTimeDropdown = document.getElementById("return_time");
    var busService = document.getElementById("bus_service").value;

    var returnTimings = {
        "RedBus": ["07:00 AM", "11:00 AM", "03:00 PM", "07:00 PM", "11:00 PM"],
        "VRL Travels": ["08:30 AM", "12:30 PM", "04:30 PM", "08:30 PM", "12:30 AM"],
        "KSRTC": ["06:45 AM", "10:45 AM", "02:45 PM", "06:45 PM", "10:45 PM"]
    };

    returnTimeDropdown.innerHTML = '<option value="" disabled selected>Select Return Time</option>';
    
    if (busService in returnTimings) {
        returnTimings[busService].forEach(time => {
            var option = document.createElement("option");
            option.value = time;
            option.textContent = time;
            returnTimeDropdown.appendChild(option);
        });
    }
}

function calculatePrice() {
    var adults = parseInt(document.getElementById("adults").value) || 0;
    var kids = parseInt(document.getElementById("kids").value) || 0;
    var seniors = parseInt(document.getElementById("seniors").value) || 0;
    var selectedSeats = document.querySelectorAll("input[name='selected_seats']:checked").length;

    var adultPrice = 500;
    var seniorPrice = 375; 
    var kidsPrice = 0;

    var totalPrice = (adults * adultPrice) + (seniors * seniorPrice);

    document.getElementById("total_price").innerText = "₹" + totalPrice;
}
