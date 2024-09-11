Name: libqtkeychain-qt6
Version: 0.14.3
Release: alt1

%define _cmake__builddir BUILD
%define sover 1
%define libqt6keychain libqt6keychain%sover

Group: Development/KDE and QT
Summary: QtKeychain is a Qt API to store passwords and other secret data securely
License: BSD-3-Clause
Url: https://github.com/frankosterfeld/qtkeychain

Source0: %name-%version.tar
BuildRequires: cmake qt6-tools-devel pkgconfig(Qt6DBus) libsecret-devel

%description
QtKeychain is a Qt API to store passwords and other secret data securely.
If running, GNOME Keyring is used, otherwise  qtkeychain tries to use
KWallet (via D-Bus), if available.

%package -n qt6keychain-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
Conflicts: libqtkeychain-qt6 < 0.7
%description -n qt6keychain-common
%name common package

%package -n %libqt6keychain
Group: Development/KDE and QT
Summary: A password store library
Provides: qtkeychain-qt6 = %version
Requires: qt6keychain-common
%description -n %libqt6keychain
The qt6keychain library allows you to store passwords easy and secure.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name-qt6
Provides: qtkeychain-qt6-devel = %version
Requires: libsecret-devel
%description devel
This package contains development files for qt6keychain.

%prep
%setup

%build
QTDIR="%_qt6_prefix" \
%cmake .. \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DECM_MKSPECS_INSTALL_DIR=%_qt6_archdatadir/mkspecs \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
export PATH=$PATH:%_qt6_bindir
make -C BUILD install DESTDIR=%buildroot

%find_lang --with-qt qtkeychain

%files -n qt6keychain-common -f qtkeychain.lang
%doc ReadMe.*
%doc COPYING

%files -n %libqt6keychain
%_libdir/libqt6keychain.so.%sover
%_libdir/libqt6keychain.so.*

%files devel
%_includedir/qt6keychain/
%_libdir/cmake/Qt6Keychain/
%_libdir/libqt6keychain.so
%_qt6_archdatadir/mkspecs/qt_Qt6Keychain.pri

%changelog
* Wed Sep 11 2024 Sergey V Turchin <zerg@altlinux.org> 0.14.3-alt1
- initial build
