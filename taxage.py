'''The module contains the tax returns for your income based on whether your staus is "single" or "married based on your age gap."'''
def single_taxes_age(status, income, age_gap):
  '''This function returns taxes for a single status.

Args:
    status: The relationship status of the person which can be married or single.

    income: The amount of money that the user makes in a year.

    age_gap: The difference between your current age and age you've chosen for retirement.
Returns:
    A string representing the amount of taxes for a single status multiplied by your age gap.

Examples:
    income ==  returns
    ""

    income ==  returns
    ""
    '''
  if status == "single" or status == "Single":
    if 0 <= income <= 9875:
      return str(round(income * 0.1 * age_gap, 2))
    elif 9876 <= income <= 40125:
      return str(round(income * 0.12 + 987.50 * age_gap, 2))
    elif 40126 <= income <= 85525:
      return str(round(income * 0.22 + 4617.50 * age_gap, 2))
    elif 85526 <= income <= 163300:
      return str(round(income * 0.24 + 14605.50 * age_gap, 2))
    elif 163301 <= income <= 207350:
      return str(round(income * 0.32 + 33271.50 * age_gap, 2))
    elif 207351 <= income <= 518400:
      return str(round(income * 0.35 + 47367.50 * age_gap, 2))
    elif income >= 518401:
      return str(round(income * 0.37 + 156235 * age_gap, 2))

def married_taxes_age(status, income, age_gap):
  '''This function returns taxes for a married.

Args:
    status: The relationship status of the person which can be married or single.

    income: The amount of money that the user makes in a year.

    age_gap: The difference between your current age and age you've chosen for retirement.
Returns:
    A string representing the amount amount of taxes for a married status multiplied by your age gap.

Examples:
    income ==  returns
    ""

    income ==  returns
    ""
    '''
  if status == "married" or status == "Married":
    if 0 <= income <= 19750:
      return str(round(income * 0.1 * age_gap, 2))
    elif 19751 <= income <= 80250:
      return str(round(income * 0.12 + 1975 * age_gap, 2))
    elif 80251 <= income <= 171050:
      return str(round(income * 0.22 + 9235 * age_gap, 2))
    elif 171051 <= income <= 326600:
      return str(round(income * 0.24 + 29211 * age_gap, 2))
    elif 326601 <= income <= 414700:
      return str(round(income * 0.32 + 66543 * age_gap, 2))
    elif 414701 <= income <= 622050:
      return str(round(income * 0.35 + 94735 * age_gap, 2))
    elif income >= 622051:
      return str(round(income * 0.37 + 167307.50 * age_gap, 2))