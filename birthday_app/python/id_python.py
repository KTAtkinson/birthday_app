"This script idendifies python files"


def is_python(file_name):
	if (".py" in file_name 
			or "#!/usr/bin/python" in open(file_name).read().split("\n")[0]):
		return True
	
	return False


if __name__ == "__main__":
	pass
