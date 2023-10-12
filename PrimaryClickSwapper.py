from pynput import mouse
import time
import ctypes
def swap_primary_mouse_button():
    ctypes.windll.user32.SwapMouseButton(True)

def restore_primary_mouse_button():
    ctypes.windll.user32.SwapMouseButton(False)
    
SM_SWAPBUTTON = 23
def is_primary_mouse_button_swapped():
    return ctypes.windll.user32.GetSystemMetrics(SM_SWAPBUTTON)
    


middle_clicks = 0
last_click_time = 0
click_interval = 0.5  # Time interval between clicks (in seconds)

def on_click(x, y, button, pressed):
    global middle_clicks, last_click_time
    if not pressed and button == mouse.Button.middle:
        current_time = time.time()
        if current_time - last_click_time < click_interval:
            middle_clicks += 1
        else:
            middle_clicks = 1
        last_click_time = current_time

        if middle_clicks == 3:
            print('Three Middle Clicks Detected ...')
            
            
            if is_primary_mouse_button_swapped():
                print('Now Your Mouse Button is in Default Mode')
                restore_primary_mouse_button()
                
            else:
                print('Now Your Mouse Button is in Swapped Mode')
                swap_primary_mouse_button()
            middle_clicks = 0

with mouse.Listener(on_click=on_click) as listener:
    listener.join()