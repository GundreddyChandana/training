#create a list of 3 spam words and take the user input check the spam words in user input if the msg is spam print true if the msg is not spam print false and also what are the spam words in user input  ["win","cash","free"]
#input:"you are wining a free price now!"
#output: true , false

def spam_detector(message, spam_words):
    # Convert to lowercase
    message_lower = message.lower()
    
    # Find spam words in message
    found_spam_words = []
    for spam_word in spam_words:
        if spam_word in message_lower:
            found_spam_words.append(spam_word)
    
    # Check if spam
    is_spam = len(found_spam_words) > 0
    
    return is_spam, found_spam_words

# Test
spam_words = ["win", "cash", "free"]
user_input = "you are wining a free price now!"

is_spam, found_words = spam_detector(user_input, spam_words)
print(f"Is Spam: {is_spam}")
print(f"Spam words found: {found_words}")
