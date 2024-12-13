#!/usr/bin/env python3
import minimalmodbus

# SENSECAP - CO2, TEMPERATURE, HUMIDITY SENSOR
# DATASHEET: https://files.seeedstudio.com/products/SenseCAP/101991029_CO2_Sensor/CO2_Sensor_Datasheet(S-CO2-03).pdf
#
# RS485+    (YELLOW WIRE)
# RS485-    (GREEN WIRE)
# VCC+      (RED WIRE) / 5~24V
# VCC-      (BLACK WIRE)
#
# DEFAULT COMM: 9600bps, 1 start bit, 8 data bits, no parity, 1 stop bit
#
# DEFAULT SLAVE ADDRESS: 45
#
# REGISTER:
# CO2           -   0x0000      -   DEC
# TEMPERATURE   -   0x0001      -   DEC / 100 = CELSIUS
# RELATIVE HUM  -   0x0002      -   DEC / 100 = RH%
#
#   === === === === === === === === === === === ===
#
# WAVESHARE - USB TO 4CH RS485
# DATASHEET: https://www.waveshare.com/wiki/USB_TO_4CH_RS485
#
# :-$ ls /dev/ttyACM*
# /dev/ttyACM0  /dev/ttyACM1  /dev/ttyACM2  /dev/ttyACM3 

SERIAL_ADDRESS  = "/dev/ttyACM3"
SLAVE_ADDRESS   = 45
BAUD_RATE       = 9600
BYTE_SIZE       = 8
STOP_BITS       = 1
TIMEOUT         = 0.05

try:
    instrument = minimalmodbus.Instrument(SERIAL_ADDRESS, SLAVE_ADDRESS)
    instrument.serial.port
    instrument.serial.baudrate = BAUD_RATE
    instrument.serial.bytesize = BYTE_SIZE
    instrument.serial.stopbits = STOP_BITS
    instrument.serial.timeout = TIMEOUT
except Exception as e:
    print('Caught exception: ' + str(e))


# TESTING INFOMATION
co2_raw     = instrument.read_register(0, 0)
temp_raw    = instrument.read_register(1, 0)
hum_raw     = instrument.read_register(2, 0)

temp_dec = int(temp_raw / 100)
temp_far = (temp_dec * (9/5) + 32)
hum_dec = int(hum_raw / 100)

LEVEL_CO2   = co2_raw
LEVEL_TEMP  = temp_far
LEVEL_HUM   = hum_dec

print('CO2 Level: '+ str(LEVEL_CO2))
print('Temperature: '+str(LEVEL_TEMP)+' F')
print('Relative Humidity: '+str(LEVEL_HUM)+'%')
