import time

from openpyxl import Workbook

def sheet(classes: list, start_date: str, end_date: str, file_location: str) -> None:
    """
    Generates the hour sheet file and saves it to a given file_location.

    :param list classes: List with the names of the classes the file should be generated with.
    :param str start_date: String representation of thed ate the sheet should start at. Using '-' as a seperator.
    :param str end_date: String reperesentation of the date the sheet should end at. Using '-' as a seperator.
    :param str file_location: Location the file should be stored at.
    """

    wb = Workbook()
    ws = wb.create_sheet("Hoursheet")

    start_date = time.strptime(format_date(start_date), "%d-%m-%Y")
    end_date = time.strptime(format_date(end_date), "%d-%m-%Y")

    




def format_date(date: str) -> str:
    """
    Ensures the time is formatted according to the format specifiers of the Python time library.
    Assumes the year is in the 2000 century if the year is two characters long.
    Assumes the year is between 0-9999.

    :param str date: A string representation of a date using '-' as delimiter. 
    """

    if date.count("-") != 2:
        raise ValueError("Please provide the date in a valid string format (with - as seperator)")
    
    res = ""
    for i, p in enumerate(date.split("-")):
        if i == 2:
            if len(p) == 2:
                return res + "20" + p
            else:
                return res + (4 - len(p))*"0" + p
            
        res += (2 - len(p))*"0" + p + "-"
        



def test_format_date():
    print(20*"=" + " Testing format_date() " + 20*"=" + "\n")

    dates = [
        "28-2-2025",
        "6-7-13",
        "13-8-813",
        "6-6-6",
        "25-12-2000"
    ]

    for d in dates:
        print(f"{d} becomes {format_date(d)}")

    print("\n" + 63*"=" + "\n\n")

if __name__ == "__main__":
    test_format_date()