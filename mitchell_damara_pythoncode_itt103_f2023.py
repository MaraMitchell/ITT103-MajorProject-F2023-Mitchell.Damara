# -*- coding: utf-8 -*-
"""Mitchell.Damara-PythonCode-ITT103-F2023

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ug7cbScnljUg0oIfPNP3vQ_rUCMC6Hv2
"""



#  Author: Damara Mitchell
#  Date Created: 26/11/23
#  Course: ITT103
#  Purpose: Use user input to make a bus reservation. To travel from one UCC campus to another.

from tabulate import tabulate

#First Class Arrays
fc_seat_array = [
    [1, 2, " ", 15, 16],
    [3, 4, " ", 17, 18],
    [5, 6, " ", 19, 20],
    [7, 8, " ", 21, 22],
    [9, 10, " ", 23, 24],
    [11, 12, " ", 25, 26],
    [13, 14, " ", None, 27]
]

fc_window_seats_array = [
    [1," ", 16],
    [3," ", 18],
    [5," ", 20],
    [7," ", 22],
    [9," ", 24],
    [11," ", 26],
    [13," ", 27],
]

fc_aisle_seats_array = [
    [2," ", 15],
    [4," ", 17],
    [6," ", 19],
    [8," ", 21],
    [10," ", 23],
    [12," ", 25],
    [14," ", None],
]

#Business Class Arrays
bc_seat_array = [
    [1, 2, " ", 20, 21],
    [3, 4, " ", 22, 23],
    [5, 6, " ", 24, 25],
    [7, 8, " ", 26, 27],
    [9, 10, " ", 28, 29],
    [11, 12, " ", 30, 31],
    [13, 14, " ", 32, 33],
    [15, 16, " ", 34, 35],
    [17, 18, " ", 36, 37],
    [19, None, " ", None, 38],
]

bc_window_seats_array = [
    [1," ", 21],
    [3," ", 23],
    [5," ", 25],
    [7," ", 27],
    [9," ", 29],
    [11," ", 31],
    [13," ", 33],
    [15," ", 35],
    [17," ", 37],
    [19," ", 38],
]

bc_aisle_seats_array = [
    [2," ", 20],
    [4," ", 22],
    [6," ", 24],
    [8," ", 26],
    [10," ", 28],
    [12," ", 30],
    [14," ", 32],
    [16," ", 34],
    [18," ", 36],
]

#Economy Class Arrays
ec_seat_array = [
    [1, 2, " ", 29, 30],
    [3, 4, " ", 31, 32],
    [5, 6, " ", 33, 34],
    [7, 8, " ", 35, 36],
    [9, 10, " ", 37, 38],
    [11, 12, " ", 39, 40],
    [13, 14, " ", 41, 42],
    [15, 16, " ", 43, 44],
    [17, 18, " ", 45, 46],
    [19, 20, " ", 47, 48],
    [21, 22, " ", 49, 50],
    [23, 24, " ", 51, 52],
    [25, 26, " ", 53, 54],
    [27, 28, " ", 55, 56],
]

ec_window_seats_array = [
    [1," ", 30],
    [3," ", 32],
    [5," ", 34],
    [7," ", 36],
    [9," ", 38],
    [11," ", 40],
    [13," ", 42],
    [15," ", 44],
    [17," ", 46],
    [19," ", 48],
    [21," ", 50],
    [23," ", 52],
    [25," ", 54],
    [27," ", 56],
]

ec_aisle_seats_array = [
    [2," ", 29],
    [4," ", 31],
    [6," ", 33],
    [8," ", 35],
    [10," ", 37],
    [12," ", 39],
    [14," ", 41],
    [16," ", 43],
    [18," ", 45],
    [20," ", 47],
    [22," ", 49],
    [24," ", 51],
    [26," ", 53],
    [28," ", 55],
]

# Campuses
campuses = ["KINGSTON", "MANDEVILLE", "OCHO-RIOS", "MONTEGO BAY", "MAY PEN"]

