hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} booked for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print("Invalid room number.")

def check_out(room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"Checked out {customer_name} from room {room_number}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print("Invalid room number.")

def display_rooms_status():
    print("Hotel Room Status:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: {details['status'].capitalize()} - {details['customer']}")

print("Initial Room Status:")
display_rooms_status()
print()

book_room("101", "Alice")
book_room("103", "Bob") 
print()

check_out("102")
check_out("103") 
print()

print("Updated Room Status:")
display_rooms_status()
