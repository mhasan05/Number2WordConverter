list_01 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]  
list_02 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]  
list_03 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
list_04 =["", "", "", "", "Hundred", "Thousand", "Lac", "Million", "Billion", "Trillion"]
def convert_to_words(num):
    if num == 0:  
        return "zero"  
    elif num< 0:  
            return "minus " + convert_to_words(abs(num))  
    elif num< 10:  
            return list_01[num]
    elif num< 20:  
            return list_02[num - 10]  
    elif num< 100:  
            return list_03[num // 10] + (" " + convert_to_words(num % 10) if num % 10 != 0 else "")
    elif num< 1000: 
            return list_01[num // 100] +" "+ list_04[4] + (" " + convert_to_words(num % 100) if num % 100 != 0 else "")  
    elif num>= 1000 and num < 100000:  
            return convert_to_words(num // 1000) + " "+ list_04[5] + (" " + convert_to_words(num % 1000) if num % 1000 != 0 else "")  
    elif num>= 100000 and num<1000000:
            return list_01[num // 100000] + " "+ list_04[6] + (" " + convert_to_words(num % 100000) if num % 100000 != 0 else "")
    elif num>= 1000000 and num<1000000000:
            return convert_to_words(num // 1000000) + " "+ list_04[7] + (" " + convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
    elif num>= 1000000000 and num<1000000000000:  
            return convert_to_words(num // 1000000000) + " "+ list_04[8] + (" " + convert_to_words(num % 1000000000) if num % 1000000000 != 0 else "")
    elif num>= 1000000000000:  
            return convert_to_words(num // 1000000000000) + " "+ list_04[9] + (" " + convert_to_words(num % 1000000000000) if num % 1000000000000 != 0 else "") 
    else:  
        return "Number out of range"  
def number_to_words(num):
    get_num = str(num).split('.')
    
    try:
        num = int(get_num[0])
        get_paysa = int(get_num[1])
    except:
        num =int(num)
        get_paysa=0  
    try:
        if get_paysa == 0:
                taka = convert_to_words(num)
                paysa = convert_to_words(get_paysa)
                words = f"{taka} Taka Only"
        else:
                taka = convert_to_words(num)
                paysa = convert_to_words(get_paysa)
                words = f"{taka} Taka and {paysa} paysa Only"
    except:
        words = "Invalid Number"
    
    return words
    
    
num = input("Enter Number: ")
words = number_to_words(num)
print(words)
