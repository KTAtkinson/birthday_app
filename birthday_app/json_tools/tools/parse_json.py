"""Parse JSON document containing JSON objects"""

def parse(json):
  json_objs = list()
  level = 0
  
  for i, char in enumerate(json):
    if level == 0:
      opening_index = i
    
    if char == '{':
      level += 1
    elif char == "}":
      level -= 1
    
    if level == 0:
      try:
        json_objs.append(json[opening_index:i+1])
      except IndexError:
        json_objs.append(json[opening_index:])

  if json_objs:
    return json_objs
  
  return None

    
if __name__ == '__main__':
  pass
      