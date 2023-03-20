"""Movie theatre ticketing system - v6
Print end summary
Created by Robson Butler
"""


# Component 6 - Print summary
def print_summary(tickets_sold, adult_tickets, student_tickets, child_tickets,
                  gift_vouchers, total_sales):
    print("=" * 40)
    print(f"The total tickets sold today was {tickets_sold}\n"
          f"This was made up of: \n"
          f"\t{adult_tickets} for adults; and \n"
          f"\t{student_tickets} for students; and \n"
          f"\t{child_tickets} for children; and \n"
          f"\t{gift_vouchers} gift vouchers \n"
          f"Sales for the day came to ${total_sales:.2f}")
    print("=" * 40)


# Component 4 - Confirm order
def confirm_order(ticket, num_tickets, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nConfirm your order of {num_tickets} {ticket} "
                        f"ticket(s)!"
                        f"at a cost of ${cost:.2f} each; and a total cost of " 
                        f"${cost * num_tickets:.2f}!"
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

            # Component 5 - Update totals
            total_sales += cost * number_tickets
            tickets_sold += number_tickets
            if ticket == "A":
                adult_tickets += number_tickets
            elif ticket == "S":
                student_tickets += number_tickets
            elif ticket == "C":
                child_tickets += number_tickets
            else:
                gift_vouchers += number_tickets
        else:
            print("Order cancelled")

        ticket_wanted = input("Do you want to sell another ticket (Y/N):"
                              "").upper()

    # Component 6 - Print summary
    print_summary(tickets_sold, adult_tickets, student_tickets,
                  child_tickets, gift_vouchers, total_sales)


# Main routine
sell_ticket()
print("Goodbye\nThanks for using Fun Movies")
