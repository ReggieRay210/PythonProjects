"""
date_format program:
Prompt for the user input and ensure that the date is a valid date.
If the date given is in the correct format,
it will return the date in the format 'YYYY-MM-DD'.
If not, it will reprompt for the date.
"""
def main():
    format("Date: ")

def format(prompt):
    month_list = ["January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"]

    while True:
        try:
            date = input(prompt)
        except EOFError:
            print()
            break
        else:
            # 9/8/2023
            if "/" in date:
                month, day, year = date.replace("/",' ').split()
                if month.isalpha():
                    continue

            # February 4, 2023
            elif ',' in date:
                month, day, year = date.replace(",", ' ').split()
                if month.isdigit():
                    continue
                if month in month_list:
                    month = month_list.index(month)+1
            else:
                continue

            if int(month) > 12:
                continue
            elif int(day) > 31:
                continue
            elif len(year) < 4:
                continue
            else:
                print(f'{int(year)}-{int(month):02d}-{int(day):02d}')
                break
main()
