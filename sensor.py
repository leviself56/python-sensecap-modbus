#!/usr/bin/env python3
import time
import sys
from modbus import *

def main():
    while True:
        if instrument:
            try:
                co2_raw     = instrument.read_register(0, 0)
                temp_raw    = instrument.read_register(1, 0)
                hum_raw     = instrument.read_register(2, 0)
            
                temp_dec = int(temp_raw / 100)
                temp_far = (temp_dec * (9/5) + 32)
                hum_dec = int(hum_raw / 100)

                LEVEL_CO2   = co2_raw
                LEVEL_TEMP  = temp_far
                LEVEL_HUM   = hum_dec

                print("Data Available!")
                print("CO2:",           LEVEL_CO2,  "PPM")
                print("Temperature:",   LEVEL_TEMP, "degrees F")
                print("Humidity::",     LEVEL_HUM,  "%%rH")
                print("")
                print("Waiting for new data...")
                print("")
                
                exception_occurred = False

            except Exception as e:
                print('Error reading insrument data: '+str(e))
                exception_occurred = True

            finally:
                if not exception_occurred:
                    time.sleep(60)
                else:
                    time.sleep(2)

if __name__ == "__main__":
    main()
