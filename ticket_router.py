 
def route_ticket(ticket):
    category = ticket["category"]
    priority = ticket["priority"]

    if category == "hardware":
        return "Desktop Support Team"

    elif category == "software":
        if priority == "high":
            return "Tier 2 Support"
        else:
            return "Application Operations Center"

    elif category == "network":
        return "Network Opereations Center"

    else:
        return "General IT Queue"