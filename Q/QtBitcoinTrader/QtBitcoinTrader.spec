Name: QtBitcoinTrader
Version: 0.98
Release: alt1
Summary: Mt.Gox Bitcoin Trading Client
Url: http://sourceforge.net/projects/bitcointrader/
Group: Office
License: GPLv3
Source0: BitcoinTraderQtSRC_v%{version}.zip

BuildRequires: /usr/bin/convert gcc-c++ unzip libqt4-devel

%description
Mt.Gox Bitcoin Trading Client
This software helps you to open and cancel Mt.Gox orders vary fast.

%prep
%setup -n BitcoinTraderQtSRC_v%{version}

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
%make_build

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name
install -Dp -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
install -m 0644 %name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 %name.png %buildroot%_miconsdir/%name.png

%files
%_bindir/*
%_desktopdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Mon Jun 03 2013 Motsyo Gennadi <drool@altlinux.ru> 0.98-alt1
- 0.98

* Tue May 28 2013 Motsyo Gennadi <drool@altlinux.ru> 0.96-alt1
- 0.96

* Fri May 24 2013 Motsyo Gennadi <drool@altlinux.ru> 0.94-alt1
- 0.94

* Sat May 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.93-alt2
- fixed rules

* Sat May 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.93-alt1
- 0.93

* Fri May 17 2013 Motsyo Gennadi <drool@altlinux.ru> 0.90-alt1
- 0.90

* Tue May 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.87-alt1
- initial build for ALT Linux