# Total number of seats per bus
fClass_seat_total = 27
bClass_seat_total = 38
eClass_seat_total = 56

# Default number of reserved seats
fClass_seats_reserved = 0
bClass_seats_reserved = 0
eClass_seats_reserved = 0

# Reservation lists
fClass_seat_reservation_list = []
bClass_seat_reservation_list = []
eClass_seat_reservation_list = []

validOptions = ['F', 'B', 'E', 'Q', 'C', 'EXIT']
validCol_options = ['WINDOW', 'AISLE']

fClass_window = [1, 3, 5, 7, 9, 11, 13, 16, 18, 20, 22, 24, 26,27]
fClass_aisle = [2, 4, 6, 8, 10, 12, 14, 15, 17, 19, 21, 23, 25]

bClass_window = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
bClass_aisle = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

eClass_window = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56]
eClass_aisle = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47,49, 51, 53, 55]

# USER-DEFINED FUNCTIONS
# Welcome Message Function
def welcome_message():
  default_rO = ""
  print()
  print()
  print("MAIN MENU")
  print()
  print("UCC Signature Express Limited")
  print("Arrive...ON TIME!")
  print()
  print("Reservation Options:")
  print(" First Class (F/f)")
  print(" Business Class (B/b)")
  print(" Economy Class (E/e)")
  print(" Quit (Q/q)")
  print(" Cancel (C/c)")
  return default_rO

#Receipt Function
def receipt(row_position, col_position,):
  phn_num_length = 10
  while True:
    print()
    print()
    print("USER INFORMATION")
    print()
    fname = input("First Name: ").title()
    lname = input("Last Name: ").title()

    while True:
      phn_num = input("Contact Number: ")

      #Remove non-digit characters from input
      phn_num = ''.join(char for char in phn_num if char.isdigit())

      #Checks if length of the filtered input is desired length
      if len(phn_num) == phn_num_length:
        phn_num = '-'.join([phn_num[:3], phn_num[3:6], phn_num[6:]])
        break

      else:
        print()
        print(f"Invalid phone number. Enter exactly {phn_num_length} digits")
        print()

    current_location = input("From Campus: ").upper()

    # Current Campus check
    while current_location not in campuses:
      print()
      print("Invalid Location! Please check the spelling and use the full name of the location (Mobay = Montego Bay).")
      current_location = input("From Campus: ").upper()

    destination = input("To Campus: ").upper()

    # Destination Campus check
    while destination not in campuses:
      print()
      print("Invalid Location! Please check the spelling and use the full name of the location (Mobay = Montego Bay).")
      destination = input("To Campus: ").upper()

    # Prevent same campus shuttling
    while destination == current_location:
      print()
      print("On campus shuttling is not supported.")
      destination = input("To Campus: ").upper()
      print()


    #Allows user to check the information then put in and correct it if needed
    print()
    print("RESERVATION CONFIRMATION")
    print()
    print(f"Name: {fname} {lname}")
    print(f"Contact number: {phn_num}")
    print(f"From Campus: {current_location}")
    print(f"To Campus: {destination}")
    print()
    confirm_reservation = input("Would you like to edit the above information? \nY for Yes / any key for No: ").upper()

    if confirm_reservation == 'Y':
      continue

    #Prints final recepit format
    else:
      print()
      print(f"RESERVING SEAT: {row_position} \nSEAT TYPE: {col_position}. \nPassenger: {fname} {lname}")
      print()
      print("RECEIPT")
      print("UCC Signature Express Limited")
      print("Arrive...ON TIME!")
      print()
      print(f"Reservation for: {fname} {lname}")
      print(f"Contact Number: {phn_num}")
      print(f"Seat Number: {row_position}")
      print(f"Seat Type: {col_position}")
      print(f"From Campus: {current_location}")
      print(f"To Campus: {destination}")
      print()
      print(f"Reservation Confirmed! Enjoy the ride {fname}.")
      break
  return

