def alt_caps(original_string):
    
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """

    y=0
    new_string=original_string 
    original_string="omer is crazy" 
    for character in new_string: 
        if y%2 == 0: #even
            string=character.upper()
            print(string)
        if y%2 == 1: #odd
            string=character.lower()
            print(string)
        y=y+1
        
            
        #     new_string.upper()
        #     print(character)
        # y=y+1


        
        
        
     #   new_string = new_string.upper()
    # YOUR CODE HERE
 
    

    return new_string

print(alt_caps("Alternating Capitalization"))
#for i, character in enumerate(original_string)


        