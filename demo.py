from Bill import Bill
from Group import Group
from datetime import datetime

def main():
    # DEMO USECASE :

    unformatted_timestamp = datetime.now()
    timestamp = unformatted_timestamp.strftime("%Y_%m_%d_%H:%M:%S")

    hamburg_bill = Bill("Hamburg", timestamp)
    pedigree = Group("Pedigree")

    members_list = [
        'Achal',
        'Rishabh',
        'Drishya',
        'Pratsss'
    ]

    items_list = {
        'King of Chicken Burger': 139,  
        'Veg Sandwich': 195,            
        'Mughalai Chicken Wrap': 75,    
        'Vanilla Avil Milk': 49,        
        'Butterscotch Avil Milk': 59,   
        'Grape Lime Juice': 45          
    }

    # Adding Food Items
    for item_name in items_list:
        hamburg_bill.add_items(item_name, items_list[item_name])
    # print(f"\nAdded Items: \n{hamburg_bill.items}")           # ! DEBUGGING

    # Adding Members
    for member in members_list:
        hamburg_bill.add_members(member)
    # print(f"\nAdded Members: \n{hamburg_bill.members}")       # ! DEBUGGING

    # Adding Members sharing that Item
    hamburg_bill.add_members_to_item("King of Chicken Burger", ["Drishya", "Rishabh"])
    hamburg_bill.add_members_to_item("Veg Sandwich", ["Achal"])
    hamburg_bill.add_members_to_item("Mughalai Chicken Wrap", ["Rishabh"])
    hamburg_bill.add_members_to_item("Vanilla Avil Milk", ["Pratsss", "Achal"])
    hamburg_bill.add_members_to_item("Butterscotch Avil Milk", ["Rishabh", "Achal"])
    hamburg_bill.add_members_to_item("Grape Lime Juice", ["Drishya"])
    # print(hamburg_bill.item_shares)                           # ! DEBUGGING
    
    print("\n",hamburg_bill.name)

    # Calculating the Individual Shares
    hamburg_bill.find_individual_shares()

    # Adding the bill to the group object
    pedigree.add_bill(f"{hamburg_bill.name}")
    # print(pedigree.bills)                                     # ! DEBUGGING

if __name__ == '__main__':
    main()