#Cancel Function
def cancel():
  global fClass_seats_reserved, bClass_seats_reserved, eClass_seats_reserved
  valid_cancel_option = ['F', 'B', 'E']
  print()
  print()
  print("CANCELLATION MENU")
  print()
  print("UCC Signature Express Limited")
  print("Arrive...ON TIME!")
  print()
  print("Reservation Options:")
  print(" First Class (F/f)")
  print(" Business Class (B/b)")
  print(" Economy Class (E/e)")
  print()
  reservation_option = input("Which class was the reservation made for?: ").upper() #Allows user to target a specific class to remove reservation from

  while reservation_option not in valid_cancel_option:
    print()
    print("Invalid input")
    reservation_option = input("Which class from the list above was the reservation made for?: ").upper()

  if reservation_option == 'F':
    print()
    print()
    print("First Class Reservation Cancellation")
    print()
    print("Reservation Made: First Class")

    #Checks if row position is integer
    while True:
      try:
        row_position = int(input("Please input reserved seat number: "))
        break
      except ValueError: #If not it tells the user it must be a number
        print()
        print("Seat number must be a number!")

    while True:
      #Checks if seat exists in first class
      if row_position > 27:
        print()
        print("Seat does not exist!")
        row_position = int(input("Please input reserved seat number: "))

      elif row_position <= 0: #Checks if the seat is valid
        print()
        print("Number must be positive or greater than zero!")
        row_position = int(input("Please input reserved seat number: "))

      else:
        #Checks if seat was reserved, if it isn't it returns to main menu
        if row_position not in fClass_seat_reservation_list:
          print()
          print("Seat was never reserved. Exiting to Main Menu...")
          return

        else:#if seat is reserved seat. Reservation will be cancelled
          print()
          print(f"CANCELLING RESERVATION  \nFirst Class Seat: {row_position}")
          fClass_seat_reservation_list.remove(row_position) #Removes seat from reserved list to make it available again
          fClass_seats_reserved -= 1 #Removes seat from reserved count
          print("Reservation cancelled. Seat is now available")
          break

  elif reservation_option == 'B':
    print()
    print()
    print("Business Class Reservation Cancellation")
    print()
    print("Reservation Made: Business Class")

    #Checks if row position is integer
    while True:
      try:
        row_position = int(input("Please input reserved seat number: "))
        break
      except ValueError: #If not it tells the user it must be a number
        print()
        print("Seat number must be a number!")

    while True:
      #Checks if seat exists in business class
      if row_position > 38:
        print()
        print("Seat does not exist!")
        row_position = int(input("Please input reserved seat number: "))

      elif row_position <= 0: #Checks if the seat is valid
        print()
        print("Number must be positive or greater than zero!")
        row_position = int(input("Please input reserved seat number: "))

      else:
        #Checks if seat was reserved, if it isn't it returns to main menu
        if row_position not in bClass_seat_reservation_list:
          print()
          print("Seat was never reserved. Exiting to Main Menu...")
          return

        else:#if seat is reserved seat. Reservation will be cancelled
          print()
          print(f"CANCELLING RESERVATION  \nBusiness Class Seat: {row_position}")
          bClass_seat_reservation_list.remove(row_position) #Removes seat from reserved list to make it available again
          bClass_seats_reserved -= 1 #Removes seat from reserved count
          print("Reservation cancelled. Seat is now available")
          break

  elif reservation_option == 'E':
    print()
    print()
    print("Economy Class Reservation Cancellation")
    print()
    print("Reservation Made: Economy Class")

    #Checks if row position is integer
    while True:
      try:
        row_position = int(input("Please input reserved seat number: "))
        break
      except ValueError: #If not it tells the user it must be a number
        print()
        print("Seat number must be a number!")

    while True:
      #Checks if seat exists in business class
      if row_position > 56:
        print()
        print("Seat does not exist!")
        row_position = int(input("Please input reserved seat number: "))

      elif row_position <= 0: #Checks if the seat is valid
        print()
        print("Number must be positive or greater than zero!")
        row_position = int(input("Please input reserved seat number: "))

      else:
        #Checks if seat was reserved, if it isn't it returns to main menu
        if row_position not in eClass_seat_reservation_list:
          print()
          print("Seat was never reserved. Exiting to Main Menu...")
          return

        else:#if seat is reserved seat. Reservation will be cancelled
          print()
          print(f"CANCELLING RESERVATION  \nEconomy Class Seat: {row_position}")
          eClass_seat_reservation_list.remove(row_position) #Removes seat from reserved list to make it available again
          eClass_seats_reserved -= 1 #Removes seat from reserved count
          print("Reservation cancelled. Seat is now available")
          #break
  return

