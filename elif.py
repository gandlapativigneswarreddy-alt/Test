score = 95
rank = 5
if score >= 90:
    if rank == 1:
        print("top")
    else:
        print("better luck")    
    print("Grade A+")
elif score >= 75 <= 89:
    print("Grade A")
elif score >= 60 <=74:
    print("Grade B")
elif score == 100:
    print("Your great")    
else: 
    print("Grade C")            