%define		rev 20091230

Name:		QCheckers
Summary:	Qt checkers game
Summary(ru_RU.UTF8): Игра в шашки на Qt
Summary(uk_UA.UTF8): Гра в шашки на Qt
Version:	0.1
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	GPLv3
Group:		Games/Boards
Url:		http://code.google.com/p/qcheckers/
Source0:	http://qcheckers.googlecode.com/files/%name-%rev.tar.gz
Source1:	%name.png
Source2:	%name.desktop

BuildRequires: gcc-c++ libqt4-devel /usr/bin/convert

%description
Qt checkers game. Written as a course work in university ;)

Features:

- Russian and international drafts (checkers)
- The player can choose a color
- Setting the depth of move search
- Viewing the history of moves

%prep
%setup -q -n %name

%build
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"
%make_build VERBOSE=1

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE1 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE1 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE1 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE1 %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png

%changelog
* Thu Nov 08 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
