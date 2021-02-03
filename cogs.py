from monitorcontrol import get_monitors


def switch():
    for monitor in get_monitors():
        with monitor:
            if monitor.get_luminance() >= 50:
                monitor.set_luminance(0)
            else:
                monitor.set_luminance(100)
    
def set(brightness):
    for monitor in get_monitors():
        with monitor:
            monitor.set_luminance(brightness)


