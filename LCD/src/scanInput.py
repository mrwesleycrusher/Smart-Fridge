

class scannerInput():

    def __init__(self):
        print "Scanner done"

    def scanForCode(self):
        try:
            code = raw_input("Enter code: ")
            return code;    

        except KeyboardInterrupt:
            print "Failed Read"
        
# q = scannerInput()
# bc = q.scanForCode()
# print bc