
class Group:
    def __init__(self, name: str):
        self.name = name
        self.bills = []

    def add_bill(self, name: str):
        if name not in self.bills:
            self.bills.append(name)
