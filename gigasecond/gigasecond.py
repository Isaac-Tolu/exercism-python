from datetime import datetime

def add(moment):
    
    stamp = moment.timestamp() + 1000000000

    return datetime.fromtimestamp(stamp)

print(add(datetime(2011, 4, 25, 0, 0)))