# calculate simple and compund interest
# Simple Interest = Principle × Rate × Time = PTR/100

# defining simple interest func.  logic
def simple_interest():
        print("******* SIMPLE INTEREST *******")
        principal_amt = int(input("Enter Borrowed Amount: RS."))
        rate = int(input("Enter Interest Rate: "))
        time = int(input("Enter Interest For Years: "))
        simple_interest = (principal_amt*rate*time) / 100 #simple interest coumpution
        print(f"*******SIMPLE INTEREST FOR {time}  YEARS IS Rs.{simple_interest}") #displaying computed simple interest
        
# defining coumpound interest func. logic
def coumpound_interest():
     # compound_interest = principal * ( (1+rate/100)**time - 1)
     principal_amt = int(input("Enter Borrowed Amount: RS."))
     rate = int(input("Enter Interest Rate: "))
     time = int(input("Enter Interest For Years: "))
     coumpound_interest = principal_amt*((1+rate/100)**time)-1
     print(f"************COMPOUND INTEREST FOR {time} YEARS IS Rs.{coumpound_interest - principal_amt}")
      

# *********** MENU DRAWN ***********
while(1):
  print("*******************MENU*************************")
  print("Press 1: simple interest")
 
  print("press 2: compound interest")
  
  print("press 0: EXIT")
  choice = int(input("Enter a choice:- "))
  print("********************************************")
  
  if (choice == 1):
    simple_interest()
  elif (choice == 2):
    coumpound_interest()
  elif(choice == 0):
   exit(0)
  else:
    print("OOPS! Wrong Choice")