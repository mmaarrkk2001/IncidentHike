# rows are numbered from top to bottom (i.e. row 1 is top row of puzzle)
# columns are numbered left to right
# boxes are from left to right, top to bottom (box 1 is top left, 3 top right)

# this list is used to work out the box any number is in
row_to_box_switcher = [[1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3],
                       [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6],
                       [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9]]
#these are the co-ordinates of every number in a box
box_1 = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
box_2 = [[0,3],[0,4],[0,5],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5]]
box_3 = [[0,6],[0,7],[0,8],[1,6],[1,7],[1,8],[2,6],[2,7],[2,8]]
box_4 = [[3,0],[3,1],[3,2],[4,0],[4,1],[4,2],[5,0],[5,1],[5,2]]
box_5 = [[3,3],[3,4],[3,5],[4,3],[4,4],[4,5],[5,3],[5,4],[5,5]]
box_6 = [[3,6],[3,7],[3,8],[4,6],[4,7],[4,8],[5,6],[5,7],[5,8]]
box_7 = [[6,0],[6,1],[6,2],[7,0],[7,1],[7,2],[8,0],[8,1],[8,2]]
box_8 = [[6,3],[6,4],[6,5],[7,3],[7,4],[7,5],[8,3],[8,4],[8,5]]
box_9 = [[6,6],[6,7],[6,8],[7,6],[7,7],[7,8],[8,6],[8,7],[8,8]]

# this variable used to stop the main loop, when puzzle is solved
puzzle_not_solved = 1

#this variable is used to stop the programme looping forever!
max_loops = 10

#This list used to store all of the unknown numbers in the puzzle
unknown_numbers = []


def get_puzzle():
    # function to ask user for input
    # first we create a list to contain the puzzle
    puzzle_list = []

    row = 1
    print("I will ask for each row in order, row 1 is the top line of the puzzle. Enter unknowns as zero")
    while row < 10:

        my_str = input("Please enter row %a :\n" % (row))
        if len(my_str) > 9:
            print("That's too many!")
        elif len(my_str) < 9:
            print("That's too few!")
        else:

            puzzle_list.append(["x", "x", "x", "x", "x", "x", "x", "x", "x"])
            # print("just appeneded a blank row, puzzle list =", puzzle_list, "\nrow=",row)

            for x in range(0, 9):
                puzzle_list[row - 1][x] = int(my_str[x])

            row = row + 1

    print("\npuzzle list =")
    for x in range(0, 9):
        print(puzzle_list[x])

    return (0, puzzle_list)

def get_puzzle_file():
    # function to get input from file

    #First, open the file and read first row
    my_file = open("Input.txt","r")

    my_str = my_file.readline()



    # create a list to contain the puzzle
    puzzle_list = []

    row = 1

    #Now loop through the file and get the input
    while row < 10:

        # remove newline character
        my_str = my_str.rstrip("\n")

        if len(my_str) > 9:
            print("That's too many!")
        elif len(my_str) < 9:
            print("That's too few!")
        else:

            puzzle_list.append(["x", "x", "x", "x", "x", "x", "x", "x", "x"])
            # print("just appeneded a blank row, puzzle list =", puzzle_list, "\nrow=",row)

            for x in range(0, 9):
                puzzle_list[row - 1][x] = int(my_str[x])

            #Print out what we have read
            print("Row ", row," added = ",puzzle_list[row-1])

            #move onto the next row
            row = row + 1

        #read next row
        my_str = my_file.readline()

    print("\npuzzle list =")
    for x in range(0, 9):
        print(puzzle_list[x])

    return (0, puzzle_list)



def check_row(row_list):
    # this function loops through a list, and counts the zeros.
    # if there is only one, it will work out the missing number
    # function will return 0 if 0 or > 1 number missing, else it will return the number and updated row

    print("check_row called with row =", row_list)

    num_zeros = 0
    missing_number = 45
    position = 0

    for x in range(0, 9):
        if row_list[x] == 0:
            num_zeros = num_zeros + 1
            position = x
        missing_number = missing_number - int(row_list[x])

    print("missing_number =", missing_number, "\nnum_zeros =", num_zeros)

    if num_zeros == 1:
        # only 1 number  issing in row, let's work out which one!
        # 9+8+7+6+5+4+3+2+1= 45, subtract all the known number and what is left is unknown number

        row_list[position] = missing_number

        print("\nUpdated row is:", row_list)
        return (missing_number, row_list)

    else:

        return (0, row_list)


