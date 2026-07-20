try:
    num = int(input("Enter Number"));
    result = 10/num
    print(result);
except Exception as e:
    print("error")
finally:
    print("execute complete")
    
