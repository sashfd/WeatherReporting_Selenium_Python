from datetime import datetime


def create_log(test_name):
    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y %H:%M:%S")
    filename = "logs/" + "execution_report" + '.log'
    line_prepend(filename, current_time + '  ' + test_name + '\n')


def logic_for_pass_fail_error(result):
    if result:
        return "Passed. "
    elif not result:
        return "Failed. "
    else:
        return "Error. "


def line_prepend(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def initialize_log():
    filename = "logs/" + "execution_report" + '.log'

    f = open(filename, 'r+')
    f.truncate(0)
