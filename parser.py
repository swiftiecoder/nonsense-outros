import re
import csv

def parse_html_to_csv(html_code, output_csv_path):
    """
    Parses the provided HTML code to extract city and nonsense outros, then writes them to a CSV file.

    Args:
        html_code: The HTML code to parse.
        output_csv_path: The path where the output CSV file will be saved.
    """

    # Remove <a> and <span> tags but keep their content
    html_code = re.sub(r'<a[^>]*>|</a>', '', html_code)
    html_code = re.sub(r'<span[^>]*>|</span>', '', html_code)

    # Replace <br/> with '\n'
    html_code = html_code.replace('<br/>', '\n')

    # Define regex pattern for city, date, and outro
    pattern = r"<b>(.*?)</b>, <i>(.*?)</i>\n(.*?)(?=\n<b>|$)"

    # Find all matches using the regex pattern
    matches = re.findall(pattern, html_code, re.DOTALL)

    # Extract city and clean outro from matches
    city_outros = []
    for match in matches:
        city = match[0].strip()
        outro = re.sub(r'<[^>]+>', '', match[2].strip())
        city_outros.append((city, outro))

    # Write to CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['City', 'Nonsense Outro'])  # Write header
        csvwriter.writerows(city_outros)  # Write data rows

# Example usage
with open('./nonsense outros/outros.txt', 'r', encoding='utf-8') as file:
    html_code = file.read()

output_csv_path = './nonsense outros/nonsense_outros.csv'
parse_html_to_csv(html_code, output_csv_path)
print(f"CSV dataset created at {output_csv_path}")
