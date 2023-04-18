#! usr/bin/python3
# -*- coding: utf-8 -*-
################################################################################
# <CREATE XML TO CSV >  This script will generate csv file from given xml file 
# Usage : python create_csv.py
#            -input_xml_file="E:\Shruti\Python\Python_scripts.xml"
#            -output_csv_file="D:\python\output\Team_Skillset.csv"
# Based on different scenario script will return different exit code as follows:
#  0: Ran Successfully.
# -1: Script Failure.
################################################################################

# Importing Required Libraries
import argparse
import sys
import csv
import xml.etree.ElementTree as ET
import os

# Defining Global Parameters
input_xml_file = ""
output_csv_file = ""

################################################################################
# Function Name  : create_csv
# Arguments      : input_xml_file,output_csv_file
# Return Value   : 0,-1
# Called By      : main
# Description    : This function will parse input xml file and generate output into csv file
################################################################################
def create_csv(input_xml_file,output_csv_file):
    try:
        # Open the CSV file for writing
        with open(output_csv_file, 'w', newline='') as csvfile:
        # Create a CSV writer object
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow(['Company', 'Team Members', 'Python_Rating', 'Git', 'SW_Code_Quality', 'Database', 'Jenkins'])

            # Load the XML file
            tree = ET.parse(input_xml_file)
            root = tree.getroot()
          

            # Loop through the team members
            for member in root.find('ListOfTeamMembers').findall('TeamMember'):
                # Extract the data
                name = member.find('Name').text
                python_rating = member.find('Python_Rating').text
                git = member.find('Git').text
                code_quality = member.find('SW_Code_Quality').text
                database = member.find('Database').text
                jenkins = member.find('Jenkins').text

                # Write the data to the CSV file
                writer.writerow(['A-devops', name, python_rating, git, code_quality, database, jenkins])
    except Exception as e:
        raiseException(e, "Error While creating csv file from input xml")
    else:
        print("output csv file generated Successfully at location: ",output_csv_file)
################################################################################
# Function Name  : process_cmdl_args
# Arguments      : None
# Return Value   : -1 (in case of failure)
# Called By      : main
# Description    : Read command line arguments
################################################################################
def process_cmdl_args():
    global input_xml_file,output_csv_file

    print("Reading Command Line Arguments..")

    # Reading All Command Line Arguments
    parser = argparse.ArgumentParser(description="Template File For Python")
    parser.add_argument("-input_xml_file", "--input_xml_file", type=str, nargs=1, default=None, required=True, help="Give the input file path from which data shall be extracted")
    parser.add_argument("-output_csv_file", "--output_csv_file", type=str, nargs=1, default=None, required=True, help="Give the output file path where csv shall be stored")
    # Assigning the Command Line Arguments to Global Variables
    try:
        args = parser.parse_args()
        input_xml_file = args.input_xml_file[0]
        output_csv_file = args.output_csv_file[0]
        
        #To check the input_xml_file path is valid or not
        if not os.path.exists(input_xml_file):
             print("File path is not valid")
             raiseException("Error:", " input xml file is not present at given location please give correct path")
       
       # check if output directory path is already exist if not exist then create
        directory = os.path.dirname(output_csv_file)
        if not os.path.exists(directory):
            os.makedirs(directory)
             
    except Exception as e:
        raiseException(e, "Error While Reading Command Line arguments")
    else:
        print("Arguments Fetched Successfully!")

################################################################################
# Function Name  : raiseException
# Arguments      : err, msg
# Return Value   : -1
# Called By      : Wherever we want to raise exception.
# Description    : Helper Function to give exception and exit the system!
################################################################################
def raiseException(err, msg):
    print(f"Exception Occurred: {msg} : {err}")
    sys.exit(-1)

################################################################################
# Function Name  : main
# Arguments      : None
# Return Value   : 0,-1
# Called By      : None
# Description    : This is the main function.
################################################################################
def main():
    global input_xml_file,output_csv_file

    # Processing Command Line Arguments
    process_cmdl_args()

    # Calling our create csv funcition which will generate output csv file from input xml file
    create_csv(input_xml_file,output_csv_file)

if __name__ == '__main__':
    print("================== A-DEVOPS PYTHON: TEMPLATE ==================")
    main()