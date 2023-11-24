
from argparse import ArgumentParser
from os import environ

todo = {}


def _get_arguments():

    parser = ArgumentParser(
        description='Assignment 12'
    )

    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 

    parser.add_argument(
        '-f', '--films', choices=['1', '2'], default='1',
        help='which films resolvers to choose, default: 1 (films_1_resolvers.py)'
    ) 

    return vars(parser.parse_args())


def _get_todo_folder(args):
    
    return 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'     

def _get_resolvers(args):

    return f'films_{args["films"]}_resolvers.py'


def set_config():


    if 'GQL_EXAMPLE' in environ:

        if environ.get('GQL_EXAMPLE') == 'places':
            from examples.places import resolvers
        elif environ.get('GQL_EXAMPLE') == 'persons':
            from examples.persons import resolvers
        else:
            print('unknown example')
            quit()

        todo['resolvers'] = resolvers.query
        
        print('***')
        print('*** running example:', environ.get('GQL_EXAMPLE'))
        print('***')

        return


    args = _get_arguments()

    if args['review'] == '1':
        if args['films'] == '2':
            from todos.review_1 import films_2_resolvers as resolvers
        else:
            from todos.review_1 import films_1_resolvers as resolvers

    elif args['review'] == '2':
        if args['films'] == '2':
            from todos.review_2 import films_2_resolvers as resolvers
        else:
            from todos.review_2 import films_1_resolvers as resolvers

    else:
        if args['films'] == '2':
            from todos.your_code import films_2_resolvers as resolvers
        else:
            from todos.your_code import films_1_resolvers as resolvers

    todo['resolvers'] = resolvers.query

    print('***')
    print('*** todo folder:', _get_todo_folder(args))
    print('*** resolvers:  ', _get_resolvers(args))
    print('***')
