Name: photos-desktop
Version: 0.1.0
Release: alt1

Summary: Electron based Textile Photos

License: MIT
Url: https://github.com/textileio/photos-desktop
Group: File tools

# Source-url: https://github.com/textileio/photos-desktop/archive/master.zip
Source: %name-%version.tar

Source1: %name-predownloaded-%version.tar

BuildArch: noarch

Requires: electron >= 4.0

BuildRequires: npm node-asar

%description
Textile provides encrypted, recoverable, schema-based, and cross-application data storage built on IPFS and libp2p.
We like to think of it as a decentralized data wallet with built-in protocols for sharing and recovery,
or more simply, an open and programmable iCloud.

%prep
%setup -a 1
%__subst "s|require('electron-is-dev')|false|" public/electron.js

%build
npm run build

cat <<EOF >%name
#!/bin/sh
electron %_datadir/%name/build/electron.js "\$@"
EOF

# Note: internal ../build using
#mv build/electron.js build/index.js
#asar pack build/ resources/app.asar

%install
install -m755 -D %name %buildroot%_bindir/%name
mkdir -p %buildroot%_datadir/%name/
cp -a build %buildroot%_datadir/%name/

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
* Sat Mar 23 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial release for ALT Sisyphus
