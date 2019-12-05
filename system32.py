def osx(rundll):
	sshd = ""
	for i in rundll:
		sshd = sshd + chr(int(i/11))
	print(sshd)
	return(sshd)