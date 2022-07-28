from fileconverter import read_and_convert_file
import os

def main():
    file_name = "Submit_Seller_Account_for_Approval.flow-meta.xml"
    file_extension = "flow"
    read_and_convert_file(file_name, file_extension)

if __name__ == "__main__":
    main()