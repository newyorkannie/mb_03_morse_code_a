input.onButtonPressed(Button.A, function () {
    radio.sendString("YES")
    basic.showIcon(IconNames.Yes)
    basic.pause(700)
    basic.clearScreen()
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "YES") {
        basic.showIcon(IconNames.Yes)
        basic.pause(500)
        basic.clearScreen()
    } else if (receivedString == "NO") {
        basic.showIcon(IconNames.No)
        basic.pause(500)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("NO")
    basic.showIcon(IconNames.No)
    basic.pause(700)
    basic.clearScreen()
})
radio.setGroup(88)
