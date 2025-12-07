from datetime import datetime
from datetime import timedelta
from calendar import day_name

from openpyxl import Workbook

from cell import Cell

def sheet(classes: list, start_date: str, end_date: str, file_location: str) -> None:
    """
    Generates the hour sheet file and saves it to a given file location.

    :param list classes: List with the names of the classes the file should be generated with.
    :param str start_date: String representation of thed ate the sheet should start at. Using '-' as a seperator.
    :param str end_date: String reperesentation of the date the sheet should end at. Using '-' as a seperator.
    :param str file_location: Location the file should be stored at.
    """

    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")

    if end_date < start_date:
        raise ValueError("Start date is later than end date.")
    
    days = (end_date - start_date).days + 1

    wb = Workbook()
    ws = wb.active
    ws.title = "Hoursheet"

    add_header(ws)
    add_dates(ws, start_date, days)

    wb.save(file_location, )


def add_header(sheet, row_offset: int = 2, col_offset: int = 3, sessions: int = 6):
    """
    Adds the header to the sheet.

    :param sheet: Openpyxl sheet to which the header should be added.
    :param int row_offset: Row where the header should start relative to the top left of the spreadsheet.
    :param int col_offset: Column where the header should start relative to the top left of the spreadsheet.
    :param int sessions: Amount of sessions blocks should be generated.
    """

    cell = Cell(Cell.get_column(col_offset) + str(row_offset))

    for _ in range(sessions):
        sheet[str(cell)] = "Start"
        cell.right()
        sheet[str(cell)] = "Stop"
        cell.right()
        sheet[str(cell)] = "Course"
        cell.right()

    sheet[str(cell)] = "Class hours"
    cell.right()
    sheet[str(cell)] = "Day total"
    cell.right()
    sheet[str(cell)] = "Week total"
    cell.right()
    sheet[str(cell)] = "Month total"
    cell.right()
    


def add_dates(sheet, start_date: datetime, days: int, row_offset: int = 3, col_offset: int = 1):
    """
    Adds the days of the weeks and the dates to the hoursheet.

    :param sheet: Openpyxl sheet to which the dates should be added.
    :param datetime start_day: Python datetime object of the first day to be added.
    :param int row_offset: Row where the dates should start relative to the top left of the spreadsheet.
    :param int col_offset: Column where the dates should start relative to the top left of the spreadsheet.
    :param int days: Number of days that should be added.
    """

    cell = Cell(Cell.get_column(col_offset) + str(row_offset))
    day = start_date

    for _ in range(days):
        sheet[str(cell)] = day_name[day.weekday()]
        cell.right()
        sheet[str(cell)] = day.strftime("%d/%m/%Y")
        cell.left()
        cell.down()
        day += timedelta(days=1)
    


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

def test_sheet():
    sheet(["Computer architecture", "Operating systems", "Computer networks"], "1-1-2000", "11-1-2000", "test.xlsx")

if __name__ == "__main__":
    # test_format_date()
    test_sheet()