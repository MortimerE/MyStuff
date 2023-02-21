#import google-auth
#import google-api-python-client
import csv
import re
import PyPDF2

# Open the PDF file
statement = input("name of the pdf file containing the card statement: ")
with open(statement, 'rb') as f:
    # Create a PDF object
    pdf = PyPDF2.PdfFileReader(f)
    i=0
    text = ""
    for page in pdf.pages:
        page = pdf.getPage(i)
        i += 1
        # Extract the text from the PDF
        text += page.extract_text() + '\n'
    
    #slicing input to only retrieve payments of interest 
    name = "<Cardholder Name>"
    dig = "<first 4 digits>"
    its = "<last 4 digits>"
    filestart = text.find(f"{name} - {dig} XXXX XXXX {its}")
    transactions = text.find(f"Total Transactions For {name}")
    charges = text[filestart:fileend]
    with open('output.txt', 'a') as fil:
        fil.write(charges)
    # Use regular expressions to extract the relevant information from the text
    transactions = []
    for line in charges.split('\n'):
        # Extract the date, description, and amount for each transaction
        date_pattern = r'(\d+/\d+)'
        description_pattern = r'([\w\s]+)'
        amount_pattern = r'(\$\d+.\d+)'
        match = re.search(f'{date_pattern}\s+{description_pattern}\s+{amount_pattern}', line)
        if match:
            date, description, amount = match.groups()
            transactions.append((date, description, amount))
    
    # Write the transactions to a CSV file
    delimiter = statement.find('.')
    name = statement[:delimiter]
    with open(f'{name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Description', 'Amount'])
        for transaction in transactions:
            writer.writerow(transaction)

'''Next, you'll need to authenticate your program with the Google Sheets API. You can do this by creating a Google API project, enabling the Google Sheets API for the project, and creating a service account and downloading the private key file. Then, you can use the google-auth and google-api-python-client libraries to authenticate your program and authorize it to access your Google Sheets data.

Now you can use the PyPDF2 library to open and read the PDF file. You'll need to extract the text from the PDF, which you can do using the extractText() method of the PyPDF2 library.

Once you have the text from the PDF, you'll need to parse it to extract the relevant information. This will likely involve using regular expressions or string manipulation techniques to extract the data you need.

With the data extracted and organized, you can now use the google-api-python-client library to write the data to a Google Spreadsheet. You'll need to create a new spreadsheet or specify an existing one to write to, and then use the append() method of the google-api-python-client library to add the data to the sheet.
'''