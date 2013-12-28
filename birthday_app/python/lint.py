"Lints files"

import subprocess


def pylint(file_path):
	args = ["pylint",
			"""--rcfile=./standard.rc""",
			"--output-format",
			"parseable",
			"--reports",
			"n",
			file_path]
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	stdout, stderr = popen.communicate()
	
	if stdout:
		errors = stdout[:-1].replace("{0}:".format(file_path), "line ")
		return [False, "\t" + "\n\t".join(errors.split("\n")) + "\n"]
	
	return [True, None]