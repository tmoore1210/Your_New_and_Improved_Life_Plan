# Your New and Improved Life Plan
Welcome! This Life Plan uses your income to give you an idea of how your income will affect your life for a year. It will give an idea of how your money can be distributed in catergories such as taxes, taxes after income, discretionary income, savings, charity, and investment. So... let's begin."

## Name
Simply type the name of your choice.  
```python
  print("Hello, and welcome to Your New and Improved Life Plan!" + " " + "What is your name?")

  name = input("\n")

```
## Profession
Simply type the profession of your choice. 
```python
  print("\nWhat is your profession?")

  profession = input("\n")

  print("\nAh a" + " " + profession + "" + "!" + " " + "What an interesting profession! What is your income?")
```
## Status
Type in whether your status is single or married. Here are the ways you can type status according to these lists.
```python
  print("\nWhat is your status? Are you single or married?")

  status_options_one = ["single", "Single"]

  status_options_two = ["married", "Married"]
```

## Income
Type in any income that you would like to.
 ```python
   print("\nAh a" + " " + profession + "" + "!" + " " + "What an interesting profession! What is your income?")

  income = float(input("\n$"))
  ```

## Tracking Your Taxes
Type in the exact amount of taxes the program gave you.
 ```python
  print("\nWhat's your taxes?")

  self_tax = float(input("$"))

  remaining_income = income - self_tax
    
  ```
## Remaining Income
The remaining income will be calculated by subtracting the taxes from your income.

## Discretionary Income
The remaining income will always be calculated by remaining your remaining income by 50%.

## Charity
The charity quantity of money will be calculated by multiplying the remaining income by the charity percentage based on your remaining income.

## Savings Account
The savings quantity of money will always be calculated by multiplying your remaining income by 20 percent. Below also shows a list of responses that you can choose from if you want to save money.
 ```python
  print("\nWould you like to use a savings account or invest money in the stock market? Please choose an option.")

  print("\nOption 1. Savings Account" + " " + "Option 2. Invest Money")

  save_money = input("\n")

  option_one = ["1", "One", "one", "Option 1", "option 1", "Savings Account","savings account", "Savings account", "savings"]

  option_two = ["2", "Two", "two", "Option 2", "option 2", "Invest Money", "Invest money", "invest money", "invest"]

  if save_money in option_one:
    print("\nSince you chose to save money, let's learn a bit about saving money. Saving money will involve you dedicating 20 percent of your remaining income to an area for money, so that you will have an extra amount of money to use. You could even put some of your savings into a emergency fund which is an area to have money in case of an emergency. Let's see how much money you can put into your savings account.")
    print("\nSavings:" + " " + "$" + savings(remaining_income))
  elif save_money in option_two:
    print("\nLet's learn a little bit about the stock market! Investing in the stock market involves you putting money towards a stock that belongs to a company. Doing so will allow you to get back money in portions that you dedicate within your own choice. Let's say you invest in a company with a return of 10 percent going back to you. Let's see how much money you'll receive.")
    print("\nInvestment Return:" + " " + "$" + invest(remaining_income))
  ```

## Investing
The investments quanity of money will always be calculated by multiplying the remaining income by 10 percent. Below also shows a list of responses that you can choose from if you want to invest money.
 ```python
  print("\nWould you like to use a savings account or invest money in the stock market? Please choose an option.")

  print("\nOption 1. Savings Account" + " " + "Option 2. Invest Money")

  save_money = input("\n")

  option_one = ["1", "One", "one", "Option 1", "option 1", "Savings Account","savings account", "Savings account", "savings"]

  option_two = ["2", "Two", "two", "Option 2", "option 2", "Invest Money", "Invest money", "invest money", "invest"]

  if save_money in option_one:
    print("\nSince you chose to save money, let's learn a bit about saving money. Saving money will involve you dedicating 20 percent of your remaining income to an area for money, so that you will have an extra amount of money to use. You could even put some of your savings into a emergency fund which is an area to have money in case of an emergency. Let's see how much money you can put into your savings account.")
    print("\nSavings:" + " " + "$" + savings(remaining_income))
  elif save_money in option_two:
    print("\nLet's learn a little bit about the stock market! Investing in the stock market involves you putting money towards a stock that belongs to a company. Doing so will allow you to get back money in portions that you dedicate within your own choice. Let's say you invest in a company with a return of 10 percent going back to you. Let's see how much money you'll receive.")
    print("\nInvestment Return:" + " " + "$" + invest(remaining_income))
  ```
## Age and Retirement
When asked to input an age, simply input an age of your choice. After being asked to input a retirement age, input a retirement age of your choice. Inputing these two numbers will provide an age gap which will be used to show your total results after officially retiring.

### If you would like to learn more about tax brackets, savings, and other aspects of money, then take a look at some of these websites.
1. Tax Brackets Article: https://www.nerdwallet.com/article/taxes/federal-income-tax-bracket
1. Donate Charity Article: https://districtcapitalmanagement.com/how-much-should-i-donate-to-charity/
1. Savings and 50/30/20 Rule Article: https://www.tiaa.org/public/learn/personal-finance-101/how-much-of-my-income-should-i-save-every-month