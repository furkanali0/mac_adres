import subprocess
import optparse
import re


def giris():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="interface degistirme")
    parse.add_option("-m", "--mac", dest="mac_adress", help="Yeni mac adres")
    return parse.parse_args()


def mac(inter, mac_adres):
    subprocess.call(["ifconfig", inter, "down"])
    subprocess.call(["ifconfig", inter, "hw", "ether", mac_adres])
    subprocess.call(["ifconfig", inter, "up"])


def kontrol(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    print(ifconfig)


print("Mac degistirici baslatildi.")
(userInput, arguments) = giris()
mac(userInput.interface, userInput.mac_adress)
kontrol(userInput.interface)
