microIoT.init_device()
basic.show_icon(IconNames.SQUARE)
microIoT.wifi_setup("ap123", "pirouette123")
basic.show_icon(IconNames.DIAMOND)

def on_forever():
    pass
basic.forever(on_forever)
