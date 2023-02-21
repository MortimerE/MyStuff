import csv
import subprocess

#SQL on csv
def query_csv(sql_query):
  # Execute the SQL query using csvql
  result = subprocess.run(['csvql', '--query', sql_query, 'data.csv'], stdout=subprocess.PIPE)

  # Convert the output to a list of rows
  rows = result.stdout.decode('utf-8').strip().split('\n')
  return [row.split(',') for row in rows]

# Read the CSV file into a list of rows
with open('data.csv', 'r') as f:
  rows = list(csv.reader(f))

# Write the organized blocks 
print(query_csv('SELECT * FROM stdin WHERE date = "2022-01-01"'))

with open(f'{name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Description', 'Amount'])
        for transaction in transactions:
            writer.writerow(transaction)

