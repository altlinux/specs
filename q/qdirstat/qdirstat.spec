Name: qdirstat
Version: 1.8
Release: alt1
Summary: Qt-based directory statistics
Group: File tools
License: GPLv2
Url: https://github.com/shundhammer/qdirstat
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %url/archive/%version/%name-%version.tar.gz
Source1: %name.appdata.xml
Source2: %name.svg

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5)
BuildRequires: pkgconfig(zlib)
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
#BuildRequires: qt5-tools-devel-static
BuildRequires: qt5-svg-devel
BuildRequires: qt5-script-devel
BuildRequires: perl-Encode-Escape perl-URI-Escape-XS perl-URI perl-URI-Encode


#Requires: qt5-qtbase
Requires: icon-theme-hicolor

%description
QDirStat is a graphical application to show where your disk space has gone
and to help you to clean it up.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
 latest Qt 5. It does not need any KDE libs or infrastructure. It runs on
 every X11-based desktop on Linux, BSD and other Unix-like systems.

%prep
%setup -n %name-%version

%build
%qmake_qt5
%make_build


%install

%makeinstall INSTALL_ROOT=%buildroot


install -Dp -m 644 %SOURCE1 %buildroot%_datadir/metainfo/%name.appdata.xml
install -Dp -m 644 %SOURCE2 %buildroot%_datadir/icons/hicolor/scalable/apps/%name.svg

%check
desktop-file-validate %buildroot%_datadir/applications/qdirstat.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.appdata.xml

%files
#doc LICENSE
%_docdir/%name/
%_bindir/qdirstat
%_bindir/qdirstat-cache-writer
%_datadir/metainfo/%name.appdata.xml
%_datadir/applications/%name.desktop
#_datadir/icons/hicolor/*/apps/%name.png
%_man1dir/qdirstat-cache-writer.1.*
%_man1dir/qdirstat.1.*
%_datadir/icons/hicolor/scalable/apps/%name.svg

%changelog
* Mon Aug 30 2021 Ilya Mashkin <oddity@altlinux.ru> 1.8-alt1
- 1.8

* Wed Apr 21 2021 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- 1.7.1
- add man pages

* Mon May 21 2018 Ilya Mashkin <oddity@altlinux.ru> 1.4-alt1
- build for Sisyphus

* Fri Mar 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-7
- Add a svg icon for Appstream

* Sun Feb 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.4-6
- Add missing BR for gcc-c++

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4-4
- Remove obsolete scriptlets

* Tue Jul 25 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-3
- Fix for Fedora Review

* Thu Jul 20 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-2
- Update to Fedora Packaging Guidelines specification

* Sat Jun 24 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.4-1
- Update to version 1.4

* Tue Mar 07 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.3-1
- Update to version 1.3

* Fri Jan 06 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.2-1
- Update to version 1.2

* Sat Dec 03 2016 Robert-André Mauchin <zebob.m@gmail.com> 1.1-1
- First RPM release
