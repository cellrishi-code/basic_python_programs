class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)


class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state


Add = Address("war", 506004, "tel")

cust = Customer("rishi", "Male", Add)

cust.edit_profile("rocky","delhi", 10000, "delhi")

print(cust.name)
print(cust.address.city)
print(cust.address.pin)
print(cust.address.state)