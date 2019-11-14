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