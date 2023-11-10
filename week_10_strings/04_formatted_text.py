# ignoring special characters
my_file_path = "C:\\Users\\John\\Desktop"
my_file_path = "C:/Users/John/Desktop"
my_file_path = r"C:\Users\John\Desktop"

subdirectory_location_list = ["Scripts", "Libs"]

for subdirectory_location in subdirectory_location_list:
    print(f"{my_file_path}\{subdirectory_location}")

print(f"The root directory is: {my_file_path}")
