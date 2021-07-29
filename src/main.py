# main assembler code
import sys

from Lexer import Lexer
from SyntaxChecker import SyntaxChecker


def main():
	lexer = Lexer()
	syntaxChecker = SyntaxChecker()
	
	for line_num, line in enumerate(sys.stdin, 1):
		tokens = lexer.tokenize(line_num, line)
		sentenceType = syntaxChecker.parse(line_num, tokens)
		if(sentenceType):
			print(line.strip("\n"), "TYPE:", sentenceType)

if __name__ == '__main__':
	main()