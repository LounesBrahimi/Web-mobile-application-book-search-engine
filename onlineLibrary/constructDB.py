import urllib.request

def contructDB(bookId: int, sizeDB: int, minNumberWords: int):
    numberBooksStocked : int = 0
    while (numberBooksStocked < sizeDB):
        bookIdStr = str(bookId)
        try:
            with urllib.request.urlopen("https://gutenberg.org/files/"+bookIdStr +"/"+
                                bookIdStr+"-h/"+bookIdStr+"-h.htm") as url:
                textBook : str = url.read().decode('utf-8')
                print(len(textBook))
        except:
            pass
        numberBooksStocked += 1
        bookId += 1

        


sizeDB : int = 1664
minNumberWords : int = 10006
bookInitialId : int = 56672
contructDB(bookInitialId, sizeDB, bookInitialId)