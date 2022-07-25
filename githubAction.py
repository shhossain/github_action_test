# a = 'v0.0.1'
# b = int(a.split('.')[-1]) if a.split('.')[-1] else 0
# c = b + 1
# d = '.'.join(a.split('.')[0:-1] + [str(c)])
# d = d if d != '1' else '0.0.1'
# d = d if 'v' in d else 'v' + d
# print(d)

# one line
a = 'v0.0.1'; b = int(a.split('.')[-1]) if a.split('.')[-1] else 0; c = b + 1; d = '.'.join(a.split('.')[0:-1] + [str(c)]) if c != 1 else '0.0.1'; d = d if 'v' in d else 'v' + d; print(d)