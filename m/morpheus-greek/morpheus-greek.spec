Name: morpheus-greek
Version: 0.3.1
Release: alt1

Summary: Simple practical Ancient Greek morph analizer

License: GPL
Url: https://github.com/mbykov/morpheus-greek
Group: File tools

# Source-url: https://github.com/mbykov/morpheus-greek/releases/download/v%version/morpheus-%version.tar.xz
Source: %name-%version.tar

BuildArch: noarch

Requires: electron

%description
Simple practical Ancient Greek morph analizer on a top of electron.js.

%prep
%setup

%build
cat <<EOF >%name
#!/bin/sh
electron %_datadir/%name/resources/app.asar
EOF

%install
install -m755 -D %name %buildroot%_bindir/%name
install -m644 -D resources/app.asar %buildroot%_datadir/%name/resources/app.asar

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
* Sat Jul 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial release for ALT Sisyphus
