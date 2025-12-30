from datetime import datetime

# Get current date and time
now = datetime.now()

# Print the raw datetime object
print("now =", now)

# Format the date and time into a specific string format (DD/MM/YY H:M:S)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
