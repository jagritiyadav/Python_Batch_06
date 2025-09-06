for num in range(2, 200):
   
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:   
        if num == 13:
            continue   
        if num == 59:
            print("Encountered 59, exit program")
            break    
        print(f"Square of {num} = {num**2}")
