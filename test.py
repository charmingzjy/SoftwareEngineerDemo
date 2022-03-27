import os
import sys
from YQ import YQ_Data

# test1
def test_01():  # no parameters
    if len(sys.argv) < 2:
        input_file = ''
        yq = YQ_Data(input_file=input_file)
        assert len(yq.provs) == 0  # empty data
        print('Test01 Passed')

test_01()


# test2
def test_02():  # parameter: in, out
    if len(sys.argv) == 3 and '.' in sys.argv[2]:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        class Logger(object):
            def __init__(self):
                log_dir = output_file
                self.terminal = sys.stdout
                self.log = open(log_dir, 'w')
            def write(self, message):
                self.terminal.write(message)
                self.log.write(message)
            def flush(self):
                pass
        sys.stdout = Logger()

        yq = YQ_Data(input_file=input_file)
        assert len(yq.provs) != 0
        yq.print(sorted=True, specified_prov=None)
        print('Test02 Passed')

test_02()


# test3
def test_03():  # parameter: in, prov
    if len(sys.argv) == 3 and not os.path.isfile(sys.argv[2]):
        input_file = sys.argv[1]
        province = sys.argv[2]

        yq = YQ_Data(input_file=input_file)
        assert len(yq.provs) != 0
        yq.print(sorted=True, specified_prov=province)
        print('Test03 Passed')

test_03()

