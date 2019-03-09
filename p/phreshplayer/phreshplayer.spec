Name: phreshplayer
Version: 1.0.0
Release: alt1

Summary: Electron based media player app

License: MIT
Url: https://github.com/Phreshhh/PhreshPlayer
Group: Video

# Source-url: https://github.com/Phreshhh/PhreshPlayer/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-preloaded-%version.tar

Patch: phreshplayer-disable-autoupdate.patch
Patch1: phreshplayer-electron4.patch

BuildArch: noarch

Requires: electron >= 4.0

BuildRequires: node-asar

%description
Electron based media player app.

%prep
%setup -a 1
%patch -p2
%patch1 -p2

%build
cat <<EOF >%name
#!/bin/sh
electron %_datadir/%name/resources/app.asar "\$@"
EOF

#asar pack --unpack-dir cedict . resources/app.asar
asar pack . resources/app.asar

%install
install -m755 -D %name %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name/
cp -a resources %buildroot%_datadir/%name/

#mkdir -p %buildroot%_iconsdir/
#cp -a usr/share/icons/hicolor/ %buildroot%_iconsdir/
#mkdir -p %buildroot%_desktopdir/
#cp -a usr/share/applications/akasha.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_datadir/%name/
#%_desktopdir/%name.desktop
#%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version (1.0.0) with rpmgs script

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.86-alt1
- initial release for ALT Sisyphus
