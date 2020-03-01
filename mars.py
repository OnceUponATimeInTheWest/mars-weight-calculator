weight = float(input('Enter your weight in pounds '))

#Gravity vars in m/s²
mars_grav = 3.711
earth_grav = 9.81

#Calculation
weight2 = (weight / float(9.81)) * 3.711
approxweight = ("%.2f" % weight2)

#Result
print('Your weight on Mars would be approximately ' +  str(approxweight) + ' lbs')




