# escher
A self-writing program, like  M.C. Escher's "Drawing Hands"; completely unsupervised
https://en.wikipedia.org/wiki/Drawing_Hands

https://upload.wikimedia.org/wikipedia/en/b/ba/DrawingHands.jpg

# Goal
1) To find out: Can a program write itself completely unsupervised?
2) Give me an excuse to add more to github

# Initial Setup
First, I created a text file, hello_world.txt that is just a text file which has an "a" and that's it.
I use python packages "random" and to randomly grab characters from the package "string".

## Procedure
1) The program reads in hello_world.txt
2) It deletes the last character, and then adds 10 random characters.
3) It checks if what it just made is a runnable python program
4) If no, it keeps trying 2-3, if yes, it saves it
4) repeat

First, I set it up to go through 1000 cycles. One could also change it to be a 'while loop' which infinitely adds onto the program
