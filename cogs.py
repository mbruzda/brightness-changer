from monitorcontrol import get_monitors

def switch():
    if get_brightness() >= 50:
        set_brightness(0)
    else:
        set_brightness(100)
    
def set_brightness(brightness):
    for monitor in get_monitors():
        with monitor:
            monitor.set_luminance(brightness)

def get_brightness():
    with get_monitors()[0] as monitor:
        return monitor.get_luminance()
