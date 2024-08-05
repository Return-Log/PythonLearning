# 创建和使用类
class Dog:
    """模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is sitting")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over")


my_dog = Dog('Willie', 6)  # 根据类创建实例
print(my_dog.name)  # 访问属性
print(my_dog.age)
my_dog.sit()  # 调用方法

your_dog = Dog('an', 89)  # 创建多个实例
your_dog.sit()


# 使用类和实例
class Car:
    """模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 属性指定默认值

    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """
        里程表读数设为指定值
        禁止将表往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("！！！YOU CAN'T ROLL BACK！！！")

    def increment_odometer(self, miles):
        """数值增大到指定的量"""
        self.odometer_reading += miles

    def read_odometer(self):
        """打印行驶里程"""
        print(f"This car has {self.odometer_reading} mile on it")


my_car = Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())

my_car.update_odometer(87)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()


# 继承
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类属性,再初始化特有属性"""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """打印描述电池容量信息"""
        print(f"This car has a {self.battery_size}-kWh battery")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
