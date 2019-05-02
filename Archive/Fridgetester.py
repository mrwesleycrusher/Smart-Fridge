from barcodeProcessing.Food import Foodstuff

def main():
    # ATM I'm just manually gatting barcode data to test the API
    meme = Foodstuff('5705831011120')
    print(meme.get_name())

if __name__ == '__main__':
    main()