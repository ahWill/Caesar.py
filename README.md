# Caesar.py
attempt at making an interactive Caesar cipher in Python

This is my first "just because" project that I wanted to have a second attempt at. 
I liked the idea of ciphers, and was starting to learn about them from my exposure to Cicada 3301, which is an interesting topic.
In short, I like puzzles, I'm not the best, but it's fun to challenge myself and I feel good completing this. 

```
python caesar.py
```

it will then launch an "interactive" cipher which you specify in the format of 

```
[left/right] [1-26] [string_to_cipher]
```

on a blank new line.

Returns a ciphered string, which funny enough also unciphers a ciphered string. Anyways. 

***The output shifts the spaces to be the mirror of the input see Example 2***


Commands
--------
```
break         same as exit, breaks the program (safely)
clear         clears screen and resumes waiting for input
exit          same as break, exits the program (safely)
help          a help message similar to this.
```



"Encrypt"
---------
```
Example 1:    right 15 this is my test
Return:       iwxh xh bn ithi


Example 2:    left 15 another fun test oh boy
Return:       lyz es pcqf yep dezsmzj
```




"Decrypt"
---------
```
Example 1:    left 15 iwxh xh bn ithi
Return:       this is my test

Example 2:    right 15 lyz es pcqf yep dezsmzj
Return:       another fun test oh boy
```
