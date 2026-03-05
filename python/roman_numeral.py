

def romanNumeral(string):
    roman = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
             }
    num = 0
    for i in range(len(string)-1):
        if roman[string[i]] < roman[string[i+1]]:

            num -=  roman[string[i]]
        else:
            num += roman[string[i]] 
        
    return num + roman[string[-1]]



    # roman = {
    #             'I': 1,
    #             'V': 5,
    #             'X': 10,
    #             'L': 50,
    #             'C': 100,
    #             'D': 500,
    #             'M': 1000
    #          }
    # mark = 0
    # num = 0
    # for char in string:
    #     if roman[char] > mark:
    #         num = roman[char] - 2*mark
    #     else:
    #         num = num + roman[char]
    #     mark = roman[char]
    # return num



# if (require.main === module) {
#   // add your own tests in here
#   console.log("Expecting: 1");
#   console.log(romanNumeral('I'));

#   console.log("");

#   console.log("Expecting: 9");
#   console.log(romanNumeral('IX'));

#   console.log("");

#   console.log("Expecting: 402");
#   console.log(romanNumeral('CDII'));
# }

# module.exports = romanNumeral;

# Please add your pseudocode to this file
# And a written explanation of your solution
