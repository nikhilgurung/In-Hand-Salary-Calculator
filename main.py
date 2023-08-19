# A program for calculating in-hand salary
class Salary:
    def __init__(self,basic_salary):
        self.basic_salary = basic_salary
        self.hra = 0.10
        self.da = 0.05
        self.pf = 0.03

    #calculating gross salary
    def gross_salary(self):
        gross_salary = self.basic_salary + (self.basic_salary * self.hra)+(self.basic_salary * self.da)+(self.basic_salary * self.pf)
        return gross_salary
    #calulating tax
    def calculate_tax(self, gross_salary):
        if 100000 < gross_salary <= 500000:
            tax = 0.10 * gross_salary
        elif 500001 < gross_salary <= 1000000:
            tax = 0.20 * gross_salary
        elif gross_salary > 1000000:
            tax = 0.30 * gross_salary
        else:
            tax = 0
        return tax
    #Calcuating deductions
    def calculate_deductions(self):
        gross_salary = self.gross_salary()
        pf_deduction = self.basic_salary * self.pf
        tax = self.calculate_tax(gross_salary)
        total_deduction = pf_deduction + tax
        return total_deduction
    # Calculating in-hand salary
    def calculate_in_hand_salary(self):
        total_deduction = self.calculate_deductions()
        gross_salary = self.gross_salary()
        in_hand_salary = self.gross_salary() - self.calculate_deductions()
        return in_hand_salary
# Main Function
def main():
    basic_salary = float(input("Enter your basic salary:\n"))
    salary_calculator = Salary(basic_salary)
    in_hand_salary = salary_calculator.calculate_in_hand_salary()

    print(f"Your in-hand salary is : {in_hand_salary:.2f}")

#calling main function
if __name__ == "__main__":
    main()
