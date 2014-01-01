"Lints files"

import subprocess


def pylint(file_path):
  """ runs pylint on file found at file_path"""
  if ("__init__.py" in file_path or 
      "# __script__=hook" in open(file_path).read() and
      "lint.py" not in file_path):
    return [None, None]
	
  args = ["pylint",
			"""--rcfile=./standard.rc""",
			"--output-format",
			"parseable",
			"--reports",
			"n",
			"-d",
			"E1101",
			file_path]
  popen = subprocess.Popen(args, stdout=subprocess.PIPE)
  stdout, stderr = popen.communicate()
  
  if stderr:
    return [False, stderr]
	
  if stdout:
    errors = stdout[:-1].replace("{0}:".format(file_path), "line ")
    return [False, "\t" + "\n\t".join(errors.split("\n")) + "\n"]
	
  return [True, None]

if __name__ == '__main__':
  pass