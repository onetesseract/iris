import os   #imports go at top or is that just node
import importlib.util
from padatious import IntentContainer
import threading
container = IntentContainer('intent_cache')
commands = {}
for filename in os.listdir('./cmds'):
    if filename.endswith(".py") and not filename.endswith("__init__.py"): #this all feels hacky af but i can't find a better SO answer
        print(os.path.join('./cmds', filename))                           #wait where did good coding principles go? i don't care atp.
        spec = importlib.util.spec_from_file_location("*", os.path.join('./cmds', filename))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('Adding', mod.name)
        container.add_intent(mod.name, mod.examples)
        commands[mod.name] = mod.exec
        continue
    else:
        continue
container.train()
def run(inp):
    resp = container.calc_intent(inp)
    if resp.conf > 0.4: #important number, defines how good a match the command must be to execute
        x = threading.Thread(target=commands[resp.name], args=(resp.matches,), daemon=True)  #daemon=true makes it dai quickli
        x.start()
    print(resp)
inp = ''
while inp != 'quit':
    inp = input('>>')
    if inp == 'quit':
        continue
    else:
        run(inp)