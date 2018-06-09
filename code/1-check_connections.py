#!/usr/bin/env ipython

import socket
import pandas as pd
import os
import sys


def is_connected():
#     try:
#         socket.create_connection(("www.google.com", 80))
#         return True
#     except OSError:
#         pass
#     return False
    # test if works with even/odd minutes    
    return pd.datetime.now().minute % 2 == 0

previous_state = pd.read_csv('../data/previous_state.csv')

# first instance of the connection going down:
if not is_connected() and previous_state.state[0]: 
    current_state = pd.DataFrame({'state': [is_connected()],
                                  'time' : [pd.datetime.now()]})
    current_state.to_csv('../data/previous_state.csv', index=False)
    
# first instance of the connection going up:
elif is_connected() and not previous_state.state[0]:
    current_state = pd.DataFrame({'state': [is_connected()],
                                  'time' : [pd.datetime.now()]})
    current_state.to_csv('../data/previous_state.csv', index=False)
    
    outage_info = pd.DataFrame({'outage_start': [previous_state.time[0]],
                                'outage_end':   [current_state.time[0]]})
    
    outage_info.to_csv('../data/outage_info.csv', mode='a', header=False, index=False)
  
