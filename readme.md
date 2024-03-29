# CSI2-SPY-22

[![Upload to - AISLER](https://img.shields.io/badge/Upload_to_-AISLER-ff8000)](https://aisler.net/p/new?url=https://raw.githubusercontent.com/MisterHW/CSI2-SPY-22/master/CSI2-SPY-22-1A/CSI2-SPY-22-1A.kicad_pcb&ref=github)

> [!WARNING]  
> Rev.A layout and footprints have not been proven through prototyping yet. Replicate this design based on your own assessment. Follow the updates of this repository to be notified when more results have been added.

## CSI2-SPY-22-1A 

This board fundamentally has two variants integrated into a single PCB. It can be fully populated, or one one side can be left unpopulated. Only one side may be used at a time, since the six broken-out signals are shared, but this allows easy testing under similar conditions with and without the re-timer IC.

- Front side: passive FPC extender with I2C tapping
- Back side. active FPC extender based on the DPHY440 re-timer IC, with I2C tapping

![](CSI2-SPY-22-1A/output/RevA_3D_views.png)

## Raspberry Pi Camera Debugging

Prior work on https://github.com/jergling/MIPI-Spy offers a 15-pin, 1mm pitch PFC bridge PCB with probe points for all signals. RPI CM4 IO BOARD features one, Raspberry Pi 5 boards feature two 4-lane CSI2 camera ports using 22-pin, 0.5mm pitch FFC headers. 

To obtain access to the associated I2C lines and to be able to hook up a logic analyzer, a matching PCB design is provided in this repository.


## 22-Pin FPC Extender With I2C Connections

CSI2-SPY-22 is a 4-layer board that can be populated in multiple variants:
- front-ony: passive PCB with three headers J1, J2, J3.
- back-only: J3, J4, J5 plus [SN65DPHY440SS](https://www.ti.com/product/SN65DPHY440SS) MIPI® CSI-2/DSI DPHY retimer, LDO and passives. 

Re-timers can be used to zero out skew between lanes and re-transmit data with optional pre-emphasis. Please refer to  [DPHY440 datasheet](https://www.ti.com/lit/ds/symlink/sn65dphy440ss.pdf)  *8.2.2
Detailed Design Procedure* for an appropriate adaption via R1 thru R8.

	The output pins automatically compensate for uneven skew between clock and data lanes received on its 
	inputs ports. The DPHY440 output voltage swing and edge rate can be adjusted by changing the state of
	the VSADJ_CFG0 pin and ERC pin respectively.


Populate Q1 (DMG1024), R5 (2k) and R7 (2k) to enable I2C. 

![RevA_schematic](CSI2-SPY-22-1A/output/RevA_schematic.PNG)
[Rev-1A schematic (pdf version)](CSI2-SPY-22-1A/output/RevA_schematic.pdf)

## Raspberry Pi 5 Connectors

On The Raspberry Pi 5 board, the connector name labels J3 and J4 are not used as Pin 1 location indicators. 
- Note RPi 5 J3 and J4 Pin 1 locations are on the inward facing side of the ZIF FPC connectors.
- Orient CSI2-SPY-22 based on the Pin 1 and Pin 22 markings on the board.
- Use a **same-side 22-pin 0.5mm** pitch flex print cable to connect the CSI2-SPY-22 board HOST side to RPi 5 CAM/DISP headers.
- Erroenous connection (with an opposite-side flex print cable) will either lead to a disconnected state or the RPi 5 3.3V power rail will be shorted to GND.

Raspberry Pi 5 camera connectors:

![](CSI2-SPY-22-1A/setup/Pi5_J3_J4_orientations.jpg)

## iBOM

via htmlpreview.github.io: [2024-03-24_bom/ibom.html](http://htmlpreview.github.io/?https://github.com/MisterHW/CSI2-SPY-22/blob/master/CSI2-SPY-22-1A/output/2024-03-24_bom/ibom.html) 

## License

KiCad project: copyright Helge Wurst 2024.

This source describes Open Hardware and is licensed under the CERN-OHL-S v2.

You may redistribute and modify this source and make products using it under the terms of the CERN-OHL-S v2 (https://ohwr.org/cern_ohl_s_v2.txt).

This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-S v2 for applicable conditions.

Source location: https://github.com/MisterHW/CSI2-SPY-22

As per CERN-OHL-S v2 section 4, should You produce hardware based on this source, You must where practicable maintain the Source Location visible on the external case of the Gizmo or other products you make using this source.

## Changes

- 2024-03 Rev. 1A release with part numbers and consolidated BOM
- 2024-02 Rev. 1A pre-release and initial documentation.
