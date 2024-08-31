from datetime import datetime


# convert datetime object to string
datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("time_board.txt", "w") as f:
    # convert datetime_str to iso format
    
    f.write(datetime_str)