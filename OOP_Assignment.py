# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Battery Life: {self.battery_life} hours")

    def power_on(self):
        print(f"{self.model} is now powered on.")

# Subclass for Android
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, android_version):
        super().__init__(brand, model, storage, battery_life)
        self.android_version = android_version

    def display_info(self):
        super().display_info()
        print(f"Android Version: {self.android_version}")

# Subclass for iPhone
class IPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, ios_version):
        super().__init__(brand, model, storage, battery_life)
        self.ios_version = ios_version

    def display_info(self):
        super().display_info()
        print(f"iOS Version: {self.ios_version}")

#Testing the classes
samsung = AndroidPhone("Samsung", "Galaxy S23", 256, 20, "Android 13")
iphone = IPhone("Apple", "iPhone 14", 128, 18, "iOS 17")

samsung.display_info()
print("------")
iphone.display_info()
