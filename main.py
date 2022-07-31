import DBFunction as DBFunction

def main():
    db = DBFunction.DBFunction()
    db.getOLV(["tek"])
    db.getArticoli(["tek"])
    db.getEvasi(["tek"])
    db.getDaEvadere(["tek"])
    print('Done')
if __name__ == "__main__":
    main()