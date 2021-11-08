'''The module contains the functions for calculating your discretionary income, charity, and your savings or investments.'''
def discret(remaining_income):
  '''This function returns the discretionary income.

Args:
    remaining_income: The income left for yourself which is the income after taxes.

Returns:
    A string representing discretionary income which is the remaining income multiplied by 50 percent.

Examples:
    remaining_income == 7812.5  returns
    "3906.25"

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * 0.5, 2))

def savings(remaining_income):
  '''This function returns the savings quantity.

Args:
    remaining_income: The income left for yourself which is the income after taxes.

Returns:
    A string representing the savings amount which is your remaining income multiplied by 20 percent.

Examples:
    remaining_income == 7812.5 returns
    "1562.62"

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * 0.2, 2))

def invest(remaining_income):
  '''This function returns the investments quantity.

Args:
    remaining_income: The income left for yourself which is the income after taxes.

Returns:
    A string representing the investments amount which is your remaining income multiplied by 10 percent.

Examples:
    remaining_income == 7812.5 returns
    "781.25"

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * 0.1, 2))

def charity(remaining_income):
  '''This function returns the charity quantity.

Args:
    remaining_income: The income left for yourself which is the income after taxes.

Returns:
    A string representing the charity amount which is your remaining income multiplied on a percentage based on your remaining income.

Examples:
    remaining_income == 7812.5 returns
    "1015.62"

    remaining_income == returns
    ""
    '''
  if remaining_income <= 15000:
    return str(round(remaining_income * 0.13, 2))
  elif 15000 <= remaining_income <= 29999:
    return str(round(remaining_income * 0.08, 2))
  elif 30000 <= remaining_income <= 49999:
    return str(round(remaining_income * 0.07, 2))
  elif 50000 <= remaining_income <= 99999:
    return str(round(remaining_income * 0.05, 2))
  elif 100000 <= remaining_income <= 199999:
    return str(round(remaining_income * 0.03, 2))
  elif remaining_income >= 200000:
    return str(round(remaining_income * 0.03, 2))

# def all_factors(save_money, option_one, remaining_income, charity, savings, invest, discret):
#    if save_money in option_one:
#      return str((remaining_income) - (charity(remaining_income) + savings(remaining_income) + discret(remaining_income)))
#    else:
#      return str((remaining_income) - (charity(remaining_income) + invest(remaining_income) + discret(remaining_income)))