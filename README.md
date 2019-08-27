# WordListHelperScripts
A collection of python scripts that aid in the creation of word list permutations


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

## Word Lists

Each line counts as 1 word. 

My examples use the following word lists: 

wordlist1.txt 
```
AAA
BBB
CCC
```

wordlist2.txt 
```
111
222
333
```

wordlist3.txt
```
aaa
bbb
ccc
```
