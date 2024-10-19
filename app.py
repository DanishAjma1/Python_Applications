# Here is the Shares calculator used for calculate the share for sons and daughter from the total inheritance amount..

#This is the main file of this application..
import SharesCalculation as cal

try:    #to handle the error
    inheritance_amount = float(input("Enter the total inheritance amount that a men leave after deceased..?(float) "))     # get the inherited amount
    sons = int(input("How much sons he have..?(int) "))    #sons eligible for the inherited amount
    daughters = int(input("How much daughters he have..?(int) "))      #daughters eligible for the inherited amount
    wifes= input("Does his spouse alive..? y for yes n for no : ")

    wife = 0
    if wifes == "y":
        wife = int(input("how much wives he have..? "))

    mother= input("Does his mother alive..? y for yes n for no : ")
    father= input("Does his father alive..? y for yes n for no : ")

    cal.calculate(inheritance_amount,sons, daughters,mother, father, wife)    #function...

    sons = int(sons)  # check either the sons and the following variables are integer?
    daughters = int(daughters)
    inheritance_amount = int(inheritance_amount)
    wife= int(wife)

except ValueError:      #Catch block
    print("The values must be an int or float!")
    exit()  #exit the application
