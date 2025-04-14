def read_and_modify_file(input_filename, output_filename):
    try:
        
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        modified_content = [line.upper() for line in content]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File '{input_filename}' has been read and modified content saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or '{output_filename}' could not be written.")

input_file = input("Enter the name of the file to read from: ")
output_file = input("Enter the name of the file to write to: ")

read_and_modify_file(input_file, output_file)
