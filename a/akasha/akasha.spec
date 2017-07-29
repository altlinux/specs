Name: akasha
Version: 0.5.2
Release: alt2

Summary: Advanced Knowledge Architecture for Social Human Advocacy

License: Apache 2.0
Url: https://github.com/AkashaProject/node-app#readme
Group: Networking/Instant messaging

# Source-url: https://github.com/AkashaProject/Alpha/releases/download/%version/AKASHA-linux-x64-%version.deb
Source: %name-%version.tar

BuildArch: noarch

%description
A Next-Generation Social Media Network.
Powered by the Ethereum world computer.
Embedded into the Inter-Planetary File System.

AETH is our test token on the private chain used for this pre-release.
As a test token it does not have any value outside the purpose of testing AKASHA.
At this point, you can obtain AETH tokens by creating an identity on AKASHA.

%prep
%setup
%__subst "s|/opt/AKASHA/akasha|%_bindir/%name|g" usr/share/applications/akasha.desktop

cat <<EOF >%name
#!/bin/sh
electron %_datadir/%name/resources/app.asar
EOF

%install
install -m755 -D %name %buildroot%_bindir/%name
install -m644 -D opt/AKASHA/resources/app.asar %buildroot%_datadir/%name/resources/app.asar

mkdir -p %buildroot%_iconsdir/
cp -a usr/share/icons/hicolor/ %buildroot%_iconsdir/
install -m755 -D usr/share/applications/akasha.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Jul 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt2
- build with external electron

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial release for ALT Sisyphus
