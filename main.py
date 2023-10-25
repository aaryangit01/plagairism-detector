from difflib import SequenceMatcher 

with open('doc1.txt') as first_file, open('doc2.txt') as second_file: 
	
	file1 = first_file.read()  #reading both files
	file2 = second_file.read() 
	
	ab = SequenceMatcher(None, file1, file2).ratio() # Comparing Both Text Files 
	
	result = int(ab*100) 
	print(f"{result}% Plagiarized Content") 
