# What is this?

These are system services to enhance the compatibility of the Logitech Trackball Marble and Logitech MX Anywhere 2S with Linux. It contains scripts that start during system boot and map the device inputs into commands, like Back, Forward, Scrolling, Alt+Tab, and so on.

# Usage

## Logitech Trackball Marble

![Buttons](images/keys_marble.png)

Normal Mode

- A : Left Click
- B : Go to Declaration / Open New (Ctrl + Left Click)
- C : Right Click
- D : Middle Click
- E : Move Cursor

Holding B

- B + A : Show All Windows (Super)
- B + C : Back
- B + D : Forward
- B + E : Vertical and Horizontal Scrolling

Holding C

- C + A : New Tab (Ctrl + T)
- C + B : Reopen Tab (Ctrl + Shift + T)
- C + D : Search Selection (+Alt RightClick S -Alt)
- C + E : Change Volume (Vertical) or Undo / Redo (Horizontal)

Holding D

- D + A : Close Tab (Ctrl + W)
- D + B : Close Window (Alt + F4)
- D + C : Close Terminal (Ctrl + D)
- D + E : Switch Tabs (Vertical) or Switch Windows (Horizontal)

## Logitech MX Anywhere 2S

![Buttons](images/keys_mx2s.png)

Normal Mode

- A : Left Click
- B : Middle Click
- C : Right Click
- D : Horizontal Scroll
- E : Vertical Scroll
- F : Horizontal Scroll
- H : Back
- G : Forward
- G + H : Show All Windows

Browser Mode

- H + A : Go to Declaration (Ctrl + Click)
- H + B : Close Tab
- H + C : Reopen Tab (Ctrl + Shift + T)
- H + D : Zoom In
- H + E : Switch Tabs
- H + F : Zoom Out

System mode

- G + A : Ctrl + Z
- G + B : Close Window
- G + C : Ctrl + Shift + Z
- G + E : Switch Window

Multimedia Mode

- G + H + A : Play / Pause
- G + H + B : Stop
- G + H + C : Mute / Unmute
- G + H + D : Next Track
- G + H + E : Volume Up / Down
- G + H + F : Previous Track

# Dependencies

This daemon requires python3, pip and evdev. It has only been tested in Ubuntu 20.04 LTS, you can install its dependencies with the following commands.

```shell
sudo apt update
sudo apt install -yq libpython3-dev
sudo pip3 install evdev
```

# Install

```shell
# Install the services and python sources for all devices
sudo ./install.sh

# Start the service you want
sudo service marble-svc start # For Logitech Trackball Marble
sudo service mx2s-svc start   # For Logitech MX Anywhere 2S

# Activate autostart during system boot
sudo systemctl enable marble-svc # For Logitech Trackball Marble
sudo systemctl enable mx2s-svc   # For Logitech MX Anywhere 2S
```

# Uninstall

```shell
# Stop services, uninstall them, and remove all files
sudo ./uninstall.sh
```
