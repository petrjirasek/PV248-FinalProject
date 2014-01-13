from interface import Interface
import commands.listdir as listdir
import commands.quit as quit
import commands.titles as titles

class Shell(object):
    __i = Interface

    def __init__(self, i):
    	self.__commands = {}
        self.__i = i

    def run(self):
        while True:
            line = self.__i.read()

            try:
                output = self.process(line)
            except Exception, e:
                i.write("error: " + str(e))
            else:
                if output is not None:
                    i.write(output)

    def process(self, line):
        inputs = line.split()
        function = self.__commands[inputs[0]]

        if len(inputs) < 2:
            parameter = None
        else:
         	parameter = inputs[1]

        return function(parameter)

    def add_command(self, command_name, command_function):
        self.__commands[command_name] = command_function


if __name__ == "__main__":
    i = Interface()
    s = Shell(i)
    thread = titles.TitlesThread(i)
    s.add_command('listdir', listdir.listdir)
    s.add_command('quit', quit.quit)
    s.add_command('titles', thread.titles)

    try:
        thread.start()
        s.run()
    except SystemExit:
        thread.stop()