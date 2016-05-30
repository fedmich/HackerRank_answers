'''
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
'''

def solution(a ):
	return a.swapcase()

if __name__ == "__main__":
	s = raw_input()
	answer = solution( s )
	print ( answer )