# This script calculates yearly compound interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# compound interest = p * (1 + r/100)^t


def compound_interest(principle, time, rate):
    return principle* (pow((1 + rate / 100), time))


if __name__ == "__main__":
    principle = float(input("Enter the principal amount: "))
    time = float(input("Enter the time period: "))
    rate = float(input("Enter the rate of interest: "))

    print("The compound interest is {:.2f}".format(compound_interest(principle, time, rate)))
