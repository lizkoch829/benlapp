import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("C:\\Users\\Salim\\Downloads\\nfl-contracts-app-db-firebase-adminsdk-tzfkc-701dcd1182.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

clean_prefix = 'C:/Users/Salim/Desktop/ProgLangs/PythonJupNotebook/BenAndLizAppWebScraper/Clean_Team_Data/'
postfix = '-cleaned.txt'


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

# For File of Player Rows
for tn in team_names:
    infile_name = clean_prefix + tn + postfix
    infile = open(infile_name, 'r')

    # For Current Player's Row
    for line in infile:
        line = line.strip()
        line_lst = line.split()
        fName = line_lst[0]
        lName = line_lst[1]
        position = line_lst[2]
        accruedSeasons = line_lst[3]
        if (line_lst[4].count("$") == 2):
            element = line_lst[4]
            element = element.replace("$", " $")
            element = element.strip()
            element = element.split()
            baseSalary = element[0]
            baseGuarenteed = element[1]
        else:
            baseSalary = line_lst[4]
            baseGuarenteed = "$0"
            
        proratedBonus = line_lst[5]
        rosterBonus = line_lst[6]
        workoutBonus = line_lst[7]
        capNumber = line_lst[8]
        cutDM = line_lst[9]
        jCutDM = line_lst[10]
        tradeDM = line_lst[11]
        
        # Create DB Reference and Add to Collection
        doc_ref = db.collection(u'NFLPlayerContracts2018')
        doc_ref.add({
            u'CurrentTeam': tn,
            u'FirstName' : fName,
            u'LastName' : lName,
            u'Position' : position,
            u'AccruedSeasons' : accruedSeasons,
            u'BaseSalary' : baseSalary,
            u'BaseGuarenteed' : baseGuarenteed,
            u'ProratedBonus' : proratedBonus,
            u'RosterBonus' : rosterBonus,
            u'WorkoutBonus' : workoutBonus,
            u'CapNumber' : capNumber,
            u'CutDeadMoney' : cutDM,
            u'JuneFirstCutDeadMoney' : jCutDM,
            u'TradeDeadMoney' : tradeDM,
        })
    
    infile.close()
