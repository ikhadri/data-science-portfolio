# My first Python project in GitHub
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to Data Science.")
def ask_age():
    age = int(input("Enter your age: "))
    date_of_birth_year = 2026 - age
    print (f"You were born in {date_of_birth_year}. ")
def name_a_fruit():
    fruit = input("Name a fruit for fun: ")
    print(f"You named this {fruit}.")
if __name__ == "__main__":
    greet_user()
    ask_age()
    name_a_fruit()
