from models import (Base, session,
                    Book, engine)
# main menu - add, seaarchc, analysis, exit, view

# add books to thee database
# edit books
# delete books
# searchc books
# data cleaning
# loop runs program


if __name__ == '__main__':
    Base.metadata.create_all(engine)
