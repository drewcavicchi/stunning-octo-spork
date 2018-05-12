import journal


def main():
    print_header()
    run_event_loop()


def run_event_loop():
    print("Welcome to your journal.")
    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd!= 'x':
        cmd = input('[A]dd Entry, [L]ist Entries, E[x]it: ')
        cmd = cmd.lower().strip()
        if cmd == 'a':
            add_journal_entry(journal_data)
        elif cmd == 'l':
            list_journal(journal_data)
        elif cmd != 'x':
            print("Hmm...looks like your typed '{}', learn to follow directions.".format(cmd))
    print('See ya')
    journal.save(journal_name, journal_data)


def add_journal_entry(data):
    entry = input("Please type entry, <enter> to exit: ")
    journal.add_journal_entry(entry, data)


def list_journal(data):
    print('Your entries: ')
    for (idx, item) in enumerate(data):
        print('[{}], {}'.format(idx, str(item)))





def print_header():
    print('--------------------')
    print('       Journal')
    print('--------------------')

main()
