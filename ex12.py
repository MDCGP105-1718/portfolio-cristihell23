#Hotel Cost
def hotel_cost (nights):
    night = 70

#Plane Ticket Cost
def plane_ticket_cost (city,seat_class):
    ticket_cost = 0
    multiplier = 0
#City Condition
    if city == "New York":
        ticket_cost = 2000
    if city == "Auckland":
        ticket_cost = 790
    if city == "Venice":
        ticket_cost = 154
    if city == "Glasgow":
        ticket_cost = 65
    else "We don't have this destination"

#Seat Condition
    if seat_class == "Economy":
        multiplier = 1
    if seat_class == "Premium":
        multiplier = 1.3
    if seat_class == "Business":
        multiplier = 1.6
    if seat_class == "First":
        multiplier = 1.9

#Rental car Cost
def rental_car_cost(days):
    daily_cost = 30
    t_cost = days * daily_cost
    if days > 7:
        t_cost -= 50
    elif days > 3:
        t_cost -= 30
    return(t_cost)

#Total cost definition
def total_cost (city,days):
