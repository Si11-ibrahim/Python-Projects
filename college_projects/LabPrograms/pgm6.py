import os


def readFile(filePath):
    if not os.path.isfile(filePath):
        print('File not found!!')
        return None

    with open(filePath, 'r') as f:
        return f.readlines()


def countLines(fileContent):
    return len(fileContent) if fileContent else 0


def analyzeLog(file_path):
    content = readFile(file_path)

    if content is not None:
        lines = countLines(content)
        print(f'\nNumber of lines in {file_path} : {lines}')
        print('Some sample here:\n')
        print(''.join(content[:10]))


if __name__ == '__main__':
    filePath = input('Enter the path for the access log file: ')
    errorFilePath = input('Enter the path for the error log file: ')

    file = readFile(filePath)
    totalLines = countLines(file)
    analyzeLog(filePath)
