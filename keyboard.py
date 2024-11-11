from convert import str_to_float


def gather_numbers() -> list[float]:
    new_list = []
    response = ""
    while response != "done":
        response = input("Provide a number or enter 'done' to quit: ")
        if str_to_float(response) == None:
            print("Not a valid number")
        else:
            new_list.append(str_to_float(response))
    return new_list

if __name__ == '__main__':
    print(gather_numbers())