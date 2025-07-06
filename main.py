
category = input("Enter ticket category (hardware/software/network): ").lower()
priority = input("Enter ticket priority (low/medium/high): ").lower()

ticket = {
    "category": category, "priority": priority
}

print("\nNew Ticket Created:")
print(f"Category: {ticket['category']}")
print(f"Priority: {ticket['priority']}")

from ticket_router import route_ticket

assigned_group = route_ticket(ticket)

print(f"\nTicket assigned to: {assigned_group}")

import csv

with open("tickets.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for ticket in reader:
        assigned_group = route_ticket(ticket)
        print("\nNew Ticket Created:")
        print(f"Category: {ticket['category']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Ticket assigned to: {assigned_group}")
