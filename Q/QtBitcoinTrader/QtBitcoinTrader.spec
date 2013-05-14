Name: QtBitcoinTrader
Version: 0.87
Release: alt1
Summary: Mt.Gox Bitcoin Trading Client
Url: http://sourceforge.net/projects/bitcointrader/
Group: Office
License: GPL2+
Source0: BitcoinTraderQtSRC_v%{version}.zip
Source1: %name.png
Source2: %name.desktop
Patch0: BitcoinTraderQt-alt_QtSolutions.diff
Patch1: BitcoinTraderQt-alt_QtSolutions_link.diff

BuildRequires: /usr/bin/convert gcc-c++ libqtsingleapplication-devel unzip libqt4-devel

%description
Mt.Gox Bitcoin Trading Client
This software helps you to open and cancel Mt.Gox orders vary fast.

%prep
%setup -c
%patch0 -p1
%patch1 -p1

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
%make_build

%install
install -Dp -m 0755 BitcoinTrader %buildroot%_bindir/BitcoinTrader
ln -s %_bindir/BitcoinTrader %buildroot%_bindir/%name
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
install -m 0644 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png

%files
%_bindir/*
%_desktopdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.87-alt1
- initial build for ALT Linux
