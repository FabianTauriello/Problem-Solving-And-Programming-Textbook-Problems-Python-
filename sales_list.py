# The num_days constant holds the number of days that we will gather
# sales data for. prgram is adapted from pg 314 of textbook.
num_days = 5

def main():
    # create a list to hold the sales for each day
    sales = [0] * num_days

    # create a variable to hold an index.
    index = 0

    print('Enter the sales for each day.')

    # Get the sales of each day.
    while index < num_days:
        print('Day #', index + 1, ': ', sep='', end='')
        sales [index] = float(input())
        index += 1

    # Display the values entered.
    print('\nHere are the values you entered:')
    for value in sales:
        print(value)

# call the main function
main()
