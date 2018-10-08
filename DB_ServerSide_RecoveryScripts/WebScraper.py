import requests
from bs4 import BeautifulSoup



url_prefix = "https://overthecap.com/calculator/"
url_postfixs = ["buffalo-bills", "baltimore-ravens", "houston-texans",
               "denver-broncos", "dallas-cowboys", "chicago-bears",
               "atlanta-falcons", "arizona-cardinals", "miami-dolphins",
               "cincinnati-bengals", "indianapolis-colts", "kansas-city-chiefs",
               "new-york-giants", "detroit-lions", "carolina-panthers",
               "los-angeles-rams", "new-england-patriots", "cleveland-browns",
               "jacksonville-jaguars", "los-angeles-chargers", "philadelphia-eagles",
               "green-bay-packers", "new-orleans-saints", "san-francisco-49ers",
               "new-york-jets", "pittsburgh-steelers", "tennessee-titans",
               "oakland-raiders", "washington-redskins", "minnesota-vikings",
               "tampa-bay-buccaneers", "seattle-seahawks"]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


for team_name in url_postfixs:
    
    # Assign this iteration's website and outfile strings.
    url = url_prefix + team_name
    out_file_name =  team_name + ".txt"
    
    # Connect to this iteration's website if possible (SHITLOADA ERROR HANDLING NEEDED)
    response =  requests.get(url, headers = headers)
    
        # Use Beautiful Soup's html parser and assign it as 'soup'
    soup = BeautifulSoup(response.content, 'html.parser') 

    # Locate Tables or information to acquire
    # Can locate with 'class_ = "contracted-players"' or id = "t2018"'
    player_table = soup.find_all('table', id = 't2018')
    
    len(player_table) # ensure we were able to extract our 1 table
    
    # Extract the tag from the table element
    player_table = player_table[0]
    
    # Create Team's text file
    outfile = open(out_file_name, 'w')

    table = []
    # Extract every table row from tag element
    for row in player_table.find_all('tr'):
        table_row = []
        counter = 0 
        # Extract every cell from row element
        for cell in row.find_all('td'):
            cell_str = cell.text

            # Format Difficult Cell
            if counter == 9:
                cell_str = cell_str[43:]
                cell_str = cell_str.replace('\n', '')

            cell_str = cell_str.strip()# Trim White Space
            if cell_str: # If not empty string (empty string is 'falsy' value)
                table_row.append(cell_str)

            counter += 1
        table.append(table_row)

    for row in table:
        row_str = ""
        if len(row) == 0:
            continue
        for ele in row:
            dollarSignCount = ele.count("$")
            if (dollarSignCount > 2):
                ele = ele.replace("$", " $")
                ele = ele.replace("( $", " ($")
                ele = ele.strip()
                ele = ele.split()
                for i in ele:
                    row_str += i
                    row_str += " "
            else:
                row_str += ele
                row_str += " "

        row_str = row_str.strip()
        row_str += "\n"
        outfile.write(row_str)

    outfile.close()
