# escher
A self-writing program, like  M.C. Escher's "Drawing Hands"; completely unsupervised
https://en.wikipedia.org/wiki/Drawing_Hands

https://upload.wikimedia.org/wikipedia/en/b/ba/DrawingHands.jpg

![](https://upload.wikimedia.org/wikipedia/en/b/ba/DrawingHands.jpg)

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

## Initial Results
After 1000 tries, all it did was make a program that was almost all "commented out" with the pound symbol, something many coders learn on their first day of coding. There are thousands of commented out (non-functioning) characters except for the number 8 and the number .8. 

This is pretty interesting.
But also... not really. Very sloppy coding mister! ... and it doesn't do anything except pass 8 and .8...
I'm wondering if I should not allow it to use "#" to help encouragage it to make something which actually does something, and make it easier for me to figure out what it is doing...

I'd rather not give it any rules... stay tuned

![](results1000.png)

For now, I just think it is funny that you can actually copy and paste this rediculous, messy, nonsensical txt made from this Escher program and run it and it works! It doesn't print anything or do anything, but it doesn't fail either, which in a way, makes it a better programmer than me. I deal with errors all the time, but in about 1 second, it was able to write error-free code!