#Quit Function
def quit():
  print()
  print("Exiting Program...")
  print()

  print(f"First Class \nTotal Number of Seats: {fClass_seat_total} \nNumber of Seats Reserved: {fClass_seats_reserved}")
  print()
  print(f"Business Class \nTotal Number of Seats: {bClass_seat_total} \nNumber of Seats Reserved: {bClass_seats_reserved}")
  print()
  print(f"Economy Class \nTotal Number of Seats: {eClass_seat_total} \nNumber of Seats Reserved: {eClass_seats_reserved}")
  print()
  return

#First Class Function
def firstClass():
  global fClass_seats_reserved
  print()
  print()
  print()
  print("FIRST CLASS BOOKING SYSTEM")
  print()
  print(f"Total amount of seats: {fClass_seat_total}")
  print(f"Number of seats reserved: {fClass_seats_reserved}")

  #Fully booked bus
  if fClass_seats_reserved == fClass_seat_total:
    print()
    print("All First Class seats are reserved, redirecting you to the Main Menu...")
    return

  else:
    print()
    fClass_seat_chart = tabulate(fc_seat_array, headers=['Window', 'Aisle', ' ', 'Aisle', 'Window'],tablefmt='grid') #To put the array into a grid table format
    print(fClass_seat_chart)
    print()
    col_position = input("Please indicate whether the reservation is for a 'Window' or 'Aisle' seat: ").upper()
    print()

    while col_position not in validCol_options: #Checks if seat position is valid
      print()
      print("Seat type does not exist! Please enter valid seat type: ")
      col_position = input("Please indicate whether the reservation is for a 'Window' or 'Aisle' seat: ").upper()

      #Displays respective seats based on reservation type
    if col_position == 'WINDOW':
      fClass_window_seats_array = tabulate(fc_window_seats_array, headers=['Right Side', ' ', 'Left Side'],tablefmt='grid')
      print()
      print("WINDOW SEAT CHART")
      print(fClass_window_seats_array)
      print()

    elif col_position == 'AISLE':
      fClass_aisle_seats_array = tabulate(fc_aisle_seats_array, headers=['Right Side', ' ', 'Left Side'],tablefmt='grid')
      print()
      print("AISLE SEAT CHART")
      print(fClass_aisle_seats_array)
      print()

    #Checks if input is valid
    while True:
      try:
        row_position = int(input("Please enter a seat number from the chart above: "))
        break

      except ValueError:
        print()
        print("Seat number must be a number!")

    while True:
      if row_position <= 0: #Checks if value enetered is a valid seat number
        print()
        print("Number must be positive or greater than zero! Please enter a valid seat number.")
        row_position = int(input("Please enter a seat number from the chart above: "))

      elif row_position > 27: #Checks if seat is on the bus
        print()
        print("Seat does not exist! Please enter a valid seat number.")
        row_position = int(input("Please enter a seat number from the chart above: "))

      #Checks if seat type corresponds with reservation type
      elif col_position == 'WINDOW' and row_position not in fClass_window:
        print()
        print("This is not a window seat!")
        row_position = int(input("Please enter a seat number from 'WINDOW SEAT CHART' above: "))

      #Checks if seat number corresponds with seat type
      elif col_position == 'AISLE' and row_position not in fClass_aisle:
        print()
        print("This is not an aisle seat!")
        row_position = int(input("Please enter a seat number from 'AISLE SEAT CHART' above: "))

      elif row_position in fClass_seat_reservation_list: #Checks if seat is already taken
        print()
        print("Seat already taken! Please choose another seat.")
        row_position = int(input("Please select another seat number: "))

      else:
        break

    #Adds seat position to a list, increases seats reserved and prints receipt
    receipt(row_position,col_position)
    fClass_seat_reservation_list.append(row_position)
    fClass_seats_reserved += 1

  return

