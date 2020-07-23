#Method to get two digit decimals
def get_two_decimal_rounded(input_float_string):
    output_value = input_float_string #Worst case
    try:
        count = input_float_string.count(".")
        if count==1:
            decimal = input_float_string.split(".")[-1]
            if len(str(decimal))>1:
                output_value = str('%.2f'%float(input_float_string))
            else:
                output_value = input_float_string+"0"
        elif count == 0:
            output_value = input_float_string+".00"
    except Exception as err:
        pass
    return output_value
