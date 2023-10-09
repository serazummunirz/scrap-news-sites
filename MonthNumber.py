def get_month_number(month):

    month_abbreviations = {
        'JAN': 1,
        'FEB': 2,
        'MAR': 3,
        'APR': 4,
        'MAY': 5,
        'JUN': 6,
        'JUL': 7,
        'AUG': 8,
        'SEP': 9,
        'OCT': 10,
        'NOV': 11,
        'DEC': 12
    }

    month_abbreviation = month

    month_number = month_abbreviations.get(month_abbreviation)

    if month_number is not None:
        # print(f"The month number for {month_abbreviation} is {month_number}.")
        return month_number
    else:
        print(f"Invalid month abbreviation: {month_abbreviation}")


get_month_number("NOV")