
class Bill():
    def __init__(self):
        self.total_amount = 0
        self.items = {}                                                 # ? Item name : Item Price
        self.members = {}                                               # ? Member name : Member's Share
        self.item_shares = {}                                           # ? Item name : Member sharing

    def add_members(self, member: str):
        self.members[member] = 0                                        # ? Initially each member's share will be 0

    def add_items(self, name: str, price: int):
        self.items[name] = price                                        # ? Adding the item to the items list along with its price
        self.item_shares[name] = []                                     # ? Adding the item to the item_shares list and initializing its corresponding member list as [] 
        self.total_amount += price                                      # ? Adding to the total price as we add the item to the bill

    def add_members_to_item(self, item: str, members: list):
        for member in members:
            if item in self.item_shares:
                self.item_shares[item].append(member)                   # ? If the item is present in the item_shares list then append the member who is sharing the item

    def find_individual_shares(self):
        for member in self.members:
            self.item_serial_number = 1                                 # ? Initializing the item serial number from 1
            print(f"\b{member}: \n")                                    # ? Printing names of each member
            for item in self.item_shares:                   
                if member in self.item_shares[item]: 
                    share_amount = self.items[item] / len(self.item_shares[item])             # ? If the member is present in the list of members for that key item
                    print(f"{self.item_serial_number}) {item} : {share_amount}")              # ? Calculating the item's share amount for that item
                    self.members[member] += share_amount                                      # ? Adding the share amount to the member's share amount
                    self.item_serial_number += 1                        # ? Incrementing the item serial number
            print("-------------------------------------")
            print(f"TOTAL : {self.members[member]}")                    # ? Displaying the total share of the member

    def member_item_count(self):
        for item in self.item_shares:
            print(f"{item} : {len(self.item_shares[item])}")            # ? Displaying the number of members sharing that item

def main():
    # DEMO USECASE :

    hamburg_bill = Bill()

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
    # print(hamburg_bill.item_shares)                             # ! DEBUGGING
    
    # Calculating the Individual Shares
    hamburg_bill.find_individual_shares()

if __name__ == '__main__':
    main()
