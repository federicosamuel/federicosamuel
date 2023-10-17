#STEP1
def robot():
  print("Hello there! this is your shopping evaluator.")
  print("Give me the total price of your purchase:.")
  price = input()
  print("Do you have a membrecy card?")
  membrecy = input()
#STEP2
  if price >=100:
    print("Congratulations! you have a 10% discount")
    discount = price * 0.1
    print("your discount is", discount)
    print("your total price is", price - discount) 
  if price < 100: 
    print("you have no discount")
    print("your total price is", price)
  if membrecy:yes
  print("great, you just got an extra 5% discount")
  memberdiscount = price - discount * 0.05
  print("your discount is", memberdiscount)
  print("your total price is", price - memberdiscount)
  if membrecy:no 
  print("your total price is", price)
#STEP3
robot() 
