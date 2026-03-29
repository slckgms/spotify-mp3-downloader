import os, sys

base         = os.path.dirname(os.path.abspath(__file__))
dist_exe     = os.path.join(base, 'dist', 'SpotifyMP3.exe')
ffmpeg       = os.path.join(base, 'ffmpeg_bin', 'ffmpeg.exe')
ffprobe      = os.path.join(base, 'ffmpeg_bin', 'ffprobe.exe')
readme       = os.path.join(base, 'README.txt')
readme_dir   = os.path.join(base, 'readme_langs')
icon_ico     = os.path.join(base, 'SpotifyMP3.ico')

# readme_langs yoksa olustur
if not os.path.exists(readme_dir):
    cr = os.path.join(base, 'create_readme.py')
    if os.path.exists(cr):
        import subprocess
        subprocess.run([sys.executable, cr], cwd=base)

# README yoksa olustur
if not os.path.exists(readme):
    cr = os.path.join(base, 'create_readme.py')
    if os.path.exists(cr):
        import subprocess
        subprocess.run([sys.executable, cr], cwd=base)

for f, name in [(dist_exe,'SpotifyMP3.exe'),(ffmpeg,'ffmpeg.exe'),(ffprobe,'ffprobe.exe')]:
    if not os.path.exists(f):
        print(f'HATA: {name} bulunamadi: {f}')
        sys.exit(1)

exe_mb    = os.path.getsize(dist_exe) // (1024*1024)
ffmpeg_mb = os.path.getsize(ffmpeg)   // (1024*1024)
total_mb  = exe_mb + ffmpeg_mb + 5
print(f'SpotifyMP3.exe: {exe_mb} MB')
print(f'ffmpeg.exe:     {ffmpeg_mb} MB')
print(f'Tahmini Setup:  ~{total_mb} MB')

NL  = '$\\r$\\n'  # NSIS satir sonu
out = os.path.join(base, 'SpotifyMP3_Setup.exe')
rd  = readme_dir

