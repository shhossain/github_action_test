a = 'v0.0.1'; b = int(a.split('''.''')[-1]); c = b + 1; d = f'''{'.'.join(a.split('.')[0:-1] + [str(c)])}'''; print(d)