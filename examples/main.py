from machine import Pin
from time import sleep
from utime import sleep_us
from hcsr04 import HCSR04

############################################################
# Subroutine Space

def display(value_list, no_of_cycles = 100):
    
    for cycle in range(no_of_cycles):
        for j in range(5):
            
            clear.off()
            sleep_us(10)	
            clear.on()
            col_9.off()
            col_10.off()

            latch.off()           # first deactivate latch pin

            for i in range(10):    # then clock out the 8 data bits
                
                if i < 8:
                    clock.off()
                    
                    if value_list[j][i] == 1:
                        serial.on()
                    else:
                        serial.off()
                    
                    clock.on()
                    
                if i == 8:
                    if(value_list[j][i] == 1):
                        col_9.on()
                    else:
                        col_9.off()
                        
                if i == 9:
                    if(value_list[j][i] == 1):
                        col_10.on()
                    else:
                        col_10.off()
                               
            latch.on()
            columns[j].off()
            sleep_us(1000)
            columns[j].on()            

            
    columns[4].on()

############################################################
# End of Subroutine Space



############################################################
# Pin Definitions

sensor1_trig  =    15
sensor1_echo  =    2
 
sensor2_trig  =    5
sensor2_echo  =    4

sensor3_trig  =    17
sensor3_echo  =    16



serial_pin    =    25	  	# SER pin
latch_pin     =    26       # RCLK pin
clock_pin     =    27	    # SRCLK pin
clear_pin     =    13	    # SRCLR pin (inverted logic)

col_9_pin     =    32        # 9th  COL
col_10_pin    =    33        # 10th COL


column_pins = [18, 19, 21, 22, 23]
columns     = [None, None, None, None, None]

############################################################
# init subroutine  #########################################

# initialize the inputs and outputs

for i in range(len(column_pins)):
    columns[i] = Pin(column_pins[i], Pin.OUT)
    columns[i].on()



serial     = Pin( serial_pin, Pin.OUT)
latch      = Pin( latch_pin, Pin.OUT)
clock      = Pin( clock_pin, Pin.OUT)
clear      = Pin( clear_pin, Pin.OUT)
col_9      = Pin( col_9_pin, Pin.OUT)
col_10     = Pin( col_10_pin, Pin.OUT)


sensor1 = HCSR04( sensor1_trig, sensor1_echo, echo_timeout_us = 1000000)
sensor2 = HCSR04( sensor2_trig, sensor2_echo, echo_timeout_us = 1000000)
sensor3 = HCSR04( sensor3_trig, sensor3_echo, echo_timeout_us = 1000000)
############################################################
# MAIN subroutine  #########################################

# first 8 bits of the value list are sent to the shift register
# the remaining two are sent to the individual GPIOs

arrow_down = [
                [0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,1,0,0],
                [0,1,0,1,0,1,0,1,0,1],
                [0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,1,0,0,0,0]
             ]


x_symbol   = [
                [1,0,0,0,0,0,0,0,1,0],
                [0,0,1,0,0,0,1,0,0,0],
                [0,0,0,0,1,0,0,0,0,0],
                [0,0,1,0,0,0,1,0,0,0],
                [1,0,0,0,0,0,0,0,1,0]
             ]

while(True):
    if( sensor2.distance_cm() > 200):
        display(arrow_down, 100)
        sleep(1)
    else:
        display(x_symbol, 1000)

