import subprocess

def main() : 
    raw_output = (subprocess.run("netsh wlan show profiles", shell=True,
                        stderr=subprocess.PIPE, stdout=subprocess.PIPE, 
                                universal_newlines=True) ).stdout.split("\n")
    network_names = []
    for  string in raw_output :
        if(string.__contains__("All User Profile")) :
           network_names.append(string.replace("All User Profile     : ", ""). lstrip())

    line = '='*50
    print(line)
    for network_name in network_names :
           network_password = subprocess.run("netsh wlan show profile name = \"" + network_name +
                         "\" key=clear | find \"Key Content\" ", shell=True,
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE, 
                          universal_newlines=True).stdout.replace("Key Content            : ","").lstrip().strip("\n")
           print(network_name + ": " + network_password)
    print(line)
    input("")

main()
