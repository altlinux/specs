Name: webtorrent-desktop
Version: 0.18.0
Release: alt1

Summary: Streaming torrent app for Mac, Windows, and Linux

License: Apache 2.0
Url: https://riot.im/desktop.html
Group: Networking/Instant messaging

ExclusiveArch: x86_64
# Source-url: https://github.com/webtorrent/webtorrent-desktop/releases/download/v%version/webtorrent-desktop_%version-1_amd64.deb
Source: %name-%version.tar

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

# electron based requiries
BuildRequires: libgtk+2 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf

%description
Streaming torrent app for Mac, Windows, and Linux.

%prep
%setup
# replace strange missed functions with exit function
sed -E -i -e "s@(_ZN10crash_keys17SetVari|_ZN15MersenneTwister12in|_ZN15MersenneTwister13ge|_ZN15MersenneTwisterC1Ev|_ZN15MersenneTwisterD1Ev)@exit\x0MersenneTwisterD1Ev@g" opt/%name/WebTorrent
# strange
sed -E -i -e "s@_ZN2pp6Module3GetEv@exit\x0p6Module3GetEv@g" opt/%name/WebTorrent
sed -E -i -e "s@_ZNK2ui17WebDialogDelegate13GetDialogNameEv@exit\x0ui17WebDialogDelegate13GetDialogNameEv@g" opt/%name/WebTorrent

%__subst "s|/opt/%name/WebTorrent|%_bindir/%name|g" usr/share/applications/%name.desktop
%__subst "s|Path=/opt/%name||g" usr/share/applications/%name.desktop
chmod a+x opt/%name/WebTorrent

%install
mkdir -p %buildroot%_libdir/%name/
cp -a opt/%name/* %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/WebTorrent %buildroot/%_bindir/%name
ln -rs %buildroot%_libdir/%name/WebTorrent %buildroot/%_bindir/WebTorrent
mkdir -p %buildroot%_iconsdir/
cp -a usr/share/icons/hicolor/ %buildroot%_iconsdir/
mkdir -p %buildroot%_desktopdir/
cp -a usr/share/applications/%name.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_bindir/WebTorrent
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Jun 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.18.0-alt1
- initial release for ALT Sisyphus
