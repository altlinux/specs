Name:		transgui
Version:	5.0.1
Release:	alt1

Summary:	An App to remotely control a Transmission Bit-Torrent client
Summary(ru_RU.UTF8): Приложение для удаленного управления Бит-торрент-клиентом Transmission
Summary(uk_UA.UTF8): Додаток для віддаленого керування Біт-торрент-клієнтом Transmission
Group:		Networking/File transfer
License:	GPLv2

Url:		http://code.google.com/p/transmisson-remote-gui/
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	http://transmisson-remote-gui.googlecode.com/files/%name-%version-src.zip
Source1:	%name.desktop
Source2:	%name.1
Source3:	%name.sh

%add_findreq_skiplist %_datadir/%name/lang/%name.pl

# Automatically added by buildreq on Mon Oct 15 2012 (-bi)
# optimized out: cpio ed elfutils fontconfig fpc-compiler fpc-units-base fpc-units-db fpc-units-fcl fpc-units-fv fpc-units-gfx fpc-units-gnome1 fpc-units-gtk fpc-units-gtk2 fpc-units-math fpc-units-misc fpc-units-multimedia fpc-units-net fpc-units-rtl fpc-utils glib2-devel libX11-devel libatk-devel libcairo-devel libgdk-pixbuf libgdk-pixbuf-devel libgtk+2-devel libpango-devel sysvinit-utils termutils vim-minimal vitmp
BuildRequires: /usr/bin/convert lazarus prelink schedutils unzip

%description
Transmission Remote GUI is a feature rich cross platform front-end to remotely control
a Transmission Bit-Torrent client daemon via its RPC protocol. Transmission Remote GUI
is faster and has more functionality than the built-in Transmission web interface.

%description -l ru_RU.UTF8
Transmission Remote GUI является многофункциональным кроссплатформенныйм интерфейсом для
дистанционного управления демоном Бит-торрент-клиента Transmission через его RPC-протокол.
Transmission Remote GUI быстрее и имеет больше возможностей, чем встроенный веб-интерфейс
Transmission.

%description -l uk_UA.UTF8
Transmission Remote GUI є багатофункціональним багатоплатформовим інтерфейсом для дистанційного
керування демоном Біт-торрент-клієнта Transmission через його RPC-протокол. Transmission Remote
GUI швидше і має більше можливостей, ніж вбудований веб-інтерфейс Transmission.

%prep
%setup -T -c
%__unzip -qa %SOURCE0

%build
cd TransGUI
%make_build CC="gcc %optflags" CPP="g++ %optflags"
execstack -c %name

%install
install -Dp -m 755 TransGUI/%name %buildroot%_bindir/%name.bin
install -m 755 %SOURCE3 %buildroot%_bindir/%name
install -Dp -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dp -m 644 %SOURCE2 %buildroot%_man1dir/%name.1

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 TransGUI/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 TransGUI/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 TransGUI/%name.png %buildroot%_miconsdir/%name.png

# Lang
%__mkdir -p %buildroot%_datadir/%name
cp -a TransGUI/lang %buildroot%_datadir/%name/
rm -f %buildroot%_datadir/%name/lang/transgui.template

%files
%dir %_datadir/%name
%doc TransGUI/readme.txt TransGUI/LICENSE.txt TransGUI/rpc-spec.txt TransGUI/VERSION.txt
%_bindir/*
%_desktopdir/%name.desktop
%_man1dir/%name.*
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/lang

%changelog
* Sun Jan 05 2014 Motsyo Gennadi <drool@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Wed Nov 14 2012 Motsyo Gennadi <drool@altlinux.ru> 4.1-alt1
- 4.1

* Mon Oct 15 2012 Motsyo Gennadi <drool@altlinux.ru> 4.0.3-alt1
- initial build for ALT Linux