lines = [
    '!define APP_NAME "Spotify MP3 Indirici"',
    '!define APP_EXE  "SpotifyMP3.exe"',
    '',
    f'Name "${{APP_NAME}}"',
    f'OutFile "{out}"',
    f'!define MUI_ICON "{icon_ico}"',
    f'!define MUI_UNICON "{icon_ico}"',
    'InstallDir "$PROGRAMFILES\\SpotifyMP3"',
    'RequestExecutionLevel admin',
    '',
    '!include "MUI2.nsh"',
    '',
    '!define MUI_ABORTWARNING',
    '!define MUI_FINISHPAGE_RUN         "$INSTDIR\\${APP_EXE}"',
    '!define MUI_FINISHPAGE_RUN_TEXT    "Spotify MP3 Indiriciyi hemen baslat"',
    '!define MUI_FINISHPAGE_SHOWREADME "$INSTDIR\\README.txt"',
    '!define MUI_FINISHPAGE_SHOWREADME_TEXT "README.txt ac / Open README.txt"',
    '!define MUI_WELCOMEPAGE_TITLE      "Spotify MP3 Indirici Kurulumu"',
    (
        '!define MUI_WELCOMEPAGE_TEXT       '
        '"Spotify playlist, album veya sarki linkini yapistirip tek tikla MP3 indirin.'
        '$\\r$\\n$\\r$\\n'
        'Icinde bulunananlar:$\\r$\\n'
        '  - Spotify MP3 Indirici$\\r$\\n'
        '  - ffmpeg (ses donusturucu)$\\r$\\n'
        '  - yt-dlp (YouTube indirici)$\\r$\\n'
        '  - Pillow (gorsel isleme)$\\r$\\n'
        '$\\r$\\n'
        'Hicbir ek kurulum gerekmez."'
    ),
    '',
    '!define MUI_LANGDLL_ALLLANGUAGES',
    '!insertmacro MUI_PAGE_WELCOME',
    '!insertmacro MUI_PAGE_DIRECTORY',
    '!insertmacro MUI_PAGE_INSTFILES',
    '!insertmacro MUI_PAGE_FINISH',
    '!insertmacro MUI_UNPAGE_CONFIRM',
    '!insertmacro MUI_UNPAGE_INSTFILES',
    '!insertmacro MUI_LANGUAGE "Turkish"',
    '!insertmacro MUI_LANGUAGE "English"',
    '!insertmacro MUI_LANGUAGE "German"',
    '!insertmacro MUI_LANGUAGE "Russian"',
    '!insertmacro MUI_LANGUAGE "SimpChinese"',
    '!insertmacro MUI_LANGUAGE "Spanish"',
    '!insertmacro MUI_LANGUAGE "French"',
    '!insertmacro MUI_LANGUAGE "PortugueseBR"',
    '!insertmacro MUI_LANGUAGE "Arabic"',
    '!insertmacro MUI_LANGUAGE "Japanese"',
    '!insertmacro MUI_LANGUAGE "Korean"',
    '!insertmacro MUI_LANGUAGE "Italian"',
    '',
    'Function .onInit',
    '  !insertmacro MUI_LANGDLL_DISPLAY',
    'FunctionEnd',
    '',
    'Section "Ana Program"',
    '  SetOutPath "$INSTDIR"',
    f'  File "{dist_exe}"',
    f'  File "{icon_ico}"',
    '',
    '  ; Secilen dile gore README kur',
    '  StrCmp $LANGUAGE 1055 inst_tr',
    '  StrCmp $LANGUAGE 1031 inst_de',
    '  StrCmp $LANGUAGE 1049 inst_ru',
    '  StrCmp $LANGUAGE 2052 inst_zh',
    '  StrCmp $LANGUAGE 1034 inst_es',
    '  StrCmp $LANGUAGE 1036 inst_fr',
    '  StrCmp $LANGUAGE 1046 inst_pt',
    '  StrCmp $LANGUAGE 1025 inst_ar',
    '  StrCmp $LANGUAGE 1041 inst_ja',
    '  StrCmp $LANGUAGE 1042 inst_ko',
    '  StrCmp $LANGUAGE 1040 inst_it',
    '  Goto inst_en',
    f'  inst_tr: File "/oname=README.txt" "{rd}\\README_TR.txt"',
    '  Goto rdone',
    f'  inst_de: File "/oname=README.txt" "{rd}\\README_DE.txt"',
    '  Goto rdone',
    f'  inst_ru: File "/oname=README.txt" "{rd}\\README_RU.txt"',
    '  Goto rdone',
    f'  inst_zh: File "/oname=README.txt" "{rd}\\README_ZH.txt"',
    '  Goto rdone',
    f'  inst_es: File "/oname=README.txt" "{rd}\\README_ES.txt"',
    '  Goto rdone',
    f'  inst_fr: File "/oname=README.txt" "{rd}\\README_FR.txt"',
    '  Goto rdone',
    f'  inst_pt: File "/oname=README.txt" "{rd}\\README_PT.txt"',
    '  Goto rdone',
    f'  inst_ar: File "/oname=README.txt" "{rd}\\README_AR.txt"',
    '  Goto rdone',
    f'  inst_ja: File "/oname=README.txt" "{rd}\\README_JA.txt"',
    '  Goto rdone',
    f'  inst_ko: File "/oname=README.txt" "{rd}\\README_KO.txt"',
    '  Goto rdone',
    f'  inst_it: File "/oname=README.txt" "{rd}\\README_IT.txt"',
    '  Goto rdone',
    f'  inst_en: File "/oname=README.txt" "{rd}\\README_EN.txt"',
    '  rdone:',
    '',
    '  ; ffmpeg',
    '  SetOutPath "$INSTDIR\\ffmpeg"',
    f'  File "{ffmpeg}"',
    f'  File "{ffprobe}"',
    '',
    '  ; ffmpeg PATH ekle',
    '  ReadRegStr $0 HKLM "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" "Path"',
    '  WriteRegExpandStr HKLM "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment" "Path" "$0;$INSTDIR\\ffmpeg"',
    '  SendMessage ${HWND_BROADCAST} ${WM_WININICHANGE} 0 "STR:Environment" /TIMEOUT=5000',
    '',
    '  WriteUninstaller "$INSTDIR\\Uninstall.exe"',
    '  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SpotifyMP3" "DisplayName" "${APP_NAME}"',
    '  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SpotifyMP3" "UninstallString" "$INSTDIR\\Uninstall.exe"',
    '  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SpotifyMP3" "DisplayVersion" "1.0"',
    '  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SpotifyMP3" "Publisher" "SpotifyMP3"',
    f'  WriteRegDWORD HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SpotifyMP3" "EstimatedSize" {total_mb * 1024}',
    '',
    '  ; Masaustu kisayolu - icon ile',
    '  CreateShortcut "$DESKTOP\\Spotify MP3 Indirici.lnk" "$INSTDIR\\${APP_EXE}" "" "$INSTDIR\\SpotifyMP3.ico" 0',
    '  CreateDirectory "$SMPROGRAMS\\Spotify MP3 Indirici"',
    '  CreateShortcut "$SMPROGRAMS\\Spotify MP3 Indirici\\Spotify MP3 Indirici.lnk" "$INSTDIR\\${APP_EXE}" "" "$INSTDIR\\SpotifyMP3.ico" 0',
    '  CreateShortcut "$SMPROGRAMS\\Spotify MP3 Indirici\\Kaldir.lnk" "$INSTDIR\\Uninstall.exe"',
    'SectionEnd',
    '',
    'Section "Uninstall"',
    '  Delete "$INSTDIR\\${APP_EXE}"',
    '  Delete "$INSTDIR\\README.txt"',
    '  Delete "$INSTDIR\\SpotifyMP3.ico"',
    '  Delete "$INSTDIR\\Uninstall.exe"',
    '  Delete "$INSTDIR\\ffmpeg\\ffmpeg.exe"',
    '  Delete "$INSTDIR\\ffmpeg\\ffprobe.exe"',
    '  RMDir "$INSTDIR\\ffmpeg"',
    '  RMDir "$INSTDIR"',
    '  Delete "$DESKTOP\\Spotify MP3 Indirici.lnk"',
    '  RMDir /r "$SMPROGRAMS\\Spotify MP3 Indirici"',
    '  DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\SpotifyMP3"',
    'SectionEnd',
]

nsi_path = os.path.join(base, 'installer.nsi')
with open(nsi_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'installer.nsi yazildi: {nsi_path}')
