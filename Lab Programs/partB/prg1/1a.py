def remove_dups(lis): #function to remove duplicates
	res = []
	for i in lis:
		if i not in res:
			res.append(i)
	return res	



n  = int(input("Enter number of elements : "))
ls = []

for i in range(n):
	i = input("Enter element : ")
	ls.append(i)
print("\nEntered elements are : ")
print(ls)
new_ls = remove_dups(ls)

print("\nList without duplicates :")
print(new_ls)

even_ls = [x for x in range(n) if x%2 == 0]#making even numbers list using list comprehension
print("\nList of even numbers using list comprehension :\n" , even_ls)

rev_lis = ls
rev_lis.reverse()

print("\nReversed List of elements : ")
print(rev_lis) #printing elements in reverse