"""Movie theatre ticketing system - v2
Get category and number of tickets
Created by Robson Butler
"""

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

    print(f"You have ordered {number_tickets} {ticket} ticket(s)!")
    ticket_wanted = input("Do you want to sell another ticket (Y/N):"
                          "").upper()


# Main routine
sell_ticket()
