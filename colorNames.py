HEX_COLOURS = {"Beige": "#f5f5dc", "Black": "#000000", "Blue Violet": "#8a2be2", "Brown": "#a52a2a",
               "Blue": "#0000ff", "Red": "#ff0000"}

colour = str(input("Enter colour: "))
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
    else:
        print("Invalid Colour")
    colour = str(input("Enter Colour: "))