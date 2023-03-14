"""Movie theatre ticketing system - v4
Confirm order
Created by Robson Butler
"""


# Component 4 - Confirm order
def confirm_order(ticket, num_tickets, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nConfirm your order of {number_tickets} {ticket} "
                        f"ticket(s)!"
                        f"at a cost of ${cost:.2f} each; and a total cost of " 
                        f"${cost * number_tickets:.2f}!"
                        f"\n'Y' or 'N' ").upper()

        if confirm == "Y":
            return True
        else:
            return False


# Component 3 - Calculate price of tickets
def get_price(type_):
    prices = [["A", 12.5], ["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Component 1 - Welcome screen and set up variables
def sell_ticket():
    print("****** Fun movies - ticketing system ******\n")

    adult_tickets = 0
    child_tickets = 0
    student_tickets = 0
    gift_vouchers = 0
    total_sales = 0
    tickets_sold = 0


# Component 2 - Get category and number of tickets
ticket_wanted = "Y"
while ticket_wanted == "Y":
    ticket_type = input("What kind of ticket do you want:\n"
                        "\t'A' for Adult, or\n"
                        "\t'S' for Student, or\n"
                        "\t'C' for Child, or\n"
                        "\t'G' for Gift Voucher\n"
                        ">> ").upper()
    ticket = ticket_type
    number_tickets = int(input(f"How many {ticket} tickets do you want: "))

    cost = get_price(ticket_type)

    if confirm_order(ticket, number_tickets, cost):
        print("Order confirmed")
    else:
        print("Order cancelled")

    ticket_wanted = input("Do you want to sell another ticket (Y/N):"
                          "").upper()


# Main routine
sell_ticket()
