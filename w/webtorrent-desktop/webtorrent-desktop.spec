Name: webtorrent-desktop
Version: 0.21.0
Release: alt1

Summary: Streaming torrent app for Mac, Windows, and Linux

License: Apache 2.0
Url: https://webtorrent.io
Group: Networking/Instant messaging

# BINSource-url: https://github.com/webtorrent/webtorrent-desktop/releases/download/v%version/webtorrent-desktop_%version-1_amd64.deb
# Source-url: https://github.com/webtorrent/webtorrent-desktop/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar
#Source2: %name-production-%version.tar

#ExclusiveArch: ix86 x86_64

BuildArch: noarch

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64

Requires: electron >= 4.0

BuildRequires: npm node-asar

%description
Streaming torrent app for Mac, Windows, and Linux.

%prep
%setup -a1
# for electron >= 4.0
%__subst "s|shouldQuit = app.makeSingleInstance(\(.*\))|shouldQuit = !app.requestSingleInstanceLock()|" src/main/index.js

%build
npm run build
npm prune --production

cat <<EOF >%name
#!/bin/sh
electron %_datadir/%name/resources/app.asar "\$@"
EOF

# ignore files listed in original package command
RULE=$(grep ignore: bin/package.js | sed -e "s|.*ignore: */\(.*\)/,|\1|")
find . | sed -e "s|^\.||" | egrep "($RULE)" | sed -e "s|^/||" | xargs rm -rfv

asar pack --unpack-dir static . resources/app.asar

%__subst "s|/opt/%name/WebTorrent|%_bindir/%name|g" static/linux/share/applications/%name.desktop
%__subst "s|Path=/opt/%name||g" static/linux/share/applications/%name.desktop

%install
install -m755 -D %name %buildroot%_bindir/%name
install -m644 -D resources/app.asar %buildroot%_datadir/%name/resources/app.asar
cp -a resources/app.asar.unpacked/ %buildroot%_datadir/%name/resources/

ln -s %name %buildroot/%_bindir/WebTorrent

mkdir -p %buildroot%_iconsdir/
cp -a static/linux/share/icons/hicolor/ %buildroot%_iconsdir/
mkdir -p %buildroot%_desktopdir/
cp -a static/linux/share/applications/%name.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_bindir/WebTorrent
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- new version (0.21.0) with rpmgs script

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt3
- update node_modules

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt2
- fix run with electron 4.x

* Thu Jul 12 2018 Vitaly Lipatov <lav@altlinux.ru> 0.20.0-alt1
- new version 0.20.0 (with rpmrb script)
- use new node_modules predownloading implementation from rpmgs

* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt2
- build with external electron

* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version (0.19.0) with rpmgs script
- build from sources

* Sat Jul 29 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18.0-alt2
- build with external electron

* Sat Jun 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18.0-alt1
- initial release for ALT Sisyphus
