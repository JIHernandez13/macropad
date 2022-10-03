"""
Macro pad
by Jesus H.

Want some basic functions for this 1st page
Simple 0-9 macropad for the keys
10/11 Spare keys will be for switching through modes or enabling some menu
Rotary encoder will be basic volume functionality.

Design a way to handle different mappings in future builds.
todo: add output to LCD and maybe speaker confirmation for changing modes
todo: add led outputs
"""

from adafruit_macropad import MacroPad

macropad = MacroPad()

last_position = 0

def key_0_response(macropad):
    macropad.keyboard.send(macropad.Keycode.ONE)

def key_1_response(macropad):
    macropad.keyboard.send(macropad.Keycode.TWO)

def key_2_response(macropad):
    macropad.keyboard.send(macropad.Keycode.THREE)

def key_3_response(macropad):
    macropad.keyboard.send(macropad.Keycode.FOUR)

def key_4_response(macropad):
    macropad.keyboard.send(macropad.Keycode.FIVE)

def key_5_response(macropad):
    macropad.keyboard.send(macropad.Keycode.SIX)

def key_6_response(macropad):
    macropad.keyboard.send(macropad.Keycode.SEVEN)

def key_7_response(macropad):
    macropad.keyboard.send(macropad.Keycode.EIGHT)

def key_8_response(macropad):
    macropad.keyboard.send(macropad.Keycode.NINE)

def key_9_response(macropad):
    macropad.keyboard.send(macropad.Keycode.ZERO)

def key_10_response(macropad):
    # todo: make this cycle back through different macro modes
    macropad.keyboard.send(macropad.Keycode.ONE)
    macropad.keyboard.send(macropad.Keycode.ZERO)

def key_11_response(macropad):
    # todo: make this cycle forward through different macro modes
    macropad.keyboard.send(macropad.Keycode.ONE)
    macropad.keyboard.send(macropad.Keycode.ONE)

# macropad.keyboard.press(macropad.Keycode.SHIFT, macropad.Keycode.B)
# macropad.keyboard.release_all()
# macropad.keyboard_layout.write("Hello, World!")

while True:
    key_event = macropad.keys.events.get()

    if key_event:
        if key_event.pressed:
            if key_event.key_number == 0:
                key_0_response(macropad)
            if key_event.key_number == 1:
                key_1_response(macropad)
            if key_event.key_number == 2:
                key_2_response(macropad)
            if key_event.key_number == 3:
                key_3_response(macropad)
            if key_event.key_number == 4:
                key_4_response(macropad)
            if key_event.key_number == 5:
                key_5_response(macropad)
            if key_event.key_number == 6:
                key_6_response(macropad)
            if key_event.key_number == 7:
                key_7_response(macropad)
            if key_event.key_number == 8:
                key_8_response(macropad)
            if key_event.key_number == 9:
                key_9_response(macropad)
            if key_event.key_number == 10:
                key_10_response(macropad)
            if key_event.key_number == 11:
                key_11_response(macropad)

    macropad.encoder_switch_debounced.update()

    if macropad.encoder_switch_debounced.pressed:
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.MUTE
        )

    current_position = macropad.encoder

    if macropad.encoder > last_position:
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_INCREMENT
        )
        last_position = current_position

    if macropad.encoder < last_position:
        macropad.consumer_control.send(
            macropad.ConsumerControlCode.VOLUME_DECREMENT
        )
        last_position = current_position

