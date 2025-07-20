import sys

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
def word_count():
	 words = get_book_text(sys.argv[1]).split()
	 print(f"Found {len(words)} total words")
	 ### for the previous module's response:
	 ### print(get_book_text("WEBSITE"))

word_count()

print("--------- Character Count -------")
def letters():
	letter_count = {}
	lower_case = get_book_text(sys.argv[1]).lower()
	for lower in lower_case:
		if lower in letter_count and lower.isalpha() == True:
			letter_count[lower] += 1
		if lower not in letter_count and lower.isalpha() == True:
			letter_count[lower] = 1
	sorted_lower = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
	for sort in sorted_lower:
		print (f"{sort}: {sorted_lower[sort]}")

letters()

print("============= END ===============")

"""
def letters():
	letter_count = {}
	lower_case = get_book_text(sys.argv[1]).lower()
	for lower in lower_case:
		if lower in letter_count:
			letter_count[lower] += 1
		else:
			letter_count[lower] = 1
	print(letter_count)
"""
	

