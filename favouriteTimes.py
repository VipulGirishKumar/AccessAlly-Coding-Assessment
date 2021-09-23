# PROBLEM 1: FINDING FAVORITE TIMES
# This program calculates favourite number

# Global Variables
# initialize time variables to show 12:00.
# left_digit_hour represents the 1 in 12:34.
left_digit_hour = 1
# right_digit_hour represents the 2 in 12:34.
right_digit_hour = 2
# left_digit_min represents the 3 in 12:34.
left_digit_min = 0
# right_digit_min represents the 4 in 12:34.
right_digit_min = 0

# FUNCTIONS

# The following function increments hour by 1 on a 12-hour clock.
def incHour():
    global left_digit_hour
    global right_digit_hour
    current_hour = (left_digit_hour * 10) + right_digit_hour
    if current_hour == 12:
        left_digit_hour = 0
        right_digit_hour = 1
    else:
        current_hour += 1
        right_digit_hour = (current_hour % 10)
        left_digit_hour = ((current_hour - left_digit_hour) // 10)

# The following function increments minute by 1 on a 12-hour clock with 60min per hour.
def incMin():
    global left_digit_min
    global right_digit_min
    current_minute = (left_digit_min * 10) + right_digit_min
    if current_minute == 59:
        # increments hour by 1 when the current minute is 59 and resets the minute to 00.
        left_digit_min = 0
        right_digit_min = 0
        incHour()
    else:
        current_minute += 1
        right_digit_min = (current_minute % 10)
        left_digit_min = ((current_minute - right_digit_min) // 10)

# The following function prints the time in a valid format.
def printTime(left_digit_hour, right_digit_hour, left_digit_min, right_digit_min):
    print(left_digit_hour + right_digit_hour + ":" + left_digit_min + right_digit_min)

# checking if the current time value is a favorite time
def checkFavNumber():
    hour_hour_difference = right_digit_hour - left_digit_hour
    hour_min_difference = left_digit_min - right_digit_hour
    min_min_difference = right_digit_min - left_digit_min
    if left_digit_hour == 0:
        if hour_min_difference == min_min_difference:
            return True
    elif hour_hour_difference == hour_min_difference and hour_min_difference == min_min_difference:
            return True
    else:
        return False

# MAIN PROGRAM

# Input
input_duration = int(input("Enter the D value (duration the minutes clock is observed): "))
# Since there are many 12-hours in a clock, we can breakdown the duration into multiple sets of 12-hour.
remaining_hours = input_duration % (12 * 60)
twelve_hour_clock = (input_duration - remaining_hours) // (12 * 60)
# initialize the count value to 0.
fav_num_count = 0

# Now we find the favourite number and print it.
if twelve_hour_clock > 0:
    for i in range(12 * 60):
        incMin()
        if checkFavNumber():
            fav_num_count += 1
    fav_num_count *= twelve_hour_clock

for i in range(remaining_hours):
    incMin()
    if checkFavNumber():
        fav_num_count += 1

print("\n")
print("Number of Favorite Times:", fav_num_count)

# END OF PROGRAM