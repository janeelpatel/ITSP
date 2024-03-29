# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain

import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
# CLK  = 18
# MISO = 23
# MOSI = 24
# CS   = 25
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def read_val(): # port specifies the port to be read from
	return mcp.read_adc(0), mcp.read_adc(1), mcp.read_adc(2), mcp.read_adc(3) # 10-bit data reading from port