def row_checker(row_list, avail_nums):
    # this function is going to update a list of available numbers, removing any in the list that are in the passed row

    print("row checker called with list =", row_list, " and avail_nums =", avail_nums)
    for x in range(0, 9):
        if int(row_list[x]) > 0:
            print("removing:", row_list[x])

            avail_nums[row_list[x] - 1] = 0

    print("row checker complete, returning availnum list:", avail_nums)
    return (0, avail_nums)

def number_finder(unknown_numbers, puzzle_list):
    #this function goes through each unknown number list and checks if this is down to one number
    #which means that the missing number has been found
    #we then update the puzzle, and delete this entry from the unknown_numbers list.

    del_numbers = []

    #loop through the unknown_numbers
    for x in range (0,len(unknown_numbers)):
        my_counter = 0
        my_number = 0

        for y in range (0,9):
            print("Checking unknown_numbers[",x,"][2][",y,"] = ",unknown_numbers[x][2][y])
            if unknown_numbers[x][2][y] > 0: #we have a 3 dimension array, 2 is where the avail num list is.
                my_counter = my_counter + 1
                my_number = unknown_numbers[x][2][y] #hold the number for use later!

        if my_counter == 1: #this means we have only one available number!

            my_row = int(unknown_numbers[x][0])
            my_column = int(unknown_numbers[x][1])
            print("number_finder has found a number!")
            print("unknown_numbers record: ", unknown_numbers[x])
            print("I'm updating row", my_row +1 , ", column = ", my_column+1)
            print("")

            #first update the puzzle list.
            print("Current row entry in puzzle_list = ",puzzle_list[my_row] )
            puzzle_list[my_row][my_column] = my_number
            print("Updated row entry in puzzle_list = ", puzzle_list[my_row])

            #Hold a record of the unknown number entries we need to delete later:
            del_numbers.append(unknown_numbers[x])

    #now delete all of the found records:
    for x in range (0,len(del_numbers)):
        print("now deleting a found record: ", del_numbers[x])
        unknown_numbers.remove(del_numbers[x])
        print("unknown_numbers is now: ", unknown_numbers)


    return(0, unknown_numbers, puzzle_list)

def calc_box(box_number, puzzle_list):
    #This function will creat a list of numbers in a box on the grid.
    #first reset the list
    my_list = []

    if box_number == 1:
        #loop through the cordinates and create a new list
        for x in range(0,len(box_1)):
            my_list.append(puzzle_list[box_1[x][0]][box_1[x][1]])
    elif box_number == 2:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_2)):
            my_list.append(puzzle_list[box_2[x][0]][box_2[x][1]])
    elif box_number == 3:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_3)):
            my_list.append(puzzle_list[box_3[x][0]][box_3[x][1]])
    elif box_number == 4:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_4)):
            my_list.append(puzzle_list[box_4[x][0]][box_4[x][1]])
    elif box_number == 5:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_5)):
            my_list.append(puzzle_list[box_5[x][0]][box_5[x][1]])
    elif box_number == 6:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_6)):
            my_list.append(puzzle_list[box_6[x][0]][box_6[x][1]])
    elif box_number == 7:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_7)):
            my_list.append(puzzle_list[box_7[x][0]][box_7[x][1]])
    elif box_number == 8:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_8)):
            my_list.append(puzzle_list[box_8[x][0]][box_8[x][1]])
    elif box_number == 9:
        # loop through the cordinates and create a new list
        for x in range(0, len(box_9)):
            my_list.append(puzzle_list[box_9[x][0]][box_9[x][1]])

    print("======================================)")
    print("calc_box called for box - ", box_number)
    print("returning: ", my_list)

    return(0, my_list)



# START OF PROGRAMME

#Initialise the counter:
loop_count = 0

# First we load the input puzzle up into a set of lists, one list per row

#This version will ask for input
#puzzle_list = get_puzzle()[1]

#This version will get input from a file
puzzle_list = get_puzzle_file()[1]



