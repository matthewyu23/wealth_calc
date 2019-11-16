bracket_income = [9700, 39475, 84200, 160725, 204100, 510300]
bracket_percent = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

def calc_tax(pre_tax_income): 
    tax = 0
    for i in range(len(bracket_income)): 
        if pre_tax_income < bracket_income[i]: 
            return pre_tax_income * bracket_percent[i] + tax
        else: 
            tax += bracket_percent[i] * bracket_income[i]
            pre_tax_income -= bracket_income[i]
    return bracket_percent[-1] * pre_tax_income + tax

def standardize_length(s, l): 
    if not isinstance(s, str): 
        s = str(s)
    for x in range(l - len(s)): 
        s += " "
    return s

class Person: 
    def __init__(self, age, income, needs_ratio, wants_ratio, savings_ratio): 
        self.income, self.age, self.needs_ratio, self.wants_ratio, self.savings_ratio = income, age, needs_ratio, wants_ratio, savings_ratio
        self.column_width = 20
        self.savings = 0


    def predict(self, years): 
        print(standardize_length("age", self.column_width), standardize_length("income", self.column_width), standardize_length("income after tax", self.column_width), standardize_length("savings", self.column_width))
        for x in range(self.age, self.age + years + 1): 
            income_after_tax = self.income-calc_tax(self.income)
            savings_from_this_year = self.savings_ratio/100*income_after_tax
            self.savings += savings_from_this_year
            print(standardize_length(x, self.column_width), standardize_length(self.income, self.column_width), standardize_length(income_after_tax, self.column_width), standardize_length((self.savings), self.column_width))