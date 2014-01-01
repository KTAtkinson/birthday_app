import sys
sys.path.append('')

import subprocess


def run(args):
  args_list = ['git']
  args_list.extend(args)
  return subprocess.Popen(args_list, stdout=subprocess.PIPE)

def get_output(*args):
  call = run(args)
  stdout, stderr = call.communicate()
  if stderr:
    return stderr
  
  return stdout

def has_exit_code(*args):
  call = run(args)
  call.poll()
  if call.returncode:
    return True
  
  return False

if __name__ == '__main__':
  pass