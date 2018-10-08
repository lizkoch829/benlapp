import os

raw_prefix = "C:/Users/Salim/Desktop/ProgLangs/PythonJupNotebook/BenAndLizAppWebScraper/Raw_Team_Data/"
clean_prefix = "C:/Users/Salim/Desktop/ProgLangs/PythonJupNotebook/BenAndLizAppWebScraper/Clean_Team_Data/"
postfix = "-cleaned.txt"


team_names = ["buffalo-bills", "baltimore-ravens", "houston-texans",
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


for tn in team_names:
    infile_name = raw_prefix + tn + postfix
    team_DM_file_name = clean_prefix + tn + "-DM" + postfix
    team_roster_file_name = clean_prefix + tn + "-cleaned" + postfix

    infile = open(infile_name, 'r')
    team_DM_file = open(team_DM_file_name, 'w')
    team_roster_file = open(team_roster_file_name, 'w')


    for line in infile:
        line_lst = line.split()

        if (len(line_lst) > 16):
            team_roster_file.write(line)

        elif (line_lst[0] == "TOP" or line_lst[0] == "Top" or line_lst[0] == "TOTAL" or line_lst[0] == "Projected"):
            continue

        else:
            team_DM_file.write(line)

    infile.close()
    team_DM_file.close()
    team_roster_file.close()
