'''The module executes the program. '''
from taxes import single_taxes, married_taxes
from calulations import charity, discret, savings, invest
from calage import charity_age, discret_age, savings_age, invest_age, remain_age
from taxage import single_taxes_age, married_taxes_age
def main():
  print("Hello, and welcome to Your New and Improved Life Plan!" + " " + "What is your name?")

  name = input("\n")

  print("\nWelcome" + " " + name + "!" + " " + "This Life Plan uses your income to give you an idea of how your income will affect your life for a year. It will give an idea of how your money can be distributed in catergories such as taxes, taxes after income, discretionary income, savings, charity, and investment. So... let's begin.")

  print("\nWhat is your status? Are you single or married?")

  status_options_one = ["single", "Single"]

  status_options_two = ["married", "Married"]

  status = input("\n")

  if status in status_options_one:
    print("\nThere's nothing wrong with being single! More money for you!")
  elif status in status_options_two:
    print("\nCongratulations! Let's see what life will be like with your spouse. Also, you will be filing your taxes jointly.")

  print("\nWhat is your profession?")

  profession = input("\n")

  print("\nAh a" + " " + profession + "" + "!" + " " + "What an interesting profession! What is your income?")

  income = float(input("\n$"))

  if status in status_options_one:
    print("\nTaxes:" + " " + "$" + single_taxes(status, income))
  elif status in status_options_two:
    print("\nTaxes:" + " " + "$" + married_taxes(status, income))

  print("\nIn order for you to gain experience with your Your New and Improved Life Plan, I will require you to track down the different quantities of money exactly. One day we may part ways, and you may not be able to ask for my assistance. Just the thought alone makes me sad, but we must do this.")

  print("\nWhat's your taxes?")

  self_tax = float(input("$"))

  remaining_income = income - self_tax

  print("\nSince you have given me your taxes, we can now calculate your remaining income. Your remaining income is the amount of money that you will have left after taxes have been taken out of your income.")

  print("\nHere's your remaining income after taxes:")

  print("\n$" + str(remaining_income))

  print("\nBecause you now know what your remaining income will be, let's calulate the amount of money that will be distributed to your discretionary income and charity.")

  print("\nHere's the amount of money that will dedicated to your discretionary income. It will always be 50 percent of your income. Some believe it's always important to pay yourself first.")
  
  print("\nDiscretionary income:" + " " + "$" + discret(remaining_income))

  print("\nHere's your amount of money dedicatd to charity. The amount of your income or percentage dedicated to charity will vary based on your income.")

  print("\nCharity:" + " " + "$" + charity(remaining_income))

  print("\nLook at you! You're gaining some financial knowledge! Now let's learn about your savings. For You New and Improved Life Plan, I will give you two options. You can either dedicate 20% of your remaining income to a regular savings account with interest or you can dedicate your money into the stock market with some average returns. So... what will it be? I must receive an answer!!!")

  print("\nWould you like to use a savings account or invest money in the stock market? Please choose an option.")

  print("\nOption 1. Savings Account" + " " + "Option 2. Invest Money")

  save_money = input("\n")

  option_one = ["1", "One", "one", "Option 1", "option 1", "Savings Account","savings account", "Savings account", "savings", "Savings"]

  option_two = ["2", "Two", "two", "Option 2", "option 2", "Invest Money", "Invest money", "invest money", "invest", "Invest"]

  if save_money in option_one:
    print("\nSince you chose to save money, let's learn a bit about saving money. Saving money will involve you dedicating 20 percent of your remaining income to an area for money, so that you will have an extra amount of money to use. You could even put some of your savings into a emergency fund which is an area to have money in case of an emergency. Let's see how much money you can put into your savings account.")
    print("\nSavings:" + " " + "$" + savings(remaining_income))
  elif save_money in option_two:
    print("\nLet's learn a little bit about the stock market! Investing in the stock market involves you putting money towards a stock that belongs to a company. Doing so will allow you to get back money in portions that you dedicate within your own choice. Let's say you invest in a company with a return of 10 percent going back to you. Let's see how much money you'll receive.")
    print("\nInvestment Return:" + " " + "$" + invest(remaining_income))

  print("\nYa know" + " " + name + " " + "you sure have learned a lot about yourself! Did you enjoy your time with me? Please say yes! I know you're going to say yes" + " " + name + " " + "!")

  print("\nSo...yes or no?")

  survey = input("\n")

  survey_option_one = ["Yes", "yes"]

  if survey in survey_option_one:
    print("\nYayyyyy!!! I knew you would! It's been a great experience" + " " + name + "." + " " + "Now we must part ways. If you like to at any time, feel free to come back for more financial adivce.")
  else:
    print("\nAwwwww man! I thought we were friends. However, It's been a great experience" + " " + name + "." + " " + "Now we must part ways. If you like to at any time, feel free to come back for more financial adivce.")

  print("\nHere's a reminder of your results below:")

  print("\nIncome:" + " " + "$" + str(income))

  if status in status_options_one:
    print("\nTaxes:" + " " + "$" + single_taxes(status, income))
  elif status in status_options_two:
    print("\nTaxes:" + " " + "$" + married_taxes(status, income))

  print("\nIncome after taxes:" + " " + "$" + str(remaining_income))

  print("\nDiscretionary income:" + " " + "$" + discret(remaining_income))

  print("\nCharity:" + " " + "$" + charity(remaining_income))

  if save_money in option_one:
    print("\nSavings:" + " " + "$" + savings(remaining_income))
  elif save_money in option_two:
    print("\nInvestment Return:" + " " + "$" + invest(remaining_income))

  print("\nThis was just a glimpse of your life. Simply a year! Now let's get to know more about you, and how the rest of your life can turn out.")

  age = int(input("\nHow old are you?\n"))

  print("\nWow!" + " " + "you're" + " " + str(age) + " " + "years old!")

  print("\nRetirement can mean many things, but in simple terms...retiring is like deciding to take a very very very long break from work. It's especially taking a break from your main profession. After retirement, you can actually still work or you can simply live off of your savings, investments, or reamining income for the rest of your life. ")

  retire_age = int(input("\nNow... what age do you want to retire?\n"))

  print("\nHmmmm... I see..." + " " + str(retire_age) + " " + "is a good age to retire!")

  age_gap = retire_age - age

  print("Because your age is" + " " + str(age) + " " + "and your retirement age is" + " " + str(retire_age) + ", this means your age gap is" + " " + str(age_gap) + " " + "years.")

  print("\nNow we are going to take the age gap which is" + " " + str(age_gap) + "." + " " + "Then we will use the age gap to calulate how all of current money results will change based on the age gap. We will now multiply the age gap by all of your money calculations.")

  print("\nHere are your retirement results below:")

  print("\nIncome:" + " " + "$" + str(income))

  if status in status_options_one:
    print("\nTotal Taxes:" + " " + "$" + single_taxes_age(status, income)
  elif status in status_options_two:
    print("\nTotal Taxes:" + " " + "$" + married_taxes_age(status, income) 
 
  print("\nTotal Income after taxes:" + " " + "$" + remain_age(remaining_income, age_gap))

  print("\nTotal Discretionary income:" + " " + "$" + discret_age(remaining_income, age_gap))

  print("\nTotal Charity:" + " " + "$" + charity_age(remaining_income, age_gap))

  if save_money in option_one:
    print("\nTotal Savings:" + " " + "$" + savings_age(remaining_income, age_gap))
  elif save_money in option_two:
    print("\nTotal Investment Return:" + " " + "$" + invest_age(remaining_income, age_gap))
  
  print("\nGoodbye! Come back and see me!")

  # print("\nIncome after taxes, charity, and Savings or Investment:" + " " + "$" + all_factors(save_money, option_one, remaining_income, charity, savings, invest, discret))
 
  # if survey in survey_option_one:
  #   print("\nYayyyyy!!! I knew you would! Now...let's play a game! I love games!")
  # else:
  #   print("\nAwwwww man! I thought we were friends. Now... hehehe... let's a play a game. I will have my revenge and relish in victory.")

  # print("\nWhen I was young, other programs and I would compete with each other to see who would have the highest success rate. However, I've never had to compete against the very user in my prescence. We will test your financial understanding, and see who has the highest score!")

  # print("\nHere are the rules. For every question you get correct, you will get one point. However, there's a different result if you get a question wrong. If you get a question wrong, I get a point!")

  # print("\nLet's see many years it will take for you to become a millionare!")

  # print("\nNow that we know how long it will take for you to become a millionare, let's learn about your retirement and your total progress throughout life.")

if __name__ == "__main__":
    main()