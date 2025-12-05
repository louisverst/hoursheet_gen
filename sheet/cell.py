class Cell:
    def __init__(self, cell: str):
        """
        Initializes a Cell object by checking if the provided argument is a valid cell. 
        A valid cell consists of a variable amount of letters followed by a variable amount of digits.

        :param str cell: Cell number to be initialized on.
        """
        passed_letters = False
        self.row = ""
        self.column = ""

        for c in cell:
            if not passed_letters:
                if c.isalpha():
                    self.column += c.upper()
                elif c.isdigit():
                    if c == "0":
                        raise ValueError("Invalid Cell number")
                    else:
                        passed_letters = True
                        self.row += c
                else:
                    raise ValueError("Invalid Cell number")
            else:
                if c.isdigit():
                    self.row += c
                else:
                    raise ValueError("Invalid Cell number")
                
    def __str__(self):
        return self.column + self.row
    
    def __call__(self):
        return self.__str__()
    
    def up(self):
        if self.row != "1":
            self.row = str(int(self.row) - 1)

        return self.__str__()

    
    def right(self):
        if self.column[-1] == "Z":
            self.column = self.column[:-1] +  "A"
            self.column += "A"
        else:
            self.column = self.column[:-1] + chr(ord(self.column[-1]) + 1)     

        return self.__str__()   

    def down(self):
        self.row = str(int(self.row) + 1)
        return self.__str__()

    def left(self):
        if len(self.column) == 1 and self.column[0] == "A":
            return self.__str__()
        elif self.column[-1] == "A":
            self.column = self.column[:-2] + "Z"
        else:
            self.column = self.column[:-1] + chr(ord(self.column[-1]) - 1)

        return self.__str__()
        

def test_cell():
    print(20*"=" + " Testing class Cell " + 20*"=" + "\n")

    cell = Cell("aa4")

    print(f"Initializing cell on {cell}.")
    print(f"Moving down: {cell.down()}")
    print(f"Moving to the right: {cell.right()}")
    print(f"Moving up: {cell.up()}")
    print(f"Moving to the left: {cell.left()}")
    print("\n")

    print("Moving to the left 100 times.")
    for i in range(100):
        print(cell.left(), end="\t")
    print("\n")

    print("Moving up 100 times.")
    for i in range(100):
        print(cell.up(), end="\t")
    print("\n")

    print("Moving down 100 times.")
    for i in range(100):
        print(cell.down(), end="\t")
    print("\n")

    print("Moving to the right 100 times.")
    for i in range(100):
        print(cell.right(), end="\t")
    print("\n")

    print("Initializing illegal cells")

    try:
        cell = Cell("A4A")
    except ValueError as e:
        print(e)

    try:
        cell = Cell("a 4")
    except ValueError as e:
        print(e)

    try:
        cell = Cell("A04")
    except ValueError as e:
        print(e)

    print("\n" + 60*"=" + "\n")



if __name__ == "__main__":
    test_cell()