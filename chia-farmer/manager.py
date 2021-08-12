import time
import subprocess
#import lgpio

class Manager:
    def __init__(self):
        self.totalPlots = 162
        self.activePlots = 0
        self.driveNames = [
            'Chia_Sto_1',
            'Chia_Sto_2',
            'Chia_Sto_3',
            'Chia_TmpF_3'
        ]

        self.driveList = self.discoverDrives()

        self.watchDrives()

    def discoverDrives(self):
        for driveName in self.driveNames:

            bashCommand = f"sudo blkid -o list --match-token=LABEL={driveName}"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if not error == None:
                raise Exception(f'Subprocess error: {error}') 

            output = str(output)[53:]
            print(output)

            index = output.find(driveName)
            if index == -1:
                raise Exception(f'{driveName} not found.')

            unmountedIndex = output.find('(not mounted)')
            if not unmountedIndex == -1:
                print(f'{driveName} not mounted.')
                drivePath = ''
                for char in output:
                    if char == ' ' or char == '\\':
                        break
                    drivePath += char
                print(drivePath)


    def watchDrives(self):
        pass

    def watchDrive(self):
        pass

    def restartSequence(self, drive: str):
        pass

m = Manager()