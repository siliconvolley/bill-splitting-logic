
class Bill():
    def __init__(self):
        self.total_amount = 0
        self.items = {}             # Item name : Item Price
        self.members = {}           # Member name : Member's Share

    def add_members(self, member):
        self.members[member] = 0

    def add_items(self, name, price):
        self.items[name] = price
        self.total_amount += price


def main():
    hamburg_bill = Bill()

    members_list = [
        "Achal",
        "Rishabh",
        "Drishya",
        "Pratsss"
    ]

    items_list = {
        "King of Chicken Burger": 139,  
        "Veg Sandwich": 195,            
        "Mughalai Chicken Wrap": 75,    
        "Vanilla Avil Milk": 49,        
        "Butterscotch Avil Milk": 59,   
        "Grape Lime Juice": 45          
    }

    items_shares = {
        "King of Chicken Burger": ["Drishya", "Rishabh"],
        "Veg Sandwich": ["Achal"],
        "Mughalai Chicken Wrap": ["Rishabh"],    
        "Vanilla Avil Milk": ["Pratsss", "Achal"],        
        "Butterscotch Avil Milk": ["Rishabh", "Achal"],   
        "Grape Lime Juice": ["Drishya"]          
    }

    # Calculating total amount
    for item in items_list:
        hamburg_bill.total_amount += items_list[item]
    # print(f"\nTotal amount : {hamburg_bill.total_amount}")    # ! DEBUGGING

    # Adding Members
    for member in members_list:
        hamburg_bill.add_members(member)
    # print(f"\nAdded Members: \n{hamburg_bill.members}")       # ! DEBUGGING


    # Adding Food Items
    for item_name in items_list:
        hamburg_bill.add_items(item_name, items_list[item_name])
    # print(f"\nAdded Items: \n{hamburg_bill.items}")           # ! DEBUGGING

    # # Adding members to items
    # for item in items_shares:
    #     if item == "Veg Sandwich":
    #         items_shares[item].append("Rishabh")

    # Counting number of members in each item
    print("\nMember count for each item: \n")
    for item in items_shares:
        print(f"{item} : {len(items_shares[item])}")        # ! DEBUGGING

    # Individual share info
    print("\nIndividual share info: \n")
    for member in members_list:
        item_serial_number = 1
        print(f"\n{member}: \n")
        for item in items_shares:
            if member in items_shares[item]:
                print(f"{item_serial_number}) {item} : {items_list[item]/len(items_shares[item])}")
                hamburg_bill.members[member] += items_list[item] / len(items_shares[item])
                item_serial_number += 1
        print("---------------------------------------")
        print(f"TOTAL : {hamburg_bill.members[member]}")
    
if __name__ == '__main__':
    main()
