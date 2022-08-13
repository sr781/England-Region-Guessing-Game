import turtle
import pandas
import string
from png_marker import Marker
map_mark = Marker()
screen = turtle.Screen()
screen.title("Regions of England - Game by Sulav Rai")
image = "england.gif"
turtle.addshape(image)
turtle.shape(image)
game_is_active = True
region_data = pandas.read_csv("england.csv")  # Uses the pandas library to read the "england.csv" file into a dataframe (called "region_data")
correct_answer = []  # If a guess is correct, it is stored in this list so that it cannot be used again
regions_guessed = 0
while game_is_active:
    answer = screen.textinput(title=f"{regions_guessed}/9 Guessed Correctly", prompt="Guess a region of England: ")  # Prompts the user to enter a guess
    if answer == "":
        missing_regions = [miss_region for miss_region in region_data["region"] if miss_region not in correct_answer]  # If the user ends the game by entering nothing in the prompt, the missing regions are shown
        game_is_active = False
        print("Game ended, the missing regions are: ")
        for a in missing_regions:
            print(a)
    answer = string.capwords(answer, sep=None)  # This function capitalises the first letter of each word
    for region in region_data["region"]:  # From the data frame, this for loop goes through the "region" column
        if region == answer:  # If the guess is equal to a region from the csv file, this if statement is triggered
            check_if_already_answered = answer not in correct_answer  # If the region hasn't already been guessed, the variable is set as "True"
            if check_if_already_answered:
                correct_answer.append(answer)  # The user entered answer is appended into the list
                regions_guessed += 1
                region_row = region_data[region_data.region == answer]  # The row for the region is obtained
                x_cor = region_row["x"].item()  # The x and y coordinates are obtained and the ".item()" only keeps the element
                y_cor = region_row["y"].item()
                map_mark.mark(x_cor, y_cor, answer)  # This function is called which plots the region on the map
    if regions_guessed == 9:  # If all the regions are guessed, the game ends
        game_is_active = False


screen.exitonclick()
