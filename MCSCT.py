import urllib.request
import json
import io
import time
import os

os.system('cls')
print("MCSCT 1.0.0\n")


def main():
    print('1. Install Forge')
    print('2. Install Fabric')
    sel = input('Select: ')
    if (sel == '1'):
        return forgedl()
    elif (sel == '2'):
        return fabricdl()
    else:
        return print('Invalid Selection')


# FORGE #
def forgedl():

    fordir = './forge-server'

    if os.path.isdir(fordir) is False:
        print('Creating Directory')
        os.mkdir(fordir)
    else:
        print('Directory Already Exists.')

    if os.path.isfile(fordir+'/forge-installer.jar') is True:
        print('Installer Already Exists.')
    else:
        forgegetinput(fordir)
    frlink = [x for x in os.listdir(fordir) if x.startswith('forge-1') or x.startswith('minecraftforge')]
    forgefiles = (' '.join(frlink))
    if os.path.isfile(fordir+'/'+forgefiles) is True:
        print('Server Already Installed.')
    else:
        print('\nLaunching Forge Installer...')
        time.sleep(1)
        os.system(f'cmd /c "cd {fordir} && java -jar forge-installer.jar --installServer"')
    with open(fordir+'/eula.txt', 'w') as fe:
        fe.write('eula=true')
    if os.path.isfile(fordir+'/start.bat') is True:
        print('Start.bat Already Exists.')
    else:
        time.sleep(2)
        with open(fordir+'/start.bat', 'w') as fl:
            frlink = [x for x in os.listdir(fordir) if x.startswith('forge-1') or x.startswith('minecraftforge')]
            forgefiles = (' '.join(frlink))
            fl.write(f'@ECHO OFF\njava -Xmx2048M -Xms2048M -jar {forgefiles} nogui\nPAUSE')
            print('\n[MCSCT] Forge Server Successfully Installed.')
            print('[MCSCT] You can now start the server using start.bat')


# FABRIC #
def fabricdl():
    os.system('cls')
    print('Preparing Fabric Server...')
    time.sleep(2)

    fabdir = './fabric-server'

    if os.path.isdir(fabdir) is False:
        print('Creating Directory')
        os.mkdir(fabdir)
    else:
        print('Directory Already Exists.')
    if os.path.isfile(fabdir+'/fabric-installer.jar') is True:
        print('Installer Already Downloaded.')
    else:
        fabricgetinput(fabdir)
    if os.path.isfile(fabdir+'/fabric-server-launch.jar') is True:
        print('Server Already Installed.')
    else:
        print('\nLaunching Fabric Installer...')
        time.sleep(1)
        os.system(f'cmd /c "cd {fabdir} && java -jar fabric-installer.jar server -downloadMinecraft"')
    with open(fabdir+'/eula.txt', 'w') as fe:
        fe.write('eula=true')
    if os.path.isfile(fabdir+'/start.bat') is True:
        print('Start.bat already exists.')
    else:
        with open(fabdir+'/start.bat', 'w') as fl:
            fl.write('@ECHO OFF\njava -Xmx2048M -Xms2048M -jar fabric-server-launch.jar nogui\nPAUSE')
            print('\n[MCSCT] Fabric Server Successfully Installed.')
            print('[MCSCT] You can now start the server using start.bat')


# FORGE DOWNLOADER #
def forgegetinput(fordir):

    with urllib.request.urlopen(
            "https://gist.githubusercontent.com/stefmmm/399ee9c24da5e4631ea537c508ac99b4/raw/versions.json") as url:
        data = json.loads(url.read().decode())

    os.system('cls')
    print('Select Game Version, Ex: 1.7.10')
    print('Press Enter For Latest Version.')
    theinput = input("Version: ")
    if theinput == '':
        verselect = 'latest'
    else:
        verselect = theinput

    try:
        response = urllib.request.urlopen(data['versions'][verselect])  #
        length = response.getheader('content-length')  #
        if response.getcode() == 200:
            print('Starting Download')
        else:
            print('Something Went Wrong While Trying To Download Forge.')

        if length:
            length = int(length)
            blocksize = max(4096, length // 100)
        else:
            blocksize = 100000000

        buf = io.BytesIO()
        size = 0

        file = open(fordir+"/forge-installer.jar", "wb")
        while True:
            buf1 = response.read(blocksize)
            if not buf1:
                break
            buf.write(buf1)
            size += len(buf1)

            if length:
                file.write(buf.getbuffer())
                print(f'\rDownloading... {round((size / length) * 100)}%', end='')

        file.close()

    except KeyError:
        print('Invalid Version, Try Again.')
        time.sleep(1)
        return forgegetinput(fordir)


# FABRIC DOWNLOADER #
def fabricgetinput(fabdir):

    with urllib.request.urlopen(
            "https://gist.githubusercontent.com/stefmmm/399ee9c24da5e4631ea537c508ac99b4/raw/versions.json") as url:
        data = json.loads(url.read().decode())

    os.system('cls')

    try:
        response = urllib.request.urlopen(data['versions']['fabric_latest'])  #
        length = response.getheader('content-length')  #
        if response.getcode() == 200:
            print('Starting Download.')
        else:
            print('Something Went Wrong While Trying To Download Fabric.')

        if length:
            length = int(length)
            blocksize = max(4096, length // 100)
        else:
            blocksize = 100000000

        buf = io.BytesIO()
        size = 0

        file = open(fabdir+"/fabric-installer.jar", "wb")
        while True:
            buf1 = response.read(blocksize)
            if not buf1:
                break
            buf.write(buf1)
            size += len(buf1)

            if length:
                file.write(buf.getbuffer())
                print(f'\rDownloading... {round((size / length) * 100)}%', end='')

        file.close()

    except Exception:
        return fabricgetinput(fabdir)


if __name__ == '__main__':
    main()
