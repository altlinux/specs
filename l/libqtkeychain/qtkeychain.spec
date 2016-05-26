Name: libqtkeychain 
Version: 0.6.2
Release: alt1

Group: Development/KDE and QT
Summary: QtKeychain is a Qt API to store passwords and other secret data securely.
License: 2-clause BSD
Url: https://github.com/frankosterfeld/qtkeychain
Source0: %name-%version.tar
Provides: qtkeychain = %version

BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: cmake gcc-c++ libqt4-devel qt5-tools-devel qt5-linguist pkgconfig(QtDBus) pkgconfig(Qt5DBus)

%description
QtKeychain is a Qt API to store passwords and other secret data securely.
If running, GNOME Keyring is used, otherwise  qtkeychain tries to use 
KWallet (via D-Bus), if available.

%package devel
Group: Development/KDE and QT
Summary: QtKeychain devel files.
Provides: qtkeychain-devel = %version

%description devel
QtKeychain devel files.

%package qt5
Group: Development/KDE and QT
Summary:        A password store library
Provides:       qtkeychain-qt5 = %version
Requires:       libqtkeychain = %version

%description qt5
The qt5keychain library allows you to store passwords easy and secure.

%package qt5-devel
Group: Development/KDE and QT
Summary:        Development files for %{name}-qt5
Provides:       qtkeychain-qt5-devel = %version
Requires:       libqtkeychain-qt5 = %version

%description qt5-devel
This package contains development files for qt5keychain.


%prep
%setup -q

%build
#cmake -DBUILD_WITH_QT4=ON
#cmake_build

mkdir build
pushd build
%{fedora_cmake} .. \
    -DBUILD_WITH_QT4:BOOL=ON \
    -DCMAKE_BUILD_TYPE=Release

make %{?_smp_mflags}
popd

mkdir build-qt5
pushd build-qt5
%{fedora_cmake} .. \
    -DBUILD_WITH_QT4:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release

make %{?_smp_mflags}
popd

%install
#make install -C BUILD DESTDIR=%buildroot
make install DESTDIR=%{buildroot} -C build-qt5
make install DESTDIR=%{buildroot} -C build

%find_lang --with-qt qtkeychain

grep %{_qt4_translationdir} qtkeychain.lang > %{name}-qt4.lang
grep %{_qt5_translationdir} qtkeychain.lang > %{name}-qt5.lang

%files -f %{name}-qt4.lang
%doc ReadMe.txt
%doc COPYING
%_libdir/libqtkeychain.so.*

%files devel
%_includedir/qtkeychain/
%_libdir/cmake/QtKeychain/
%_libdir/libqtkeychain.so


%files qt5 -f %{name}-qt5.lang
%doc ReadMe.txt
%doc COPYING
%_libdir/libqt5keychain.so.0*

%files qt5-devel
%_includedir/qt5keychain/
%_libdir/cmake/Qt5Keychain/
%_libdir/libqt5keychain.so


%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.2-alt1
- NMU: new version
- NMU: added libqtkeychain-qt5

* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- fix compile flags, translation packaging

* Thu Sep 11 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt1
- first build

