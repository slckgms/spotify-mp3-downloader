import urllib.request, zipfile, os, shutil, sys

url = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip'
zip_path = 'ffmpeg_tmp.zip'

def progress(count, block, total):
    pct = min(int(count * block * 100 / total), 100)
    print(f'  {pct}%', end='\r', flush=True)

print('ffmpeg indiriliyor...')
try:
    urllib.request.urlretrieve(url, zip_path, reporthook=progress)
except Exception as e:
    print(f'HATA: {e}'); sys.exit(1)

print('\nZip aciliyor...')
try:
    with zipfile.ZipFile(zip_path, 'r') as z:
        for member in z.namelist():
            if member.endswith('bin/ffmpeg.exe') or member.endswith('bin/ffprobe.exe'):
                filename = os.path.basename(member)
                target = os.path.join('ffmpeg_bin', filename)
                with z.open(member) as src, open(target, 'wb') as dst:
                    shutil.copyfileobj(src, dst)
                print(f'  Cikartildi: {filename}')
except Exception as e:
    print(f'Zip acma HATA: {e}'); sys.exit(1)

if os.path.exists(zip_path):
    os.remove(zip_path)

if not os.path.exists('ffmpeg_bin/ffmpeg.exe'):
    print('HATA: ffmpeg.exe bulunamadi!'); sys.exit(1)

print('ffmpeg hazir.')
