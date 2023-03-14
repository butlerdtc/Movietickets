"""Movie theatre ticketing system - v3
Calculate price of tickets
Created by Robson Butler
"""


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

    print(f"You have ordered {number_tickets} {ticket} ticket(s)!"
          f"at a cost of ${cost:.2f} each; and a total cost of " 
          f"{cost * number_tickets:.2f}!")

    ticket_wanted = input("Do you want to sell another ticket (Y/N):"
                          "").upper()


# Main routine
sell_ticket()
