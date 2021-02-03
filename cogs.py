from monitorcontrol import get_monitors

def switch():
    for monitor in get_monitors():
        with monitor:
            if get_brightness() >= 50:
                monitor.set_luminance(0)
            else:
                monitor.set_luminance(100)
    
def set(brightness):
    for monitor in get_monitors():
        with monitor:
            monitor.set_luminance(brightness)

def get_brightness():
    with get_monitors()[0] as monitor:
        return monitor.get_luminance()
