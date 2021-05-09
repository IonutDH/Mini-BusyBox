import os
import sys


def pwd_f():
	if len(sys.argv) == 2:
		a = os.getcwd()
		print (a)
		return 0
	else:
		return -1

def echo_f():
	a = ""
	n = len(sys.argv)
	if n > 2:
		if sys.argv[2] == '-n':
			a = sys.argv[3]
			for i in range(4,n):
				a = a + ' ' + sys.argv[i]
			print(a, end = "")
		else:
			a = sys.argv[2]
			for i in range(3, n):
				a = a + ' ' + sys.argv[i]
			print(a)
			return 0
	else:
		print("Invalid command")
		sys.exit(246)


def cat_f():
	n = len(sys.argv)
	if n > 2:
		for i in sys.argv[2:]:
			try:
				with open(i, "r") as file:
					for j in iter((file.readline), ""):
						print(j, end = "")
			except Exception as e:
				sys.exit(236)


def mkdir_f():
	n = len(sys.argv)
	if n > 2:
		for i in range(2, n):
			try:
				os.makedirs(sys.argv[i])
			except Exception as e:
				sys.exit(226)

def mv_f():
	n = len(sys.argv)
	if n == 4:
		if os.path.exists(sys.argv[2]):
			if os.path.isfile(sys.argv[3]) == False:
				os.rename(sys.argv[2], sys.argv[3])
			else:
				sys.exit(216)
		else:
			sys.exit(216)
	else:
		sys.exit(216)


def ln_f():
	a = ""
	n = len(sys.argv)
	if n > 2:
		try:
			if sys.argv[2] == '-s' or sys.argv[2] == '--symbolic':
				os.symlink(sys.argv[3], sys.argv[4])
			else:
				os.link(sys.argv[2], sys.argv[3])
		except Exception as e:
			sys.exit(206)

def rmdir_f():
	n = len(sys.argv)
	if n > 2:
		try:
			for i in range(2, n):
				if os.path.exists(sys.argv[i]) == True:
					if os.path.isdir(sys.argv[i]):
						os.rmdir(sys.argv[i])
				else:
					sys.exit(196)
		except Exception as e:
			sys.exit(196)
def rm_f():
	n = len(sys.argv)
	opts = ['-r', "--recursive", '-R', "--dir", '-d']
	a = 0
	b = True
	if n > 2:
		if b == True:
                        l = ["rm"]
                        if(sys.argv[2])[0] != '-':
                                for i in range(2, n):
                                        if os.path.isdir(sys.argv[i]) == False:
                                                l.append(sys.argv[i])
                                os.execvp(l[0], l[0:])
                        else:
                                os.execvp(sys.argv[1],sys.argv[1:])
		else:
			sys.exit(186)
		for i in range(2, n):
			if (sys.argv[i])[0] == '-' and sys.argv[i] not in opts:
				b = False
			if (sys.argv[i])[0] != '-' and os.path.exists(sys.argv[i]) == False:
                                b = False
	else:
		sys.exit(186)

def ls_f():
	n = len(sys.argv)
	a = True
	opts = ['-R', "--recursive", '-a', "--all"]
	if n > 1:
		if n > 2:
			if(sys.argv[2])[0] != '-' and os.path.exists(sys.argv[2]) == False:
				a = False
			if(sys.argv[2])[0] == '-' and sys.argv[2] not in opts:
				a = False
			if a == True:
				os.execvp(sys.argv[1], sys.argv[1:])
			else:
				sys.exit(176)
		os.execvp(sys.argv[1],sys.argv[1:])
	else:
		sys.exit(176)

def cp_f():
	n = len(sys.argv)
	opts = ['-r', '-R', "--recursive"]
	a = True
	if n > 3:
		if(sys.argv[2])[0] != '-' and (os.path.exists(sys.argv[2]) == False or os.path.exists(sys.argv[3]) == False):
			a = False
		if(sys.argv[2])[0] == '-' and sys.argv[2] not in opts:
			a = False
		if(sys.argv[2])[0] != '-' and os.path.isdir(sys.argv[2]) == True:
			a = False
		if a == True:
			os.execvp(sys.argv[1], sys.argv[1:])
		else:
			sys.exit(166)
	else:
		sys.exit(166) 


def touch_f():
	n = len(sys.argv)
	opts = ['-m', '-a', '-c', "--no-create"]
	a = True
	if n > 2:
		if(sys.argv[2])[0] == '-' and sys.argv[2] not in opts:
			sys.exit(156)
		os.execvp(sys.argv[1], sys.argv[1:])
	else:
		sys.exit(156)


def chmod_f():
	n = len(sys.argv)
	nr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	opts = ['u', 'g', 'o', 'a']
	if n == 4:
		if(sys.argv[2])[0] not in opts:
			if(sys.argv[2])[0] < "0" or (sys.argv[2])[0] > "9":
				print("Invalid command")
				sys.exit(255)
		os.execvp(sys.argv[1], sys.argv[1:])
	else:
		sys.exit(231)



if len(sys.argv) == 1:
	print("Invalid command")
	sys.exit(255)
else:
	a = sys.argv[1]
	if a == "pwd":
		pwd_f()
	if a == "echo":
		echo_f()
	if a == "cat":
		cat_f()
	if a == "mkdir":
		mkdir_f()
	if a == "mv":
		mv_f()
	if a == "ln":
		ln_f()
	if a == "rmdir":
		rmdir_f()
	if a == "rm":
		rm_f()
	if a == "ls":
		ls_f()
	if a == "cp":
		cp_f()
	if a == "touch":
		touch_f()
	if a == "chmod":
		chmod_f()
