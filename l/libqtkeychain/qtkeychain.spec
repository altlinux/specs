Name: libqtkeychain
Version: 0.9.1
Release: alt2

%define sover 1
%define libqtkeychain libqtkeychain%sover
%define libqt5keychain libqt5keychain%sover

Group: Development/KDE and QT
Summary: QtKeychain is a Qt API to store passwords and other secret data securely
License: 2-clause BSD
Url: https://github.com/frankosterfeld/qtkeychain

Source0: %name-%version.tar
Patch1: alt-build-qt4.patch
BuildRequires: cmake gcc-c++ libqt4-devel qt5-tools-devel pkgconfig(QtDBus) pkgconfig(Qt5DBus) libsecret-devel

%description
QtKeychain is a Qt API to store passwords and other secret data securely.
If running, GNOME Keyring is used, otherwise  qtkeychain tries to use
KWallet (via D-Bus), if available.

%package -n qtkeychain-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt4-common
Conflicts: libqtkeychain < 0.7
%description -n qtkeychain-common
%name common package

%package -n qt5keychain-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
Conflicts: libqtkeychain-qt5 < 0.7
%description -n qt5keychain-common
%name common package

%package -n %libqtkeychain
Group: Development/KDE and QT
Summary: A password store library
Provides: qtkeychain = %version
Requires: qtkeychain-common
%description -n %libqtkeychain
The qtkeychain library allows you to store passwords easy and secure.

%package -n %libqt5keychain
Group: Development/KDE and QT
Summary: A password store library
Provides: qtkeychain-qt5 = %version
Requires: qt5keychain-common
%description -n %libqt5keychain
The qt5keychain library allows you to store passwords easy and secure.

%package devel
Group: Development/KDE and QT
Summary: QtKeychain devel files
Provides: qtkeychain-devel = %version
Requires: libsecret-devel
%description devel
QtKeychain devel files.

%package qt5-devel
Group: Development/KDE and QT
Summary: Development files for %name-qt5
Provides: qtkeychain-qt5-devel = %version
Requires: libsecret-devel
%description qt5-devel
This package contains development files for qt5keychain.

%prep
%setup
%patch1 -p1

%build
QTDIR="%_qt4dir" \
%cmake .. \
    -DBUILD_WITH_QT4:BOOL=ON \
    -DQTKEYCHAIN_STATIC=OFF \
    -DECM_MKSPECS_INSTALL_DIR=%_datadir/qt4/mkspecs \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
mv BUILD build-qt4

QTDIR="%_qt5_prefix" \
%cmake .. \
    -DBUILD_WITH_QT4:BOOL=OFF \
    -DQTKEYCHAIN_STATIC=OFF \
    -DECM_MKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
mv BUILD build-qt5

%install
rm -rf BUILD; ln -sf build-qt4 BUILD
PATH=$PATH:%_qt4dir/bin \
make install DESTDIR=%buildroot -C build-qt4
rm -rf BUILD; ln -sf build-qt5 BUILD
PATH=$PATH:%_qt5_bindir \
make install DESTDIR=%buildroot -C build-qt5

%find_lang --with-qt qtkeychain

grep %_datadir/qt4/translations qtkeychain.lang > %name-qt4.lang
grep %_qt5_translationdir qtkeychain.lang > %name-qt5.lang

%files -n qtkeychain-common -f %name-qt4.lang
%doc ReadMe.txt
%doc COPYING

%files -n qt5keychain-common -f %name-qt5.lang
%doc ReadMe.txt
%doc COPYING

%files -n %libqtkeychain
%_libdir/libqtkeychain.so.%sover
%_libdir/libqtkeychain.so.*

%files -n %libqt5keychain
%_libdir/libqt5keychain.so.%sover
%_libdir/libqt5keychain.so.*

%files devel
%_includedir/qtkeychain/
%_libdir/cmake/QtKeychain/
%_libdir/libqtkeychain.so
%_datadir/qt4/mkspecs/qt_QtKeychain.pri

%files qt5-devel
%_includedir/qt5keychain/
%_libdir/cmake/Qt5Keychain/
%_libdir/libqt5keychain.so
%_qt5_archdatadir/mkspecs/qt_Qt5Keychain.pri

%changelog
* Mon Feb 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.1-alt2
- NMU: fix requires

* Fri Aug 31 2018 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- new version

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt2
- fix requires

* Wed Aug 01 2018 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Mon May 22 2017 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1.M80P.1
- build for M80P

* Sun Nov 06 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt2
- fix conflicts

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt0.M80P.1
- build for M80P

* Thu Nov 03 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Sat Sep 17 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.2-alt0.M80P.1
- Backport new version to p8 branch (ALT #32507)

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1
- NMU: new version
- NMU: added libqtkeychain-qt5

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1.M70P.1
- built for M70P

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- fix compile flags, translation packaging

* Thu Sep 11 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt1
- first build

