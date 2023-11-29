katz_deli = []

def line(line):
    message = f"The line is currently: {' '.join([f'{i+1}. {name}' for i, name in enumerate(line)])}" if line else "The line is currently empty."
    print(message)

def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(line):
    if not line:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = line.pop(0)
        print(f"Currently serving {serving_customer}.")

def show_line(line):
    if not line:
        print("The line is currently empty.")
    else:
        print("The line is currently:")
        for index, customer in enumerate(line, start=1):
            print(f"{index}. {customer}")