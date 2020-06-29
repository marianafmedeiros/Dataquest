from csv import reader, writer

input_filename = './hacker_news.csv'
output_filename = './hacker_news_cleaned.csv'

with open(input_filename, newline='\n') as f_input, open(output_filename, 'w', newline='\n') as f_output:
    csv_input = reader(f_input)
    csv_output = writer(f_output)
    
    for row in csv_input:
        if row [4] != '0':
            csv_output.writerow(row)