bracket_income = [9700, 39475, 84200, 160725, 204100, 510300]
bracket_percent = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

def standardize_length(s, l): 
    if not isinstance(s, str): 
        s = str(round(s, 2))
    for _ in range(l - len(s)): 
        s += " "
    return s

class Person: 
    def __init__(self, age = 22, income = 100000, promotion = 1.08, savings_ratio = 0.2, high_intrest_savings_account_ratio = 0.5, stock_market_ratio = 0.5): 
        self.pre_tax_income = income
        self.promotion = promotion
        self.post_tax_income = self.calc_tax(self.pre_tax_income * self.promotion)
        self.age = age
        self.column_width = 20
        self.my_401k = 0
        self.promotion = promotion
        self.high_intrest_savings_account = 0
        self.stock_market = 0
        self.net_worth = 0
        self.high_intrest_savings_account_ratio = high_intrest_savings_account_ratio
        self.stock_market_ratio = stock_market_ratio
        self.savings_ratio = savings_ratio

    def calc_tax(self, pre_tax_income): 
        tax = 0
        for i in range(len(bracket_income)): 
            if pre_tax_income < bracket_income[i]: 
                return pre_tax_income * bracket_percent[i] + tax
            else: 
                tax += bracket_percent[i] * bracket_income[i]
                pre_tax_income -= bracket_income[i]
        return bracket_percent[-1] * pre_tax_income + tax

    def update(self): 
        self.age += 1
        self.pre_tax_income *= self.promotion
        self.my_401k, self.pre_tax_income = self.my_401k + 0.06 * self.pre_tax_income, self.pre_tax_income - self.pre_tax_income * 0.06
        self.post_tax_income = self.pre_tax_income - self.calc_tax(self.pre_tax_income)
        self.high_intrest_savings_account = self.high_intrest_savings_account * 1.02 + self.post_tax_income * self.savings_ratio * self.high_intrest_savings_account_ratio
        self.stock_market = self.stock_market * 1.1 + self.post_tax_income * self.savings_ratio * self.stock_market_ratio
        self.net_worth = self.my_401k + self.high_intrest_savings_account + self.stock_market
    
    def print_this_year(self):
        print(standardize_length(self.age, self.column_width), standardize_length(self.pre_tax_income, self.column_width), standardize_length(self.post_tax_income, self.column_width), standardize_length(self.stock_market, self.column_width), standardize_length(self.high_intrest_savings_account, self.column_width), standardize_length(self.my_401k, self.column_width), standardize_length(self.net_worth, self.column_width))

    def predict_and_print(self, years):
        print(standardize_length("age", self.column_width), standardize_length("income", self.column_width), standardize_length("income after tax", self.column_width), standardize_length("stocks", self.column_width), standardize_length("savings account", self.column_width), standardize_length("401k", self.column_width), standardize_length("net worth", self.column_width))
        for _ in range(self.age, self.age + years + 1): 
            self.update()
            self.print_this_year()