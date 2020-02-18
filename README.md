# WordListHelperScripts
A collection of python scripts that aid in the creation of word list permutations

*IF you are running this on Windows and want to output the information to be used with John The Ripper, you need to output in UTF-8 in order to do this you should use  "| out-file myWordList.txt -encoding utf8" For example:*
```
PS C:\YourFolder> python .\inOrderPermutationsOfNLists.py .\List_1.txt .\List_2.txt | out-file CombinedWordList.txt -encoding utf8
```

## Prerequisites

Tested on Ubuntu 18.04 using Pyton 3 (3.5.1)
```
apt -y install python3
```

## Word Lists

I use the following word lists in my examples below.

Each line counts as 1 word. 

```
wordlist1.txt           wordlist2.txt           wordlist3.txt
AAA                     111                     aaa
BBB                     222                     bbb
CCC                     333                     ccc
```

## inOrderPermutationsOfNLists.py

Generates all permutations of N word lists where wordlist 1 is slot 1, wordlist 2 is slot 2, ...

attributes are any number of word lists. The permutation length is the nubmer of word lists. 

```
Use:
python .\inOrderPermutationsOfNLists.py wordlist1.txt wordlist2.txt wordlist3.txt 

Result:
AAA111aaa
AAA111bbb
AAA111ccc
AAA222aaa
AAA222bbb
AAA222ccc
AAA333aaa
AAA333bbb
AAA333ccc
BBB111aaa
BBB111bbb
BBB111ccc
BBB222aaa
BBB222bbb
BBB222ccc
BBB333aaa
BBB333bbb
BBB333ccc
CCC111aaa
CCC111bbb
CCC111ccc
CCC222aaa
CCC222bbb
CCC222ccc
CCC333aaa
CCC333bbb
CCC333ccc
```
```
Use:
python .\inOrderPermutationsOfNLists.py wordlist1.txt wordlist2.txt

Result:
AAA111
AAA222
AAA333
BBB111
BBB222
BBB333
CCC111
CCC222
CCC333
```

## allPermutations.py

Generates all permutations in a word list

Attributes are a word list and the permutation length.

```
use: 
python .\allPermutations.py wordlist1.txt 3

retult:
AAABBBCCC
AAACCCBBB
BBBAAACCC
BBBCCCAAA
CCCAAABBB
CCCBBBAAA
```
```
use: 
python .\allPermutations.py wordlist1.txt 2

retult:
AAABBB
AAACCC
BBBAAA
BBBCCC
CCCAAA
CCCBBB
```

## inOrderPermutationsOfNListsWithMask.py

Generates all permutations of N word lists where wordlist 1 is slot 1, wordlist 2 is slot 2, ...

attributes are any number of word lists. The permutation length is the nubmer of word lists. 

?d and ?s are wildcards for files that produce numbers and symbols. It is just like defining files yourself, but they are built in.

```
?d = 0,1,2,3,4,5,6,7,8,9
?s = !,@,#,$,%,^,&,*,(,),_,-,+,=,{,},[,],\,|,?,",<,>,:,;,.,/,,
```

```
Use:
python .\inOrderPermutationsOfNListsWithMask.py wordlist1.txt ?d 

Result:
AAA0
AAA1
AAA2
AAA3
AAA4
AAA5
AAA6
AAA7
AAA8
AAA9
BBB0
BBB1
BBB2
BBB3
BBB4
BBB5
BBB6
BBB7
BBB8
BBB9
CCC0
CCC1
CCC2
CCC3
CCC4
CCC5
CCC6
CCC7
CCC8
CCC9
```
```
Use:
python .\inOrderPermutationsOfNLists.py ?d ?s

Result:
0!
0@
0#
0$

<Lots more>

9;
9.
9/
9,
```

