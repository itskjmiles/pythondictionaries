service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer_name}.")
    else:
        print("Ticket ID already exists. Please choose a different ID.")

def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Status of ticket {ticket_id} updated to {new_status}.")
    else:
        print("Invalid ticket ID.")

def display_tickets(status=None):
    print("Service Tickets:")
    if status:
        filtered_tickets = {tid: details for tid, details in service_tickets.items() if details["Status"] == status}
        if filtered_tickets:
            for ticket_id, details in filtered_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
        else:
            print("No tickets found with the specified status.")
    else:
        for ticket_id, details in service_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

print("Initial Service Tickets:")
display_tickets()
print()

open_ticket("Ticket003", "Charlie", "Website loading issue")
open_ticket("Ticket001", "Dave", "Forgot password") 
print()

update_ticket_status("Ticket002", "open")
update_ticket_status("Ticket004", "closed")
print()

print("Open Service Tickets:")
display_tickets("open")
print()

print("All Service Tickets:")
display_tickets()
