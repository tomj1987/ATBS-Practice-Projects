'''

 Chapter 4 - Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
 and a space, with and inserted before the last item. For example, passing the previous spam list to the function would
  return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
   Be sure to test the case where an empty list [] is passed to your function.

'''


names = ['thomas', 'hunter', 'frankie']


def comma(my_list):
    output = ''
    if len(my_list) == 0:
        print('Not a valid list.')  # Returns an error statement if an empty ist is entered.
    for x in range(len(my_list)):
        if len(my_list) - 1 == x:
            output += f"and {my_list[x]}."  # Find last item in the list and puts 'and' before it.
        elif len(my_list) - 2 == x:
            output += f"{my_list[x]} "  # Second from last item in the list is followed by 'and', so no comma.
        else:
            output += f"{my_list[x]}, "  # All other items in the list are separated by commas.
    return output


result = comma(names)
print(result)