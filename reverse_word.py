#reverse string
text = input("Enter text: ")

#fully reverses a string 
def reverse_string(text):
    return text[::-1]
  
#just change the word order in reverse order
def reverse_words(text):
    return " ".join(reversed(text.split()))

print(reverse_string(text))
print(reverse_words(text))
