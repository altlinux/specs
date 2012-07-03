
Name: dfbrowser
Version: 1.1
Release: alt2

Group: File tools
Summary: Deuteros File Browser
Url: http://qt-apps.org/content/show.php/Dfilebrowser
License: GPL

Source: %name-%version.tar
Source1: dfilebrowser.png
Source2: dfilebrowser.desktop

Patch0: dfilebrowser-target.patch

# Automatically added by buildreq on Mon Feb 27 2012 (-bi)
# optimized out: elfutils fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-systeminfo libstdc++-devel python-base
#BuildRequires: gcc-c++ glibc-devel-static phonon-devel qt4-mobility-devel
BuildRequires: gcc-c++ glibc-devel phonon-devel qt4-mobility-devel
BuildRequires: libqt4-devel

%description
This Filebrowser allows to work on the Touchpad like dolphin

%prep
%setup -q
%patch0
qmake-qt4 -r dfilebrowser.pro "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags"

%build
%make_build

%install
%make install INSTALL_ROOT="%buildroot"

install -d -m 755 %buildroot/%_datadir/pixmaps
install -m 644 %SOURCE1 %buildroot/%_datadir/pixmaps/dfilebrowser.png
install -d -m 755 %buildroot/%_desktopdir/
install -m 644 %SOURCE2 %buildroot/%_desktopdir/dfilebrowser.desktop

%files
%_bindir/dfilebrowser
%_datadir/pixmaps/dfilebrowser.png
%_desktopdir/dfilebrowser.desktop

%changelog
* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- increase desktopfile InitialPreference

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.1-alt0.M60P.1
- built for M60P

* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- initial build
