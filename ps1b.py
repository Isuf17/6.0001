## 6.0001 Pset 1: Part b
## Name: Mohammed Isuf Ahmed
## Time Spent: 10 minutes
## Collaborators: None

#######################################################################################
## Get user input for salary, savings_percent, total_cost and raise_percentage below ##
#######################################################################################

salary = float(input('Enter your yearly salary: '))

savings_percent = float(input('Enter the percent of your salary to save, as a decimal: '))

total_cost = float(input('Enter the cost of your dream home: '))

raise_percentage = float(input('Enter the semi-annual raise, as a decimal: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

percent_down_payment = 0.15

down_payment = total_cost*percent_down_payment

amount_saved = 0

r = 0.05

months = 0 

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ##
###############################################################################################

while amount_saved < down_payment:
    
    amount_saved += (salary/12)*savings_percent
    
    amount_saved += amount_saved*(r/12)
    
    months += 1
    
    if months % 6 == 0:
        
        salary += salary*raise_percentage

#######################################################
## Print out the number of months it would take here ##
#######################################################

print('Number of months: ', months)