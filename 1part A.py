annual_salary=float(input("enter the annual salary:"));
portion_saved=float(input("enter the portion_saved salary in decimal form:"));
total_cost=float(input("enter the toatal cost of dreamhouse:"));

portion_down_payment=0.25
current_saving=0
r=0.04

down_payment=total_cost*portion_down_payment    
# 1st payment=total cost of house* portion(bhag in nepali)
monthly_salary= annual_salary/12
months=0

while current_saving<down_payment:
    current_saving+=current_saving*r/12
    current_saving+=monthly_salary*portion_saved
    months+=1
    print("Number of months:",months)