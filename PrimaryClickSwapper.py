import ctypes
def swap_primary_mouse_button():
    ctypes.windll.user32.SwapMouseButton(True)

def restore_primary_mouse_button():
    ctypes.windll.user32.SwapMouseButton(False)
    
SM_SWAPBUTTON = 23
def is_primary_mouse_button_swapped():
    return ctypes.windll.user32.GetSystemMetrics(SM_SWAPBUTTON)

if is_primary_mouse_button_swapped():
    print('Now Your Mouse Button is in Default Mode')
    restore_primary_mouse_button()
                
else:
    print('Now Your Mouse Button is in Swapped Mode')
    swap_primary_mouse_button()