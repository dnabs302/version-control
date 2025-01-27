import datetime

current = datetime.datetime.now()
current_date_time = current.strftime("%Y-%m-%d %H:%M:%S")

with open("version.md", "w") as f:
    f.write(current_date_time +'\n')


