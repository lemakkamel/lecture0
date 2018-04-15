text=str(raw_input("Enter text : "))
def count_letter(text):
    counter = 0
    index = 0
    box = 2
    length = len(text) - 1
    while index < length:
        check = text[index:index + box]
        if check[0] not in  " ,." and check[1] == " ":
            counter += 1
        elif (index == (length - 1)) and (" .,"  in check[1]) :
            counter += 1
        index += 1
    print counter



count_letter(text)
