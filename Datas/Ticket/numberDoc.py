import pickle

FILENAME = 'Datas/Ticket/number.pkl'  

def save_number(number, filename=FILENAME):
    with open(filename, 'wb') as file:
        pickle.dump(number, file)


def load_number(filename=FILENAME):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, pickle.UnpicklingError):
        return None

def update_number(new_value, filename=FILENAME):
    current_number = load_number(filename)  
    save_number(new_value, filename)  
    print(f"Updated number: {new_value}")

