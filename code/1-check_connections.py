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

outage_time = None
outage_end  = None

while True:
    if not is_connected():
        outage_time = pd.datetime.now() if outage_time is None else outage_time

    else:
        if outage_time is not None:
                outage_end = pd.datetime.now()

                df = pd.DataFrame({'outage_time': [outage_time],
                                   'outage_end' : [outage_end]})

                if not os.path.isfile('../data/connection_info.csv'):
                    df.to_csv('../data/connection_info.csv', index=False)

                else:
                    df.to_csv('../data/connection_info.csv', mode='a', header=False, index=False)

                outage_time = None
                outage_end  = None
        
    time.sleep(1)
