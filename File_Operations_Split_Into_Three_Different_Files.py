print("""********************************************************************************************
Subject: File Operations

Instruction: Free to choose any topic that is available to split into min. three groups.
# Create main source file and its elements needs to be randomly ordered.
# If you want to use mine: 
https://github.com/acarismet/Python_Begginer_Projects_For_Exercise/blob/main/all_gods.txt
# Elements of main source file will be split into three groups like Greek Gods and Goddesses,
Egyptian Gods and Goddesses, Norse Gods and Goddesses.
# You can check to understand index order above link.
*************************************************************

There are two ways. I tried to improve to clean my code.
First of all I created three different functions and as a second way I cleaned them and re_create cleaner code.
I see these long ways as an improvement process so however I prefer always clean cod, also sharing long ways to show
the solution ways that I thought.
 
******************************************************************************************************
######################################### FIRST LONG WAY #############################################
******************************************************************************************************

All Stages of First Long Way:
# Three different functions were created to split Greeks, Norse and Egyptian into three new files.
Keypoint: There must be a str, integer or float to specify the group to split.
So I used str ([1] index) in if else statement to specify which nation does God or Goddess belong to. 
And I had to give indent. This indent is actually available to fill. I preferred God and Goddess.
The ones that stayed out of if conditions return as None under the else statement.
And finally schema of god/goddess names and their nations returned under if-else statement. 

#  After def functions: (in order)
Reading main source file, list append and filtering Nones
Creating/Writing new file
Adding title in front of file with 'r+' file access mode

********************************************************************************************
""")



def greek(line):

    line = line[:-1]
    g_list = line.split(",")

    if (g_list[1] == "Greek God"):
        g_list[1] = "God"

    elif (g_list[1] == "Greek Goddess"):
        g_list[1] = "Goddess"
    else:
        return None

    return g_list[0] + "------>" + g_list[1] + "\n"


def egyptian(line):
    line = line[:-1]
    g_list = line.split(",")

    if (g_list[1] == "Egyptian God"):
        g_list[1] = "God"

    elif (g_list[1] == "Egyptian Goddess"):
        g_list[1] = "Goddess"
    else:
        return None

    return g_list[0] + "------>" + g_list[1] + "\n"


def norse(line):
    line = line[:-1]
    g_list = line.split(",")

    if (g_list[1] == "Norse God"):
        g_list[1] = "God"

    elif (g_list[1] == "Norse Goddess"):
        g_list[1] = "Goddess"
    else:
        return None

    return g_list[0] + "------>" + g_list[1] + "\n"


with open("all_gods.txt", "r")as file:

    greek_list = []
    for i in file:

        greek_list.append(greek(i))

    print("greek_list\n", greek_list)
    greek_list = filter(None, greek_list)
    print("new_greek_list:\n", greek_list)

    with open("greek_gods.txt", "w") as file2:

        for i in greek_list:
            file2.write(i)

    with open("greek_gods.txt", "r+") as file5:
        g_title = file5.read()
        g_title = "All Greek Gods and Goddess\n" + g_title
        file5.seek(0)
        file5.write(g_title)

with open("all_gods.txt", "r")as file:

    egypt_list = []
    for i in file:

        egypt_list.append(egyptian(i))

    print("egypt_list\n", egypt_list)
    egypt_list = filter(None, egypt_list)
    print("new_egypt_list:\n", egypt_list)

    with open("egyptian_gods.txt", "w") as file3:

        for i in egypt_list:
            file3.write(i)

    with open("egyptian_gods.txt", "r+") as file6:
        e_title = file6.read()
        e_title = "All Egyptian Gods and Goddess\n" + e_title
        file6.seek(0)
        file6.write(e_title)

with open("all_gods.txt", "r")as file:

    norse_list = []
    for i in file:

        norse_list.append(norse(i))

    print("norse_list\n", norse_list)
    norse_list = filter(None, norse_list)
    print("new_norse_list:\n", norse_list)

    with open("norse_gods.txt", "w") as file4:

        for i in norse_list:
            file4.write(i)

    with open("norse_gods.txt", "r+") as file7:
        n_title = file7.read()
        n_title = "All Norse Gods and Goddess\n" + n_title
        file7.seek(0)
        file7.write(n_title)

print("""********************************************************************************************
https://github.com/acarismet/Python_Begginer_Projects_For_Exercise/blob/main/all_gods.txt
# You can check to understand index order above link.
******************************************************************************************************
####################################### SECOND SHORT WAY #############################################
******************************************************************************************************

All Stages of Second Short Way:
# This time I didn't created functions.

# Under reading main source file ------>
   - declared variables that represent three nations of gods and goddess
   - started for loop in file (variable of reading main source file)
   - put [1] index of line in if else statement for all nations of gods and goddesses.
   - append to lists according to [1] index str
   - rest of it kind of same with long way there is no shorter way to write them:    
        Creating/Writing new file
        Adding title in front of file with 'r+' file access mode

********************************************************************************************
""")

with open("all_gods.txt", "r") as file:
    greek = []
    egyptian = []
    norse = []

    for i in file:
        line = line[:-1]
        god_line_list = line.split(",")
        if (god_line_list[1] == "Greek God" or god_line_list[1] == "Greek Goddess"):
            greek.append(line + "\n")
        elif (god_line_list[1] == "Egyptian God" or god_line_list[1] == "Egyptian Goddess"):
            egyptian.append(line + "\n")
        else:
            norse.append(line + "\n")

    with open("Greek_God_Goddess.txt", "w") as file8:
        for i in greek:
            file8.write(i)

    with open("Greek_God_Goddess.txt", "r+") as file9:
        greek_title = file9.read()
        greek_title = "All Greek Gods and Goddesses\n" + greek_title
        file9.seek(0)
        file9.write(greek_title)

    with open("Egyptian_God_Goddess.txt", "w") as file10:
        for i in egyptian:
            file10.write(i)

    with open("Egyptian_God_Goddess.txt", "r+") as file11:
        egyptian_title = file11.read()
        egyptian_title = "All Egyptian Gods and Goddess\n" + egyptian_title
        file11.seek(0)
        file11.write(egyptian_title)

    with open("Norse_God_Goddess.txt", "w") as file12:
        for i in norse:
            file12.write(i)

    with open("Norse_God_Goddess.txt", "r+") as file13:
        norse_title = file13.read()
        norse_title = "All Norse Gods and Goddess\n" + norse_title
        file13.seek(0)
        file13.write(norse_title)
