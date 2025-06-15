print('hello'+input('enter  your name please'))
print(input('enter youe age please'))
weight=float(input('what is your weight(kg)'))
height_cm=float(input('how tall are you(cm)'))
height_m=height_cm /100
bmi=weight / (height_m**2)
print(f' your bmi is:{bmi:2f}')
if bmi <18.5:
    print('you are underweight')
    print('recommendation:eat more nutritious,hight_calorie foods like nuts ,dairy,and healthy fats')
elif 18.5<=bmi <25:
    print('you have normal weight')
    print('recommendation:maintain a blanced diet with fruits,vegetables,and proteins')
elif 25<=bmi>=30:
    print('you are obese.')
    print('recommendation: consult nutritionist,avoid fast food')
else:
    print('you are obese.')
    print('recommendation: consult nutritionist,avoid fast food')













