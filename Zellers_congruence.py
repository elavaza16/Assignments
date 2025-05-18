class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.day = day
        self.month = month
        self.year = year


        if self.month == 1 or self.month == 2:
            self.month += 12
            self.year -= 1

        self.K = self.year % 100
        self.J = self.year // 100

    def calculate_weekday(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J


        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7


        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]



try:
    day = int(input("Enter the Day: "))
    month = int(input("Enter the Month: "))
    year = int(input("Enter the Year: "))

    calculator = DateCalculator(year, month, day)
    weekday = calculator.calculate_weekday()
    print(f"\nThe day of the week for {day}/{month}/{year} is: {weekday}")

except ValueError:
    print("Please enter valid numeric values for day, month, and year.")