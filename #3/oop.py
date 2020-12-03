# class = blueprint
class Car():
    def __init__(self, *args, **kwargs):
        # print(kwargs.get)
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def start(self):
        print(self.color)
        print("I started")

    def __str__(self):
        return "lalala"

# class 안에 있는 function은 method라고 한다.
# print(dir(Car))

# instance
porsche = Car() # Instantiation

print(porsche)
porsche.color = "Red"
porsche.start()

ferrari = Car()
ferrari.color = "Yellow"

print(porsche.color)
print(ferrari.color)

porsche2 = Car(color="green", price="$40")
print(porsche2.color, porsche2.price)

mini = Car()
print(mini.color, mini.price)