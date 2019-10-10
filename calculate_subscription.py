from datetime import date 
 	
def calculate_subscription(expiry_date, month_to_buy, monthly_cost, annual_cost):
    
    day,month,year=map(int,expiry_date.split('/'))
    month_org = month
    
    per_day_cost = monthly_cost/30
    
    spcl = annual_cost/365
    
    if month_to_buy < 12:
        if day >= 15:
           day_ans = 15
           
        else:
            day_ans = 1
            
        
        month_ans = ( month + month_to_buy ) % 13 
        if month_ans == 0:
            month_ans = 1
        year_ans = year
        for x in range(month_to_buy):
            month = ( month + x ) % 13
            if month == 0:
                month = 1
            if month == 1:
                year_ans = year_ans + 1
        
    
    elif month_to_buy == 12:
        year_ans = year + 1
        if day >= 15:
           day_ans = 1
           month_ans = month + 1
           
        else:
            day_ans = 15
       
    date1 = date(year,month_org, day)
    date2 = date(year_ans, month_ans, day_ans)
    
    
    if month_to_buy < 12:
        total_days = (date2-date1).days - 2
        total_cost = total_days * per_day_cost
    elif month_to_buy == 12:
        total_days = (date2-date1).days 
        total_cost = total_days * spcl
        
    list = [day_ans, month_ans, year_ans]
    print(list)
    print(total_cost)
    
    
expiry_date=input()
month_to_buy = int(input())
monthly_cost = int(input())
annual_cost = int(input())
    
calculate_subscription(expiry_date, month_to_buy, monthly_cost, annual_cost)
    

