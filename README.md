# xsacks
A crossed substitution alphabetical cipher with secured key

# The sources

Please note that the python implementation is still WiP (actually it works but miss some checks and features)

You can import the xsacks.py module and use xsacks.cipher(msg, key, securekey) and xsacks.decipher(msg, key, securekey).

If you modify xsacks.py, you can run a cipher-decipher test directly from the module, so to be sure you didn't screw things up.

# X-SACK 

This cipher is based on crossed substitution of the message and on simple substitution of the key. Let’s explain it with an example. 

Our message is: msg = “Attack now” 

Our key is: key=”secret” 

Our secure-key (you’ll see the meaning later) is: skey=”cryp” 


Before starting, you have to assign to each letter of the alphabet (and also to numbers and symbols if you use them) a number. In a software, it could be the ASCII value of the character. Let’s use a simple one as example, though it’s a valid one.


0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ ? . 

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 

First of all, you need to split msg separating each letter: 

a t t a c k _ n o w 

NOTE: space is a valid character, so i used “_” just to show it 

Now substitute to each letter its number:

10 29 29 11 13 20 36 23 24 32 

You’ll do the same thing with the key: 

s e c r e t

28 14 12 27 14 29


Now you have to split the key in two parts: 


s e c | r e t

28 14 12 | 27 14 29 

Time to substitute! 

To perform a cross substition, add to the first msg value the first key value of the first group (a+s), then add to the second msg value the first key value of the second group (t+r), continue adding to the third msg value the second key value of the first group, then to the fourth msg value the second key value of the second group and so on. 


Restart from the beginning if the key ends.

Now you should reconvert numbers to letters. If the number exceed the limit of your alphabet, simple start counting from the beginning.

Let’s decode: 

10 28 15 34 35 21 36 22 20 18 

A S F Y Z L _ M K I 

The encrypted message is: ASFYZL_MKI 

Though is really hard to decode the message without having the key, even having a large amount of text, the last step is to encode also the key, with the secure key. 
The steps are almost the same, but you don’t have to split the secure key. Simple substitute, check the values and then reconvert. 

S E C R E T

28 14 12 27 14 29

C R Y P C R

12 27 34 25 12 27 40

So, the encoded key is: 238EQI 

The only way to decrypt the message is having the msg, the encoded key and the secure key, or the plain key if you are so dumb to give the plain one. 

Give to your friend: 

ASFYZL_MKI 

238EQI 

CRYP 



And he will be able to read “attack now”. 


