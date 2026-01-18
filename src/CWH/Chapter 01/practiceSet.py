# Print Poem: Twinkle Twinkle Little Star
print('''
Twinkle twinkle little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
      ''')

# Text to Speech Conversion
import pyttsx3
engine = pyttsx3.init()
engine.say('Twinkle twinkle little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.')
engine.runAndWait()

#Print the contents of this directory
import os
print("Contents of the current directory:")
print(os.listdir('.'))

for item in os.listdir('.'):
    print(item)