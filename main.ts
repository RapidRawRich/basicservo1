input.onButtonPressed(Button.A, function on_button_pressed_a() {
    pins.servoWritePin(AnalogPin.P0, 180)
    basic.pause(1000)
    pins.servoWritePin(AnalogPin.P0, 0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    pins.servoSetPulse(AnalogPin.P0, 2500)
    basic.pause(2000)
    pins.servoSetPulse(AnalogPin.P0, 500)
})
led.enable(false)
basic.forever(function on_forever() {
    
})
