# microserviceA

Microservice A - Temperature Conversion
Communication Contract
Requesting Data
To request a temperature conversion, you need to write the temperature value to the appropriate input file based on the conversion you want to perform. The microservice will read the input file, perform the conversion, and write the result to the output.txt file.

**Input Files:**
fahrenheit_to_celsius_input.txt: Write the Fahrenheit value to convert to Celsius.
celsius_to_fahrenheit_input.txt: Write the Celsius value to convert to Fahrenheit.
celsius_to_kelvin_input.txt: Write the Celsius value to convert to Kelvin.

**Example Call**
To convert 32°F to Celsius:

Write 32 to fahrenheit_to_celsius_input.txt.
with open("fahrenheit_to_celsius_input.txt", "w") as f:
    f.write("32")

**Receiving Data**
After writing the value to the input file, wait for the microservice to process the conversion. The result will be written to output.txt.

**Example Code**
To read the conversion result from output.txt:
import time

# Wait for the microservice to process the conversion
time.sleep(2)  # Adjust the sleep time as needed

# Read the conversion result from output.txt
with open("output.txt", "r") as f:
    conversion_result = f.read()
    print("Conversion Result:", conversion_result)
