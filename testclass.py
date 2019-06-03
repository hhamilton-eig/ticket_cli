import argparse

class AddTicket(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
            super(AddTicket, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()

parser.add_argument('ticket_number', 
                    metavar='<ticket_number>',
                    #type=int,
                    #action=AddTicket,
                    help='appends <ticket number> and timestamp to ~/ticket_list.txt')

# parser.add_argument('--note',
                    # '-n',
                    # action=NotateTicket,
                    # help='notates a ticket')
args = parser.parse_args()