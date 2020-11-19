## 6.0001 Pset 1: Part c
## Name: Mohammed Isuf Ahmed
## Time Spent: 20 minutes
## Collaborators: None

#############################################
## Get user input for starting_amount below ##
#############################################

starting_amount = float(input('Enter the initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_house = 750000

down_payment = cost_of_house*0.25

high = 1

low = 0

r = 0

current_savings = 0

steps = 1

########################################################################################################
## Determine the lowest return on investment needed to get the down payment for your dream home below ##
########################################################################################################

if starting_amount >= down_payment:
    
    print('Best savings rate is 0')
    
else:

    while abs(down_payment - current_savings) > 100:
        
        r = (high+low)/2
        
        current_savings = starting_amount*(1+r/12)**36
        
        if current_savings < down_payment:
            
            steps += 1 
            
            low = r
            
        else:
            
            steps += 1
            
            high = r
        
        if abs(1-r) < 0.00000000000000000000000000000001:
            
            r = None
            
            break
    
##########################################################
## Print out the best savings rate and steps taken here ##
##########################################################

print('Best savings rate: ', r)

print('Steps in bisection search: ', steps)

