# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name("atharva", "shinde"))

def function1(text):
    return text+text

def function2(text):
    return text.title()

output = function2(function1("hello"))
print(output)

#return is the end of the function anything written after it does not get executed