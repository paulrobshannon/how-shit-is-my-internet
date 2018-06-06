#!/usr/bin/env ipython

import socket
import pandas as pd
import os
import time

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

i = 0

while i < 10:
    df = pd.DataFrame({'time': pd.datetime.now(),
                   'connected': [is_connected()]})
    
    if not os.path.isfile('./data/connection_info.csv'):
        df.to_csv('./data/connection_info.csv', index=False)
    else:
        df.to_csv('./data/connection_info.csv', mode='a', header=False, index=False)
        
    time.sleep(1)
    
    i += 1

# os.remove('./data/connection_info.csv')
