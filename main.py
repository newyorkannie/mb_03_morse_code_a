def on_button_pressed_a():
    radio.send_string("YES")
    basic.show_icon(IconNames.YES)
    basic.pause(700)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    if receivedString == "YES":
        basic.show_icon(IconNames.YES)
        basic.pause(500)
        basic.clear_screen()
    elif receivedString == "NO":
        basic.show_icon(IconNames.NO)
        basic.pause(500)
        basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("NO")
    basic.show_icon(IconNames.NO)
    basic.pause(700)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(88)