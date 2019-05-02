from RPi import GPIO
import time

#######################################
#               scannerInput
#Opens a text field in the terminal
#and reads in a code
#REQUIRES THE TERMINAL BE FOCUSED WHEN READING
#######################################
class scannerInput():

    def __init__(self):
        print("Scanner up")

    ###################################
    #           scanForCode
    #Focuses the text field and allows
    #allows scanner to input code
    #Returns: Code
    ###################################
    def scanForCode(self):
        try:
            code = input("Enter code: ")
            return code;    

        except KeyboardInterrupt:
            print("Failed Read")

    ###################################
    #           getAddState
    #Returns if button is in add state
    #True(1): button is in add state
    #False(0): button is in subtract state
    ###################################
def getAddState(self):
    pass
        

#Quick test code
# q = scannerInput()
# bc = q.scanForCode()
# print bc
# while True:
#     state = q.getAddState()
#     print state
#     time.sleep(0.2)

