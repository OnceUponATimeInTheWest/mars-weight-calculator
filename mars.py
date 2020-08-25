message = float(input('Enter your weight in pounds: '))

weight = (message / float(9.81)) * 3.711
approx = ("%.2f" % message)

print(f'Your weight on Mars would be approximately {approx} lbs')




