from bisect import bisect_left, bisect_right # for binary search
import random

random.seed(77) # so that you and I get same random lists

a = [1, 2, 3, 3, 3, 4, 5]
print(bisect_left(a, 3))  # 2 (position to put 3)
print(bisect_right(a, 3)) # 5 (position to put 5)

# isect.bisect_left(a,	x): Leftmost offset where we can
# insert x into a to maintain sorted order. a is already sorted!
# bisect.bisect_right(a,	x): Like bisect_left, but
# returning rightmost instead of leftmost offset


# We can straightforwardly use binary search to fidnd a range of
# elements in a sorted list that equal some query:

strls	=	['a',	'awkward',	'awl',	'awls',	'axe',	'axes',	'bee']
#	Get	range	of	elements	that	equal	query	string	‘awl’
st,	en	=	bisect_left(strls,	'awl'),	bisect_right(strls,	'awl')
print(st,	en)	#	output:	(2,	3)

# Can also use binary search to "nd a range of elements in a
# sorted list with some query as a pre!x:

strls	=	['a',	'awkward',	'awl',	'awls',	'axe',	'axes',	'bee']
#	Get	range	of	elements	with	‘aw’	as	a	prefix
st,	en	=	bisect_left(strls,	'aw'),	bisect_left(strls,	'ax')
print(st,	en)	#	output:	(1,	4)