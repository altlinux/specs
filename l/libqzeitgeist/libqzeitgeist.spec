
Name: libqzeitgeist
Version: 0.8.0
Release: alt1

Group: System/Libraries
Summary: Qt Zeitgeist Library
Url: http://projects.kde.org/projects/kdesupport/libqzeitgeist
License: LGPLv2+

Source: %name-%version.tar

# FC
Patch1: libqzeitgeist-0.8.0-declarative.patch
Patch2: libqzeitgeist-0.8.0-reduced_linking.patch

# Automatically added by buildreq on Fri Sep 09 2011 (-bi)
# optimized out: cmake-modules elfutils libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libstdc++-devel pkg-config
#BuildRequires: cmake gcc-c++ libqt3-devel libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 phonon-devel
BuildRequires: cmake gcc-c++ libqt4-devel kde-common-devel automoc python2.7(zeitgeist.datamodel)

%description
Qt Zeitgeist Library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup
%patch1 -p1
%patch2 -p1


%build
%Kbuild

%install
%Kinstall


%files
%doc README
%_libdir/libqzeitgeist.so.*
%dir %_libdir/qt4/imports/org/gnome/
%_libdir/qt4/imports/org/gnome/zeitgeist/

%files devel
%_includedir/QZeitgeist/
%_libdir/libqzeitgeist.so
%_libdir/cmake/QZeitgeist/
%_pkgconfigdir/QZeitgeist.pc

%changelog
* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt0.M60P.1
- built for M60P

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- initial build
