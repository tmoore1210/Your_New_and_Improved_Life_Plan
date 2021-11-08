'''The module contains the functions for calculating your income after taxes, discretionary income, charity, and your savings or investments based on your age gap.'''
def discret_age(remaining_income, age_gap):
  '''This function returns the discretionary income based on your age gap.

Args:
    remaining_income: The income left for yourself which is the income after taxes.
    
    age_gap: The difference between your current age and age you've chosen for retirement.

Returns:
    A string representing discretionary income which is the remaining income multiplied by both 50 percent and your age gap.

Examples:
    remaining_income == 3906.25  returns
    "46875.0"

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * 0.5 * age_gap, 2))

def savings_age(remaining_income, age_gap):
  '''This function returns the savings quantity based on your age gap.

Args:
    remaining_income: The income left for yourself which is the income after taxes.
    
    age_gap: The difference between your current age and age you've chosen for retirement.

Returns:
    A string representing the savings amount which is your remaining income multiplied by both 20 percent and your age gap.

Examples:
    remaining_income == 7812.5 returns
    "1562.62"

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * 0.2 * age_gap, 2))

def invest_age(remaining_income, age_gap):
  '''This function returns the investments quantity.

Args:
    remaining_income: The income left for yourself which is the income after taxes.
    
    age_gap: The difference between your current age and age you've chosen for retirement.

Returns:
    A string representing the investments amount which is your remaining income multiplied by both 10 percent and your age gap.

Examples:
    remaining_income == 7812.5 returns
    "781.25"

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * 0.1 * age_gap, 2))

def charity_age(remaining_income, age_gap):
  '''This function returns the charity quantity.

Args:
    remaining_income: The income left for yourself which is the income after taxes.
    
    age_gap: The difference between your current age and age you've chosen for retirement.

Returns:
    A string representing the charity amount which is your remaining income multiplied on a percentage based on your remaining income and your age gap.

Examples:
    remaining_income == 7812.5 returns
    "1015.62"

    remaining_income == returns
    ""
    '''
  if remaining_income <= 15000:
    return str(round(remaining_income * 0.13 * age_gap, 2))
  elif 15000 <= remaining_income <= 29999:
    return str(round(remaining_income * 0.08 * age_gap, 2))
  elif 30000 <= remaining_income <= 49999:
    return str(round(remaining_income * 0.07 * age_gap, 2))
  elif 50000 <= remaining_income <= 99999:
    return str(round(remaining_income * 0.05 * age_gap, 2))
  elif 100000 <= remaining_income <= 199999:
    return str(round(remaining_income * 0.03 * age_gap, 2))
  elif remaining_income >= 200000:
    return str(round(remaining_income * 0.03 * age_gap, 2))

def remain_age(remaining_income, age_gap):
  '''This function returns the remaining income based on your age gap.

Args:
    remaining_income: The income left for yourself which is the income after taxes.
    
    age_gap: The difference between your current age and age you've chosen for retirement.

Returns:
    A string representing discretionary income which is the remaining income by your age gap.

Examples:
    remaining_income == returns
    ""

    remaining_income == returns
    ""
    '''
  return str(round(remaining_income * age_gap, 2))