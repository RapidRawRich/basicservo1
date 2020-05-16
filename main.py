def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P0, 180)
    basic.pause(1000)
    pins.servo_write_pin(AnalogPin.P0, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.servo_set_pulse(AnalogPin.P0, 2500)
    basic.pause(2000)
    pins.servo_set_pulse(AnalogPin.P0, 500)
input.on_button_pressed(Button.B, on_button_pressed_b)

led.enable(False)

def on_forever():
    pass
basic.forever(on_forever)
