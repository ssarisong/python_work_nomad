def get_yearly_revenue(monthly_revenue):
  return monthly_revenue*12
def get_yearly_expenses(monthly_expenses):
  return monthly_expenses*12
def get_tax_amount(profit):
  if profit > 100000:
    return profit*0.25
  else:
    return profit*0.15
def apply_tax_credits(tax_amount, tax_credits):
  return tax_credits*tax_amount

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01

profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
