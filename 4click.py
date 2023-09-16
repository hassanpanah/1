import pynput

#def on_click(x, y, button, pressed):
if button == mouse.Button.middle and pressed:
        global count
        count += 1
        if count == 4:
            print('yes')
            count = 0
else:
        count = 0

count = 0
#with mouse.Listener(on_click=on_click) as listener:
   # listener.join()