# wzór na bmi BMI = masa / wzrost2

waga = float(input("podaj wagę (kg):"))
wzrost_cm = float(input("podaj wzrost (cm):"))
wzrost = wzrost_cm / 100.0
bmi = round((waga / wzrost**2), 2)

print(f"Twoje BMI przy wadze {waga} i wzroście {wzrost} wynosi {bmi}")