# start the main loop of the progamme
while puzzle_not_solved:

    loop_count = loop_count + 1
    # First we need to loop through each row, and see if there are any single unknowns (these can then be calculated)
    for x in range(0, 9):
        print("===========================")
        print("Checking row ",x+1)
        print("===========================")

        function_output = check_row(puzzle_list[x])

        # if we didnt find the solution, then we loop to find the first blank, and work which numbers it cant be
        if function_output[0] == 0:
            print("didn't fix row ", x + 1, " yet - checking for first blank...")
            for y in range(0, 9):

                if int(puzzle_list[x][y]) == 0:
                    # we have found a zero!
                    print("Zero found in row ", x+1, " at postion:", y + 1)

                    # We will use a list to hold all of options for the numbers we are looking for.
                    # This will only hold an item for each blank, so the item will need to be keyed.
                    unknown_numbers.append([str(x),str(y),[1,2,3,4,5,6,7,8,9]])
                    my_index=len(unknown_numbers)

                    print("unknown_numbers = ",unknown_numbers)
                    print("number of unknown_numbers = ", len(unknown_numbers), " my_index = ", my_index)

                    # Call the row checker
                    #we only need to send in the number string, in index 2
                    function_output = row_checker(puzzle_list[x],unknown_numbers[my_index-1][2])

                    if function_output[0] == 0:
                        #success, update the available nums
                        unknown_numbers[my_index - 1][2] = function_output[1]
                    else:
                        print("Call to row checker for row failed")

                    #Need to think about identifying where a number can only be in one square, even if others
                    #could also be valid in the square.

                    print("end of row check")
                    print("")

                    # Now we check the column. First, a call to the row checker again, but with the column as the input list.
                    # first set up the column, create an empty list and add each number in the column in

                    column_list = []

                    print("calling row_checker for column ", y+1 )

                    for z in range(0, 9):
                        column_list.append(puzzle_list[z][y])

                    print("column is ",column_list)

                    function_output = check_row(column_list)

                    if function_output[0] > 0:
                        # we found a number for this row! the checker returns the new row, so update the puzzle_list
                        puzzle_list[x] = function_output[1]
                    elif function_output[0] == 0:
                        #We didn't find a number, so we need to call the row checker.
                        function_output = row_checker(column_list, unknown_numbers[my_index - 1][2])
                        if function_output[0]==0:
                            unknown_numbers[my_index - 1][2] = function_output[1]
                        else:
                            print("row_checker failed on column call")

                    # Now we check the box. First, a call to the row checker again, but with the column as the input list.
                    # first set up the column, create an empty list and add each number in the column in

                    box_list = []

                    # we need to work out what box we are in. The switcher list will return the box number for any puzzle element.
                    my_box = row_to_box_switcher[x][y]

                    function_output = calc_box(my_box, puzzle_list)

                    if function_output[0] != 0:
                        print("calc_box failed on call")
                    else:
                        #Box Checker returns a list.
                        box_list = function_output[1]

                    print("calling row_checker for Box ", my_box )

                    function_output = check_row(box_list)

                    if function_output[0] > 0:
                        # we found a number for this row! the checker returns the new row, so update the puzzle_list
                        puzzle_list[x] = function_output[1]
                    elif function_output[0] == 0:
                        #We didn't find a number, so we need to call the row checker.
                        function_output = row_checker(box_list, unknown_numbers[my_index - 1][2])
                        if function_output[0]==0:
                            unknown_numbers[my_index - 1][2] = function_output[1]
                        else:
                            print("row_checker failed on column call")


        elif function_output[0] > 0:
            #we found a number for this row! the checker will update the main puzzle list as we passed in this list.
            #nothing else to do here
            print("======================================")
            print("row ",x+1," complete")
            print("======================================")


        else:
            #row-checker failed
            print("row checker failed")

    #Now we need to check if we found any numbers:
    function_output = number_finder(unknown_numbers,puzzle_list)

    if function_output[0]==0:
        unknown_numbers=function_output[1]
        puzzle_list=function_output[2]

    print("Puzzle_list = ", puzzle_list)



    # Check we have not hit our max loops:
    if loop_count == max_loops:
        print("==============================")
        print("We hit the max loops :-(")
        print("Puzzle not solved")
        print("Puzzle_list = ", puzzle_list)
        print("unknown_numbers = ", unknown_numbers)
        print("==============================")
        puzzle_not_solved = 0

    #Have we solved the puzzle?
    if len(unknown_numbers)==0:
        print("We Solved the Puzzle!")
        print("Answer is:")
        print(puzzle_list)
        puzzle_not_solved = 0

