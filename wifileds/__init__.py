import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py':
        continue
    if module[-3:] != '.py':
        if os.path.isdir(os.path.join(os.path.dirname(__file__), module)):
            __import__(module, locals(), globals())
        continue
    __import__(module[:-3], locals(), globals())
del module
