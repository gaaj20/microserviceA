import time

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_temperature(input_files, output_file):
    try:
        while True:
            for input_file in input_files:
                # Wait until the input file is not empty
                while True:
                    with open(input_file, 'r') as f_in:
                        value_str = f_in.read().strip()
                        if value_str:
                            break  # Break the loop if the file is not empty
                    time.sleep(1)  # Sleep for a while before checking again

                # Convert the value string to float
                try:
                    value = float(value_str)
                except ValueError:
                    print("Invalid value in input file:", value_str)
                    time.sleep(1)  # Sleep for a while before checking again
                    continue

                # Perform the corresponding temperature conversion based on file name
                if "fahrenheit_to_celsius" in input_file:
                    result = fahrenheit_to_celsius(value)
                    unit = "Celsius"
                elif "celsius_to_fahrenheit" in input_file:
                    result = celsius_to_fahrenheit(value)
                    unit = "Fahrenheit"
                else:
                    result = celsius_to_kelvin(value)
                    unit = "Kelvin"

                # Write the conversion result to the output file
                with open(output_file, 'a') as f_out:  # Open in append mode to preserve existing content
                    f_out.write("{:.2f} {}\n".format(result, unit))

                # Clear the content of the input file
                with open(input_file, 'w') as f_clear:
                    f_clear.truncate(0)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    input_files = ["fahrenheit_to_celsius_input.txt", "celsius_to_fahrenheit_input.txt", "celsius_to_kelvin_input.txt"]
    output_file = "output.txt"
    convert_temperature(input_files, output_file)
