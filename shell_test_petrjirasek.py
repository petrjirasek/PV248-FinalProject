import unittest
import shell
import interface

def printMsg(msg):
    return msg

class TestShell(unittest.TestCase):
    def setUp(self):
        i = interface.Interface()
        self.shell = shell.Shell(i)

    def test_add_command_and_process(self):
        self.shell.add_command('print', printMsg)
        self.assertEqual(self.shell.process("print message"), "message")

if __name__ == '__main__':
    unittest.main()