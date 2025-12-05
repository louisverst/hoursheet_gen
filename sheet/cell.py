from helper.alphabet import next_letter
from helper.alphabet import prev_letter
from helper.alphabet import divmod_excel

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

    @staticmethod
    def get_column(n: int) -> str:
        """
        Converts a number to the textual column representation.

        Source of calculation method:
        https://stackoverflow.com/a/48984697
        
        :param int n: Number of column..
        :return str: Textual representation.
        """
        
        chars = []
        while n > 0:
            n, d = divmod_excel(n)
            chars.append(chr(65 + d - 1))

        return ''.join(reversed(chars))
        
    
    def up(self):
        if self.row != "1":
            self.row = str(int(self.row) - 1)

        return self.__str__()

    
    def right(self):
        if self.column == len(self.column)*"Z":
            self.column = (len(self.column)+1)*"A"

        elif self.column[-1] == "Z":
            i = len(self.column) - 2
            while self.column[i] == "Z":
                i -= 1

            self.column = self.column[:i] + next_letter(self.column[i]) + (len(self.column) - i - 1) * "A"

        else:
            self.column = self.column[:-1] + next_letter(self.column[-1])

        return self.__str__()   

    def down(self):
        self.row = str(int(self.row) + 1)
        return self.__str__()

    def left(self):
        if self.column == "A":
            return self.__str__()
        
        if self.column == len(self.column)*"A":
            self.column = (len(self.column) - 1)*"Z"

        elif self.column[-1] == "A":
            i = len(self.column) - 2
            while self.column[i] == "A":
                i -= 1
            
            self.column = self.column[:i] + prev_letter(self.column[i]) + (len(self.column) - i - 1) * "Z"

        else:
            self.column = self.column[:-1] + prev_letter(self.column[-1])

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
    