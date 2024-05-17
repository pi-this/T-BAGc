from run import run_main
fileCount = 0

def openTbagFile(nameOfFile):
    global data, namefile, fileCount, listFiles
    try:
        with open(nameOfFile, 'r') as f:
            data = f.read()
            namefile = nameOfFile

            variables = {
                'test': 'hi',
                'true': True,
                'false': False
            }

            _functions = {}
            python_funcs_and_vars = locals()

            lines = data.split('\n')
            for i in range(len(lines)):
                namefile = namefile.replace(".bag","")
                run_main(lines[0], variables, 0, lines, _functions, python_funcs_and_vars, namefile)
    except FileNotFoundError:

        reportError("FileNotFoundError", str(1), "kid.bag")


def reportError(errorType,line,codeError):
    errorInfo = "on line "+line+"."+codeError
    return errorType, errorInfo