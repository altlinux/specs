%define _unpackaged_files_terminate_build 1

Name: alvr-companion
Version: 0.1.1
Release: alt1

Summary: A small tool for managing ALVR from Linux distribution repositories.

License: MIT
Group: System/Configuration/Hardware
Url: https://github.com/Toxblh/ALVR-Companion

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: /usr/bin/convert

Requires: android-tools

ExclusiveArch: x86_64

%description
%summary

Main features:
* APK Download Management and Installation
* ADB Device Monitoring
* USB Forwarding Configuration
* Interactive UI

%prep
%setup

%build
%install
install -Dm 755 main.py %buildroot%_bindir/%name
install -Dm 644 assets/ALVR-Companion.desktop %buildroot%_desktopdir/ALVR-Companion.desktop

for res in 16 32 48 128 256; do
    mkdir -p %buildroot%_iconsdir/hicolor/$res'x'$res/apps/
    convert assets/ru.toxblh.AlvrCompanion.png -resize $res'x'$res %buildroot%_iconsdir/hicolor/$res'x'$res/apps/ru.toxblh.AlvrCompanion.png
done

%files
%doc Readme.md LICENSE
%_bindir/%name
%_desktopdir/ALVR-Companion.desktop
%_iconsdir/hicolor/*/apps/ru.toxblh.AlvrCompanion.png

%changelog
* Tue Oct 08 2024 Mikhail Tergoev <fidel@altlinux.org> 0.1.1-alt1
- initial build for ALT Sisyphus
