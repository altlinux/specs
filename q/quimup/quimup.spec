%define Name Quimup
Name: quimup
Version: 1.3.2
Release: alt1
Summary: A client for the music player daemon (MPD)
License: %gpl2plus
Group: Sound
#URL: http://kde-apps.org/content/show.php/Quimup?content=68374
URL: http://www.coonsden.com/
Source: %Name%{version}src.tar
Source1: Icons.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ libqt4-devel ImageMagick-tools
BuildPreReq: libmpdclient-devel libtag-devel

%description
%Name is a client for the music player daemon (MPD) written in C++ and
QT3. The clean interface makes controlling MPD's many features easy and
intuitive. The focus is on mouse handling: playlist management is done
entirely by drag-&-drop; playback functions are directly accessible
from the system tray.
%Name turns MPD into a perfect desktop music player.


%prep
%setup -n %Name%{version}src

tar -xf %SOURCE1

%build
export PATH=$PATH:%_qt4dir/bin
qmake \
	QMAKE_CXXFLAGS="%optflags" \
	%name.pro
%make_build V=1

iconv -f cp1251 -t utf-8 > %name.desktop <<__MENU__
[Desktop Entry]
Type=Application
Exec=%name
Icon=%name
Comment=Client for MPD
Terminal=false
Name=%Name
Categories=Qt;Audio;Player;
GenericName=%Name
__MENU__

for s in 16 22 24 36 72 96; do
    convert -resize ${s}x$s -depth 8 Icons/%name{128,$s}.png
done


%install
install -d %buildroot%_bindir
install -m755 %name %buildroot%_bindir/

install -d %buildroot%_pixmapsdir
install -p -m644 src/resources/* %buildroot%_pixmapsdir/

install -D -m 0644 {,%buildroot%_desktopdir/}%name.desktop
for s in 16 22 24 32 36 48 64 72 96 128; do
    install -D -m 0644 {Icons/%name$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done


%files
%doc changelog description FAQ.txt README
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*


%changelog
* Sun Sep 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Tue Dec 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.2
- Fixed build with glibc 2.16

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.1
- Fixed build

* Sat Feb 28 2009 Led <led@altlinux.ru> 0.3.5-alt1
- 0.3.5
- cleaned up spec
- updated BuildRequires

* Fri Aug 08 2008 Led <led@altlinux.ru> 0.3.4-alt2
- fixed %name.desktop
- added icons

* Sat Jun 28 2008 Led <led@altlinux.ru> 0.3.4-alt1
- initial build
