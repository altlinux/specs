Name: kuklomenos
Version: 0.4.5
Release: alt1
Summary: An abstract shoot-em-up with some strategic aspects
Group: Games/Arcade
License: GPLv2+
Url: http://mbays.freeshell.org/kuklomenos/
Source0: http://mbays.freeshell.org/%name/src/%name-%version.tar.gz
Patch: %name-0.4.4-ratingStr.patch
Source1: %name.dia
#Source2: %name.desktop

#BuildRequires: desktop-file-utils

# Automatically added by buildreq on Sat May 29 2010
BuildRequires: dia gcc-c++ libSDL-devel python-modules-encodings

%description
An abstract shoot-em-up with some strategic aspects. Minimalistic graphics, short game-length. Gameplay lies somewhere between Centipede  and Starship Command. Very challenging at the higher difficulty levels. Can you make Elite?

%prep
%setup
%patch -p1
for N in 16 24 32 48 64 128; do
dia %SOURCE1 -n -t png -s ${N}x${N} -e ${N}.png
done

cat > %name.desktop <<@@@
[Desktop Entry]
Name=Kuklomenos
Comment=Abstract old school X shooter
Exec=%name
Icon=%name
Terminal=false
StartupNotify=false
Type=Application
Categories=Game;ArcadeGame;
@@@

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

for N in 16 24 32 48 64 128; do
install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc README NEWS TODO
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%changelog
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 0.4.5-alt1
- Autobuild version bump to 0.4.5

* Sat May 29 2010 Fr. Br. George <george@altlinux.ru> 0.4.4-alt1
- Version up
- Icons and desktop added

* Thu Oct 30 2008 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Initial build from scratch

