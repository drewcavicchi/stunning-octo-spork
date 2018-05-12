import os


def load(name):
    data = []
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip)

    return data


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    print("...saving to: {}".format(filename))

    with open(filename, 'w') as fout:

        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_journal_entry(entry, journal_data):
    journal_data.append(entry)