#Business Class Function
def businessClass():
  global bClass_seats_reserved
  print()
  print()
  print()
  print("BUSINESS CLASS BOOKING SYSTEM")
  print()
  print(f"Total amount of seats: {bClass_seat_total}")
  print(f"Number of seats reserved: {bClass_seats_reserved}")

  #Fully booked bus
  if bClass_seats_reserved == bClass_seat_total:
    print()
    print("All Business Class seats are reserved, redirecting you to the Main Menu...")
    return

  else:
    print()
    bClass_seat_chart = tabulate(bc_seat_array, headers=['Window', 'Aisle', ' ', 'Aisle', 'Window'],tablefmt='grid') #To put the array into a grid table format
    print(bClass_seat_chart)
    print()
    col_position = input("Please indicate whether the reservation is for a 'Window' or 'Aisle' seat: ").upper()
    print()

    while col_position not in validCol_options: #Checks if seat position is valid
      print()
      print("Seat type does not exist! Please enter valid seat type: ")
      col_position = input("Please indicate whether the reservation is for a 'Window' or 'Aisle' seat: ").upper()

      #Displays respective seats based on reservation type
    if col_position == 'WINDOW':
      bClass_window_seats_array = tabulate(bc_window_seats_array, headers=['Right Side', ' ', 'Left Side'],tablefmt='grid')
      print()
      print("WINDOW SEAT CHART")
      print(bClass_window_seats_array)
      print()

    elif col_position == 'AISLE':
      bClass_aisle_seats_array = tabulate(bc_aisle_seats_array, headers=['Right Side', ' ', 'Left Side'],tablefmt='grid')
      print()
      print("AISLE SEAT CHART")
      print(bClass_aisle_seats_array)
      print()

    #Checks if input is valid
    while True:
      try:
        row_position = int(input("Please enter a seat number from the chart above: "))
        break

      except ValueError:
        print()
        print("Seat number must be a number!")

    while True:
      if row_position <= 0: #Checks if value enetered is a valid seat number
        print()
        print("Number must be positive or greater than zero! Please enter a valid seat number.")
        row_position = int(input("Please enter a seat number from the chart above: "))

      elif row_position > 38: #Checks if seat is on the bus
        print()
        print("Seat does not exist! Please enter a valid seat number.")
        row_position = int(input("Please enter a seat number from the chart above: "))

      #Checks if seat type corresponds with reservation type
      elif col_position == 'WINDOW' and row_position not in bClass_window:
        print()
        print("This is not a window seat!")
        row_position = int(input("Please enter a seat number from 'WINDOW SEAT CHART' above: "))

      #Checks if seat number corresponds with seat type
      elif col_position == 'AISLE' and row_position not in bClass_aisle:
        print()
        print("This is not an aisle seat!")
        row_position = int(input("Please enter a seat number from 'AISLE SEAT CHART' above: "))

      elif row_position in bClass_seat_reservation_list: #Checks if seat is already taken
        print()
        print("Seat already taken! Please choose another seat.")
        row_position = int(input("Please select another seat number: "))

      else:
        break

    #Adds seat position to a list, increases seats reserved and prints receipt
    receipt(row_position,col_position)
    bClass_seat_reservation_list.append(row_position)
    bClass_seats_reserved += 1

  return

