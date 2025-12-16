# PROBLEM 8
# Write a script that can open a text file and look through each line of text to discover consecutively doubled words. It should write the results that it discovers to an output file. For example, if line 15 of my text is "The cat jumped over the the chair.", then the occurs twice consecutively, beginning at character 20. Thus the output file should have a line like
# 15, the, 20
# or some format that you think makes sense. Some helpful methods are string.split() and string.lower().

def findDoubledWords(txtFile, output):

# Open text file, I learned this from here --> https://www.geeksforgeeks.org/python/reading-writing-text-files-python/
    with open(txtFile,"r") as text, open(output, "w") as outputFile:
        #Write the header of our output file
        outputFile.write("Line, Word, Characther Position \n")

        for lineNumber, line in enumerate(text, start=1):
            # Split each line into words
            words = line.split()

            # Check for consecutive pair of words, I substract -1 to not go out of bounds on my last loop iteration
            for i in range(len(words) -1):
                # Actually compare the words, and ignore case
                if words[i].lower() == words[i + 1].lower():
                    word = words[i].lower()

                    # Now find where our consecutive word starts at, we'll do this by first building up to our word, inclduing the first word from the two words that are repeated
                    textBeforeWord = "".join(words[:i+1])
                    # Our second word should start right after this plus a space
                    position = len(textBeforeWord) + 1

                    # Now we write out our result!  (Yes, I've started using f to format my writing or printing our outputting, adding up strings was too much of a pain)
                    outputFile.write(f"{lineNumber}, {word}, {position}\n")

# Get the file names from the user
inputFile = input("Enter the input file name: ")
outputFile = input("Enter the output file name: ")

# Actually run the function
findDoubledWords(inputFile,outputFile)
print(f"Done! Results in {outputFile}")


# TESTING
### Expected Output if using test.txt:
# Line, Word, Character Position
# 2, the, 24
# 3, really, 9
# 4, that, 10
# 5, we, 10
# 7, you, 5
# 7, the, 20

