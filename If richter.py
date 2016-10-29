richter = float(input("Please enter a magnitude on the Richter scale: "))
if richter >= 8.0:
    print ("Most structures fall.")
elif richter >= 7.0:
    print ("Many buildings destroyed")
elif richter >= 6.0:
    print ("Many buildings consideraby damaged, some collapse.")
elif richter >= 4.5:
    print ("Damage to poorly constucted buildings.")
else:
    print ("No destruction of buildings.")
