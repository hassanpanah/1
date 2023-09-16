from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle and pressed:
        global count
        count += 1
        if count == 4:
            import ctypes

            # Constants for registry access
            HKEY_CURRENT_USER = -2147483647
            KEY_ALL_ACCESS = 0xF003F

            # Function to modify registry key
            def modify_registry_key(key, value):
                # Open the registry key
                reg_key = ctypes.c_void_p()
                ctypes.windll.advapi32.RegOpenKeyExW(HKEY_CURRENT_USER, "Control Panel\\Mouse", 0, KEY_ALL_ACCESS, ctypes.byref(reg_key))

                # Set the registry value
                ctypes.windll.advapi32.RegSetValueExW(reg_key, key, 0, ctypes.c_ulong(1), ctypes.c_wchar_p(value), len(value) * 2)

                # Close the registry key
                ctypes.windll.advapi32.RegCloseKey(reg_key)

                # Change the primary mouse button to left
                modify_registry_key("SwapMouseButtons", "1")
            count = 0
    else:
        count = 0

count = 0
with mouse.Listener(on_click=on_click) as listener:
    listener.join()