#Economy Class Function
def economyClass():
  global eClass_seats_reserved
  print()
  print()
  print()
  print("ECONOMY CLASS BOOKING SYSTEM")
  print()
  print(f"Total amount of seats: {eClass_seat_total}")
  print(f"Number of seats reserved: {eClass_seats_reserved}")

  #Fully booked bus
  if eClass_seats_reserved == eClass_seat_total:
    print()
    print("All Economy Class seats are reserved, redirecting you to the Main Menu...")
    return

  else:
    print()
    eClass_seat_chart = tabulate(ec_seat_array, headers=['Window', 'Aisle', ' ', 'Aisle', 'Window'],tablefmt='grid') #To put the array into a grid table format
    print(eClass_seat_chart)
    print()
    col_position = input("Please indicate whether the reservation is for a 'Window' or 'Aisle' seat: ").upper()
    print()

    while col_position not in validCol_options: #Checks if seat position is valid
      print()
      print("Seat type does not exist! Please enter valid seat type: ")
      col_position = input("Please indicate whether the reservation is for a 'Window' or 'Aisle' seat: ").upper()

      #Displays respective seats based on reservation type
    if col_position == 'WINDOW':
      eClass_window_seats_array = tabulate(ec_window_seats_array, headers=['Right Side', ' ', 'Left Side'],tablefmt='grid')
      print()
      print("WINDOW SEAT CHART")
      print(eClass_window_seats_array)
      print()

    elif col_position == 'AISLE':
      eClass_aisle_seats_array = tabulate(ec_aisle_seats_array, headers=['Right Side', ' ', 'Left Side'],tablefmt='grid')
      print()
      print("AISLE SEAT CHART")
      print(eClass_aisle_seats_array)
      print()

    #Checks if input is valid
    while True:
      try:
        row_position = int(input("Please enter a seat number from the chart above: "))
        break

      except ValueError:
        print()
        print("Seat number must be a number!")

    while True:
      if row_position <= 0: #Checks if value enetered is a valid seat number
        print()
        print("Number must be positive or greater than zero! Please enter a valid seat number.")
        row_position = int(input("Please enter a seat number from the chart above: "))

      elif row_position > 56: #Checks if seat is on the bus
        print()
        print("Seat does not exist! Please enter a valid seat number.")
        row_position = int(input("Please enter a seat number from the chart above: "))

      #Checks if seat type corresponds with reservation type
      elif col_position == 'WINDOW' and row_position not in eClass_window:
        print()
        print("This is not a window seat!")
        row_position = int(input("Please enter a seat number from 'WINDOW SEAT CHART' above: "))

      #Checks if seat number corresponds with seat type
      elif col_position == 'AISLE' and row_position not in eClass_aisle:
        print()
        print("This is not an aisle seat!")
        row_position = int(input("Please enter a seat number from 'AISLE SEAT CHART' above: "))

      elif row_position in eClass_seat_reservation_list: #Checks if seat is already taken
        print()
        print("Seat already taken! Please choose another seat.")
        row_position = int(input("Please select another seat number: "))

      else:
        break

    #Adds seat position to a list, increases seats reserved and prints receipt
    receipt(row_position,col_position)
    eClass_seat_reservation_list.append(row_position)
    eClass_seats_reserved += 1

  return

#Reservation Booking System
while True:
  #Main Menu
  print(welcome_message())
  print()
  reservation_option = input("Please select an option: ").upper()

  #First Class Option
  if reservation_option == 'F':
    firstClass()

  #Business Class Option
  elif reservation_option == 'B':
    businessClass()

  #Economy Class Option
  elif reservation_option == 'E':
    economyClass()

  #Cancel Option
  elif reservation_option == 'C':
    cancel()

  #Quit Option
  elif reservation_option == 'Q':
    quit()

  else:
    print("Invalid Option!")
    print()