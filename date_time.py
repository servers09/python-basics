import datetime

def display_date(x):
    print(x)
    
def display_time(x):
    print(x)
    
def display_date_time(x):
    print(x)
    
def display_year(x):
    print(x.strftime("%Y"))
    
def display_month(x):
    print(x.strftime("%B"))
    
def display_day(x):
    print(x.strftime("%A"))
    
def display_24time(x):
    print(x.strftime("%H"))
    
def display_12time(x):
    print(x.strftime("%l"))
    
def day_of_the_year(x):
    print(x.strftime("%j"))
    
def week_number(x):
    print(x.strftime("%U"))
    
display_date(datetime.date(2019, 1, 18))
display_time(datetime.time(12,44))
display_date_time(datetime.datetime.now())
display_year(datetime.datetime(2019, 1, 18))
display_month(datetime.datetime(2019,1, 18))
display_day(datetime.datetime(2019,1, 18))
display_24time(datetime.datetime.now())
display_12time(datetime.datetime.now())
day_of_the_year(datetime.datetime.now())
week_number(datetime.datetime.now())
