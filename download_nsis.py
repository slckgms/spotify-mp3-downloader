import urllib.request, subprocess, os, time, sys

url = 'https://downloads.sourceforge.net/project/nsis/NSIS%203/3.10/nsis-3.10-setup.exe'
setup = 'nsis_setup.exe'

print('NSIS indiriliyor...')
try:
    urllib.request.urlretrieve(url, setup)
except Exception as e:
    print(f'HATA: {e}'); sys.exit(1)

print('NSIS kuruluyor...')
ret = subprocess.run([setup, '/S'], shell=True).returncode
print(f'Kurulum kodu: {ret}')
time.sleep(10)

if os.path.exists(setup):
    os.remove(setup)
print('Bitti.')
