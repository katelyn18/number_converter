
'''
one, two, three, four, five, six, seven, eight, nine, ten
eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
twenty, thrity, fourty, fifty, sixty, seventy, eighty, ninety,
hundred, thousand
'''
less_than_twenty = {
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen"
}

less_than_hundred = {
		2: "twenty",
		3: "thirty",
		4: "forty",
		5: "fifty",
		6: "sixty",
		7: "seventy",
		8: "eighty",
		9: "ninety"
}

message = "Enter a number between 1 and 9999: "
user_input = input( message )
#size = len(user_input)
english = ""

def less_twenty( val ):
	for num in less_than_twenty:
		if val == num:
			return less_than_twenty[num]
	return ""

def less_hundred( val ):
	for num in less_than_hundred:
		if val == num:
			return less_than_hundred[num]
	return ""



if user_input < 20: #10-19
	english += less_twenty( user_input )
elif user_input >= 20 and user_input < 100: #20-99
	english += less_hundred( user_input/10 ) + " " + less_twenty( user_input%10 )
elif user_input >= 100 and user_input < 1000: #100-999
	take_away = user_input - ( (user_input/100) * 100 )
	english += less_twenty( user_input/100 ) + " hundred "
	if take_away < 20:
		english += less_twenty( take_away ) + " "
	elif take_away >= 20 and take_away < 100:
		english += less_hundred( take_away/10 ) + " " + less_twenty( take_away%10 )
elif user_input >= 1000 and user_input <10000:	#1,000-9,999
	take_away = user_input - ( (user_input/1000) * 1000 )
	take_away2 = take_away - ( (take_away/100) * 100 )
	english += less_twenty( user_input/1000 ) + " thousand "
	if take_away != 0:
		english += less_twenty( take_away/100 ) + " hundred "
	if take_away2 < 20:
		english += less_twenty( take_away2 ) + " "
	elif take_away2 >= 20 and take_away2 < 100:
		english += less_hundred( take_away2/10 ) + " " + less_twenty( take_away2%10 )



print( english )













#
