def theasaurus(*args):
   dic = {}
   for arg in args:
      key = chr(ord(arg[0]))
      if not dic.get(key):
         name = {key: [arg]}
         dic.update(name),
      else:
         n = dic.pop(key)
         n.append(arg)
         name = {key: n}
         dic.update(name)
   print(dic)

theasaurus("Иван", "Мария", "Петр", "Илья")



