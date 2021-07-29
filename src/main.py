# main assembler code
from Lexer import Lexer
import sys


def main():
	lexer = Lexer()
	for line_num, line in enumerate(sys.stdin):
		print(line.strip("\n"))
		tokens = lexer.tokenize([line_num, line])
		print(tokens)

if __name__ == '__main__':
	main()