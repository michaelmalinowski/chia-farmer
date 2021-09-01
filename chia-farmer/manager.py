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
            'Chia_Sto_3'
        ]

        self.driveList = self.discoverDrives()

        self.watchDrives()

    def mountDrive(self, drivePath, mountPoint):
        bashCommand = f"sudo mount {drivePath} {mountPoint}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        if not error == None:
            raise Exception(f'Subprocess error: {error}') 

        print(f"{drivePath} mounted at {mountPoint}")

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
                print(f'{driveName} not found.')

            unmountedIndex = output.find('(not mounted)')
            if not unmountedIndex == -1:
                print(f'{driveName} not mounted.')
                drivePath = ''
                for char in output:
                    if char == ' ' or char == '\\':
                        break
                    drivePath += char
                
                mountPoint = '/media/' +  f"Chia_{driveName[-1]}"
                self.mountDrive(drivePath, mountPoint)

    def watchDrives(self):
        pass

    def watchDrive(self):
        pass

    def restartSequence(self, drive: str):
        pass
