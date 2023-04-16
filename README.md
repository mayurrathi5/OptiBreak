# OptiBreak: Breaks that Boost Your Eye Health

OptiBreak is a Python program designed to prevent eye strain caused by prolonged computer use. The program follows the 20-20-20 rule, which suggests that every 20 minutes, users should take a 20-second break and focus on an object 20 feet away. OptiBreak reminds users to take a break after every 20 minutes of computer use. The program runs in the background and does not interfere with other computer tasks.

## Usage

### Production Folder
Contains the executable file that you can execute after the system is turned on depending upon your operating system

In Windows (Command Prompt/PowerShell)
```cmd
OptiBreak.exe
```
or use file explorer

In Linux (Terminal)
```bash
sudo chmod +x OptiBreak
./OptiBreak
```
or use file explorer


## Development

Download the Repository  (Source Code, Production Folder from GitHub)

### Source Code Folder 
Contains the source code for different operating systems.

There are different requirements based on the operating system used for development. 


To install the requirements, follow the  process:

First, Install virtualenv that is common for all operating systems
```bash
pip3 install virtualenv
```
go to working directory (Source Code/Windows or Linux)
```bash
virtualenv env
```
In Windows (Command Prompt)
```cmd
env\Scripts\activate.bat
pip3 install -r requirement-windows.txt
```
In Windows (PowerShell)
```ps
.\env\Scripts\activate.ps1
pip3 install -r requirement-windows.txt
```

In Linux (Ubuntu/Debian Based)
```bash 
source env/bin/activate
sudo apt update
sudo apt install -y alsa-utils libasound2-dev
sudo apt install -y python3-pyqt5
pip3 install -r requirement-linux.txt
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
