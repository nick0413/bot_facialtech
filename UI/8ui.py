from datetime import datetime
now=datetime.now()
date_time = now.strftime("%m/%d/%Y")
print("date and time:",date_time)	

datetime_str = '08/08/2200'

datetime_object = datetime.strptime(datetime_str, "%d/%m/%Y").date()

# print(type(datetime_object))
print(datetime_object)  # printed in default format