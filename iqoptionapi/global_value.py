import threading

check_websocket_if_connect = None

# Real mutex replacing the old boolean flags that provided no actual mutual exclusion
_ws_lock = threading.Lock()

SSID = None

check_websocket_if_error = False
websocket_error_reason = None

balance_id = None
