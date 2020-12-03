# class = blueprint
class Car():
    def __init__(self, **kwargs):
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
        return f"Car with {self.wheels} wheels"

class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs) # 부모 클래스를 호출하는 함수
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"

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

ferrari2 = Convertible(color="white", price="$100")
print(ferrari2.color, ferrari2.price)