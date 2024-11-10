#Aaryan Karn
#creating variables to each types  of data
my_int=19
my_float=5.11
my_name="Aaryan Karn"
my_boolean=True


#Arithmetic operations and string catenations 
int_result=my_int + 1
float_result=my_float * 2
string_result=my_name + " is a good boy"


#creating a dictionary  to store the results
result_dict={
    "Integer Result":int_result,
    "Float Result":float_result,
    "String Result":string_result
}

#Displaying the output 
print(result_dict)
for data_type, values in result_dict.items():
    print(f"{data_type}: {values}")

