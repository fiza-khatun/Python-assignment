starting_salary=float(input("enter the annual salary:"));

semi_annual_raise=0.07
r=0.04
down_payment=0.25
total_cost=1000000
Months=36
x=100

required_down_payment=total_cost*down_payment

# bisection search bounds(0 to 10000)

small=0
large=10000
steps=0

# check if 100% is enough

current_savings=0
Monthly_salary=starting_salary

for Months in range(1,Months+1):
       current_savings+=current_savings*(r/12)
       current_savings+=(Monthly_salary/12)*r

       if Months%6==0:
           Monthly_salary+=Monthly_salary*semi_annual_raise
       if current_savings<down_payment-x:
           print("not possible in three years:")
       else:

            while True:
              steps+=1
              y=(small+large)//2
              saving_rate=y/10000
              current_savings=0
              Monthly_salary= starting_salary/12

              for Months in range(1,Months+1):
                 current_savings+=current_savings*(r/12)
                 current_savings+=(Monthly_salary/12)*r

              if Months%6==0:
                Monthly_salary+=Monthly_salary*semi_annual_raise
# within $100
              if abs(current_savings-required_down_payment)<=100:
               print("best savings rate:",r)
               print("steps in bisection search:",steps)
               break
              elif current_savings<down_payment:
                   small=y+1
              else:
                   large=y-1