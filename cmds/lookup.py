name = 'lookup'
examples = ['(find|lookup|search for|find me) {target} on {platform}', '(find|lookup|search for|find me) {target}','locate {target}']
def exec(args):
    if "target" in args:
        print('No chance. I\'m not gonna bother to find', args['target'])
    else:
        print('what now?')