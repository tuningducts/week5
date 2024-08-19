def book_quantity():
    try:
         bq = int(input("enter quantity of books purchased: "))
    except:
        print("Please enter and integer")
        return book_quantity()
    if bq >= 0:
        return bq
    else:
        print(f"{bq} is an invalid argument. quantity must be an integer >= 0")
        return book_quantity()

ranges = [{"points":5,"lower":2,"upper":3},{"points" :15,"lower":4,"upper":5},{"points": 30,"lower":6,"upper":7}, {"points": 60,"lower":8}]

def get_points(quantity: int):
    q = quantity
    if q == ranges[0]["lower"] or q == ranges[0]["upper"]:
        return ranges[0]["points"]
    elif q == ranges[1]["lower"] or q == ranges[1]["upper"]:
        return ranges[1]["points"]
    elif q == ranges[2]["lower"] or q == ranges[2]["upper"]:
        return ranges[2]["points"]
    elif q >= ranges[3]["lower"]:
        return ranges[3]["points"]
    else:
        return 0
    
    
print(get_points(book_quantity()))
