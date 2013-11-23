Name:		glrp
Version:	1.4.5
Release:	alt1
Summary:	Robust internet radio station streamer
Url:		http://sourceforge.net/projects/glrp/?source=dlp
License:	GPLv3+
Group:		Sound
Source0:	greatlittleradioplayer_%version.tar.gz
Source1:	Ukrainian.lng

Patch0:		greatlittleradioplayer_1.4.5_fix_phonon_includes.diff
Patch1:		greatlittleradioplayer_1.4.5_fix_desktop.diff

BuildRequires: gcc-c++ libqt4-devel

%description
A robust internet radio station streamer. It connects to web sites
offering radio streaming and lets you play radio stations directly
from that locations.

%prep
%setup -n greatlittleradioplayer_%version
chmod -R -x ./*.* ./language/*.* ./styles/*.* ./styles/images/* ./styles/thumbnails/*
%patch0 -p1
%patch1 -p1

%build
# change ugly dir for files
find -type f -name \* -exec sed -i -r 's|/opt/extras.ubuntu.com|%_datadir|g' {} \;

qmake-qt4 "QMAKE_CFLAGS+=%optflags -I/usr/include/kde4" "QMAKE_CXXFLAGS+=%optflags -I/usr/include/kde4"
%make_build

%install
install -Dp -m 0644 extras-greatlittleradioplayer.desktop %buildroot%_desktopdir/%name.desktop

install -Dp -m 0644 %SOURCE1 %buildroot%_datadir/glrp/language/Ukrainian.lng
cp language/* %buildroot%_datadir/glrp/language/

mkdir -p %buildroot%_datadir/glrp/styles
cp -r styles/* %buildroot%_datadir/glrp/styles/

install -Dp -m 0644 glrp.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -Dp -m 0755 GreatLittleRadioPlayer %buildroot%_bindir/glrp
cp stations.csv %buildroot%_datadir/glrp/
cp changelog.txt %buildroot%_datadir/glrp/

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/

%changelog
* Sat Nov 23 2013 Motsyo Gennadi <drool@altlinux.ru> 1.4.5-alt1
- initial build for ALT Linux from PCLinuxOS package
