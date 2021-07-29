# main assembler code
import sys

from Lexer import Lexer
from SyntaxChecker import SyntaxChecker
from SemanticsAnalyser import SemanticsAnalyser


def main():
	lexer = Lexer()
	syntaxChecker = SyntaxChecker()
	semanticsAnalyser = SemanticsAnalyser()
	
	for line_num, line in enumerate(sys.stdin, 1):
		if(not line.isspace()):
			tokens = lexer.tokenize(line_num, line)
			sentenceType = syntaxChecker.parse(line_num, tokens)
			frontendPass = semanticsAnalyser.isValid(line_num,sentenceType, tokens)

if __name__ == '__main__':
	main()