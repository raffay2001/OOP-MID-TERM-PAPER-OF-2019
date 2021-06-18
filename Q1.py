import datetime

# FIRST CLASS STADIUM 
class Stadium:
    # INITIATOR OF CLASS STADIUM 
    def __init__(self, area = 7888, location = "Karachi"):
            self.area = area
            self.location = location

    # METHOD FOR SETTING THE AREA OF THE STADIUM 
    def set_area(self):
        self.area = int(input(f"Enter the Area in Sq.m: "))

    # METHOD FOR DISPLAYING THE AREA OF THE STADIUM     
    def get_area(self):
        print(f"The area of the Stadium is: {self.area}")

    # METHOD FOR SETTING THE LOCATION OF THE STADIUM 
    def set_location(self):
        self.location = int(input(f"Enter the location of the Stadium: "))

    # METHOD FOR DISPLAYING THE LOCATION OF THE STADIUM 
    def get_location(self):
        print(f"The Location of the Stadium is: {self.location}")


# SECOND CLASS MATCH 
class Match:

    # SETTING UP A COUNTER TO TRACK FOR THE NUMBER OF MATCHES AS THE USER INSTANTIATE MATCH TYPE OBJECT 
    counter = 0
    #INITIALIZING AN EMPTY LIST TO STORE ALL THE MATCHES
    no_of_matches = []

    # INITIATOR OF CLASS MATCH 
    def __init__(self, run_chase = None, lowest_player_score = None):

        self.run_chase = run_chase
        self.lowest_player_score = lowest_player_score

        Match.counter += 1              #INCREAMENTING THE COUNTER WHEN THE USER MAKE AN OBJECT OF MATCH TYPE
        self.counter = Match.counter    #ASSIGNING THE VALUE OF INCREAMENTED COUNTER TO AN INSTANCE VARIABLE
        
        Match.no_of_matches.append(f"Match {self.counter}")    #APPENDING ALL THE MATCHES IN THE ABOVE LIST.

    # METHOD FOR SETTING THE RUN CHASE IN THE MATCH 
    def set_run_chase(self):
        self.run_chase = int(input(f"Enter the run chase: "))
    
    # METHOD FOR DISPLAYING THE RUN CHASE IN THE MATCH 
    def get_run_chase(self):
        print(f"The run chase in the match is: {self.run_chase}")
    
    # METHOD FOR SETTING THE LOWEST SCORE IN THE MATCH 
    def set_lowest_player_score(self):
        self.lowest_player_score = int(input(f"Enter the lowest score of the match: "))

    # METHOD FOR DISPLAYING THE LOWEST SCORE IN THE MATCH 
    def get_lowest_player_score(self):
        print(f"The lowest score of the match is: {self.lowest_player_score}")

    # METHOD FOR DISPLAYING THE TOTAL NUMBER MATCHES TO THE USER 
    def show_total_matches(self):
        print(f"The list of the Number of Matches Played are: {Match.no_of_matches}")
    
    # METHOD FOR DISPLAYING THE MATCH DATE 
    def show_match_date(self):
        print(f"The Match was Played on: {datetime.date.today()}")


# THIRD CLASS TEAM 
class Team:

    # INITIATOR OF CLASS TEAM 
    def __init__(self, team1 = "", team2 = ""):
        self.team1 = team1
        self.team2 = team2

    # METHOD FOR SETTING THE NAME OF TEAM 1
    def set_team1(self):
        self.team1 = input(f"Enter the name of Team 1: ")

    # METHOD FOR DISPLAYING THE NAME OF TEAM 1
    def get_team1(self):
        print(f"The name of the Team 1 is: {self.team1}")

    # METHOD FOR SETTING THE NAME OF TEAM 2
    def set_team2(self):
        self.team2 = input(f"Enter the name of Team 2: ")

    # METHOD FOR DISPLAYING THE NAME OF TEAM 2
    def get_team2(self):
        print(f"The name of the Team 2 is: {self.team2}")

    # METHOD FOR THE TOSS
    def toss(self):
        self.toss = input(f"Enter the name of Toss Winning Team: ")

        print(f"The Toss Has won By the Team: {self.toss}")

# DRIVER CODE : 

# MAKING 1st MATCH TYPE OBJECT 
m  = Match()
m.set_run_chase()
m.set_lowest_player_score()
m.get_run_chase()
m.get_lowest_player_score()
m.show_match_date()

# MAKING 2nd MATCH TYPE OBJECT 
m1  = Match()
m1.set_run_chase()
m1.set_lowest_player_score()
m1.get_run_chase()
m1.get_lowest_player_score()
m1.show_match_date()

# SHOWING TOTAL NUMBER OF MATCHES
m.show_total_matches()