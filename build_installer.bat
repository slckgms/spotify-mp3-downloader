@echo off
cd /d "%~dp0"
title Spotify MP3 - Installer Olusturucu

set LOGFILE=%~dp0build_log.txt
echo Build basladi > "%LOGFILE%"
echo Klasor: %CD% >> "%LOGFILE%"

echo ============================================
echo   Spotify MP3 - Windows Installer v3
echo ============================================
echo.

echo [ADIM 1] Python kontrol...
python --version >> "%LOGFILE%" 2>&1
if errorlevel 1 ( echo [HATA] Python bulunamadi! & pause & exit /b 1 )
echo [OK] Python bulundu.

echo.
echo [ADIM 2] Paketler guncelleniyor...
python -m pip install -q --upgrade pip >> "%LOGFILE%" 2>&1
python -m pip install -q --upgrade requests >> "%LOGFILE%" 2>&1
python -m pip install -q --upgrade Pillow >> "%LOGFILE%" 2>&1
python -m pip install -q --upgrade yt-dlp >> "%LOGFILE%" 2>&1
python -m pip install -q --upgrade pyinstaller >> "%LOGFILE%" 2>&1
echo [OK] Paketler hazir (requests, Pillow, yt-dlp, pyinstaller).

echo.
echo [ADIM 3] Eski dosyalar temizleniyor...
rmdir /S /Q dist > nul 2>&1
rmdir /S /Q build > nul 2>&1
del /Q SpotifyMP3.spec > nul 2>&1
echo [OK] Temizlendi.

echo.
echo [ADIM 4] SpotifyMP3.exe olusturuluyor...
python -m PyInstaller --onefile --windowed --name "SpotifyMP3" ^
    --hidden-import yt_dlp ^
    --hidden-import requests ^
    --hidden-import tkinter ^
    --hidden-import PIL ^
    --hidden-import PIL.Image ^
    --hidden-import PIL.ImageTk ^
    --icon "%~dp0SpotifyMP3.ico" ^
    "%~dp0spotify_gui.py" >> "%LOGFILE%" 2>&1
if errorlevel 1 ( echo [HATA] EXE olusturulamadi! & type "%LOGFILE%" & pause & exit /b 1 )
if not exist "%~dp0dist\SpotifyMP3.exe" ( echo [HATA] dist\SpotifyMP3.exe yok! & pause & exit /b 1 )
echo [OK] SpotifyMP3.exe hazir.

echo.
echo [ADIM 5] ffmpeg kontrol ediliyor...
if not exist "%~dp0ffmpeg_bin" mkdir "%~dp0ffmpeg_bin"
if exist "%~dp0ffmpeg_bin\ffmpeg.exe" (
    echo [OK] ffmpeg zaten mevcut, atlandi.
) else (
    echo ffmpeg indiriliyor...
    python "%~dp0download_ffmpeg.py" >> "%LOGFILE%" 2>&1
    if errorlevel 1 ( echo [HATA] ffmpeg indirilemedi! & pause & exit /b 1 )
    if not exist "%~dp0ffmpeg_bin\ffmpeg.exe" ( echo [HATA] ffmpeg.exe yok! & pause & exit /b 1 )
    echo [OK] ffmpeg hazir.
)

echo.
echo [ADIM 6] README dosyalari olusturuluyor...
python "%~dp0create_readme.py" >> "%LOGFILE%" 2>&1
echo [OK] README dosyalari hazir.

echo.
echo [ADIM 7] NSIS aranıyor...
set "MAKENSIS="
if exist "C:\Program Files (x86)\NSIS\makensis.exe" set "MAKENSIS=C:\Program Files (x86)\NSIS\makensis.exe"
if exist "C:\Program Files\NSIS\makensis.exe" set "MAKENSIS=C:\Program Files\NSIS\makensis.exe"

if "%MAKENSIS%"=="" (
    echo NSIS bulunamadi, indiriliyor...
    python "%~dp0download_nsis.py" >> "%LOGFILE%" 2>&1
    timeout /t 8 /nobreak > nul
    if exist "C:\Program Files (x86)\NSIS\makensis.exe" set "MAKENSIS=C:\Program Files (x86)\NSIS\makensis.exe"
    if exist "C:\Program Files\NSIS\makensis.exe" set "MAKENSIS=C:\Program Files\NSIS\makensis.exe"
)
if "%MAKENSIS%"=="" (
    echo [HATA] NSIS kurulamadi! https://nsis.sourceforge.io/Download
    pause & exit /b 1
)
echo [OK] NSIS: %MAKENSIS%
echo NSIS: %MAKENSIS% >> "%LOGFILE%"

echo.
echo [ADIM 8] NSI script olusturuluyor...
python "%~dp0make_nsi.py" >> "%LOGFILE%" 2>&1
if errorlevel 1 ( echo [HATA] NSI script hatasi! & pause & exit /b 1 )
if not exist "%~dp0installer.nsi" ( echo [HATA] installer.nsi yok! & pause & exit /b 1 )
echo [OK] installer.nsi hazir.

echo.
echo [ADIM 9] Installer derleniyor...
"%MAKENSIS%" "%~dp0installer.nsi" >> "%LOGFILE%" 2>&1
echo NSIS cikis kodu: %errorlevel% >> "%LOGFILE%"

if exist "%~dp0SpotifyMP3_Setup.exe" (
    copy /Y "%~dp0SpotifyMP3_Setup.exe" "%USERPROFILE%\Desktop\SpotifyMP3_Setup.exe" > nul
    echo.
    echo ==========================================
    echo  TAMAMLANDI! SpotifyMP3_Setup.exe hazir!
    echo  Masaustune kopyalandi.
    echo ==========================================
    echo BASARILI >> "%LOGFILE%"
) else (
    echo.
    echo [HATA] Setup.exe olusturulamadi!
    echo build_log.txt dosyasini acin.
    echo BASARISIZ >> "%LOGFILE%"
)

echo.
pause
