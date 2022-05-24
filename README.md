
<img align="right" width=175 src="https://github.com/RootCNC/Root-Pendant/blob/main/Media/R_Logo.png" />

# Root Pendant
CNC pendant for control of the *Root CNC* and any other *CNC machines*

This is a preliminary repo to gain ideas and assess the pendant implementation practically 

## Project goals.
- Be as flexible as possible
- Offer USB 2.0 Type C *Host* and *Slave* support for either controlling the CNC directly or via a PC 
- Support Wifi/Bluetooh for wireless control
- Support 6 Axis
- Support all of the standard features
-- Manual job movement
-- Spindle control
-- Feedrate control
-- Start/Stop/Hold
- Universal 
- Open source!

## Key Parts
- 5V 60mm 4 Pin 100 pulse Encoder [LINK](https://s.click.aliexpress.com/e/_9yPgMw)
- 2.8 Inch 320*240 FTF Touch screen display ILI9341 
- 16mm E-Stop button [Link](https://s.click.aliexpress.com/e/_A71fQ2)
- Raspberry Pi Zero 2 W [Link](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)

```mermaid

graph LR

A((Root Pendant)) -- Acts as keyboard - Via USB --> B(PC Host)

B --> C(PC Controller software - UGS)

C --> D{CNC Motion controller}

A -- Direct control of CNC - Via USB --> D{CNC Motion controller}

A -- Direct control of CNC - Via Telnet WiFi--> D{CNC Motion controller}

A --> E((CNCjS))

E --> A

E -- Direct control of CNC - Via USB--> D

E -- Direct control of CNC - Via Telnet WiFi--> D

``````

 

## Implemented interfaces

 

- [ ] Root Pendant as USB Slave - setup as USB keyboard for macro implementation with PC based CNC control software (USG)

- [ ]  Root Pendant as USB Host - Control of CNC controller via USB

- [ ] Root Pedant control controls CNC controller via Telnet (Current known controller: Root Controller ISO (FluidNC),  Duet 3 6HC W/SBC)

- [ ] Root Pendant running CNCjs connected via the Boiler Plate addon (CNCjs controls the CNC and Root Pendant talks directly to CNCjs (CNCjs Handles the connection to the CNC, either via Telnet or direct USB connection)

 

## Software development list

- [ ] GUI

                -  [ ] Main display

                -  [ ] Settings menu

                -  [ ] Touchscreen cal page

- [ ] IO

                - [ ] Touchscreen controller

                - [ ] Keypad controller

                - [ ] Jog wheel control

                - [ ] Mode control

                - [ ] Enable control

                - [ ] USB controller

                - [ ] Keypad LED and Power controller controller

                - [ ] USB

                                - [ ]  Type-C implementation

- [ ] Backend stuff

                - [ ] User-Save settings

                - [ ] Power up and power down states

                - [ ] 5V USB OTG control

                - [ ] Low Batter indication

                - [ ] Raspberry Pi LCD control

                - [ ] E-stop

## Initial placement and Ideas
<img width=400 src="https://github.com/RootCNC/Root-Pendant/blob/main/Media/OutlinePlan.PNG" />
FRO - Feedrate Override
SSO - Spindle Speed Override
## License

This project is licensed under the Creative Commons 4.0 license with 
Attribution-NonCommerial-ShareAlike see `LICENSE.txt` for details




