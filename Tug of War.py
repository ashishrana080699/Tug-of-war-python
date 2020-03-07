def main():
	num=[]
	weight=[]
	test=int(input())
	for t in range(test):
		n=int(input('\n'))
		num.append(n)
		weight+=[int(input()) for i in range(n)]
		if t==(test-1):
			print('')
	for t in range(test):
		x=weight[0:num[0]]
		del weight[0:num[0]]
		x.sort()
		lst1=[]
		lst2=[]
		if num[0]%2==0:
			subset=num[0]/2
			del num[0]
			for j in range (int(len(x))):
				if len(lst1)<subset and sum(lst1)<sum(lst2):
					lst1.append(max(x))
					x.remove(max(x))
				else:
					if len(lst2)<subset:
						lst2.append(max(x))
						x.remove(max(x))
		else:
			subset=(num[0]-1)/2
			del num[0]
			for j in range (int(len(x))):
				if len(lst1)<=subset and sum(lst1)<sum(lst2):
					lst1.append(max(x))
					x.remove(max(x))
				else:
					if len(lst2)<=subset:
						lst2.append(max(x))
						x.remove(max(x))
		if t<test-1:
			print(sum(lst1),sum(lst2))
			print()
		else:
			print(sum(lst1),sum(lst2),end="")
	return
if __name__=="__main__":
	main()