#This is the Original work of Mohammadhassan Yeganeshenas with the Student number: 041086643

#Importing CSV file that represents data
import csv

from record import Record



def readDataSet(file_path):
    """
    Reads the csv file and creats an array of Record Objects
    Parameters: 
    - file_path: path of the CSV file. 
    Returns: 
    - records: a list of record objects. 
    """
    records = [] # Creating and initializing an array
    
    
    try:    # try block 
        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            header = next(csvreader) #excepting the Header of the dataset
            
            #reading the instances row by row
            for i, row in enumerate(csvreader):
                record = Record(i +1, *row)
                records.append(record)  
            
    except FileNotFoundError: # exception for not finding the file
        print("file not found")
        
    except Exception as e: # exception for another possible errors
        print(f"an error happened: {e}")
        
        
    return records #returning the records


if __name__ == "__main__": 
    """
    Main Program in which reads the data set and displays the instances based on the numOfInstances. 
    """
    file_path = 'enterprise-data-centres-en-november-2023.csv' # path of the CSV file
    records = readDataSet(file_path) # Reading the dataset
    
    
    numOfInstances = 5 #assigning the number of instances to be shown in the output
    count = 0
    
    # Loop through the instances and printing them out to the screen
    while count < numOfInstances and count < len(records): 
        record = records[count]
        print(f"ID: {record.id}\n"
            f"Fiscal Year: {record.fiscal_year}\n"
            f"Fiscal Period: {record.fiscal_period}\n"
            f"Month: {record.month}\n"
            f"Information Date: {record.information_date}\n"
            f"Branch: {record.branch}\n"
            f"Service: {record.service}\n"
            f"SSC Client: {record.sss_client}\n"
            f"Metric Name: {record.metric_name}\n"
            f"Value: {record.value}\n"
            f"Metric Type: {record.metric_type}\n"
            "*******************************************************************\n")
        count += 1


    # Display My full name
    print("Creator Name\n"
            "Mohammadhassan Yeganeshenas")