import csv


class Item:
    pay_rate = 0.8
    all=[] # create an empty list
    
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations to the recieved arguments
        assert price>=0,f"Price {price} is not greater or equal to zero"
        assert quantity>=0, f"Quantity {quantity} is not greater or equal to zero"

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price *self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open ('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
           # print(item)
        
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    
    def __repr__(self): # Used to get unique objects
        return f"Item('{self.name}',{self.price}, {self.quantity})"
    

# item1 = Item("Phone", 100,2)
# item2 = Item("Laptop", 1000,3)
# item3 = Item("Mouse", 50,4)
# item4 = Item("Keyboard", 100,4)


Item.instantiate_from_csv()

print(Item.all)
# for instance in Item.all:
#     print(instance.name)
