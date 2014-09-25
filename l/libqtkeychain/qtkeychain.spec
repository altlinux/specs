Name: libqtkeychain 
Version: 0.4.0
Release: alt2

Group: Development/KDE and QT
Summary: QtKeychain is a Qt API to store passwords and other secret data securely.
License: 2-clause BSD
Url: https://github.com/frankosterfeld/qtkeychain
Source0: %name-%version.tar

BuildRequires: cmake gcc-c++ libqt4-devel

%description
QtKeychain is a Qt API to store passwords and other secret data securely.
If running, GNOME Keyring is used, otherwise  qtkeychain tries to use 
KWallet (via D-Bus), if available.

%package devel
Group: Development/KDE and QT
Summary: QtKeychain devel files.

%description devel
QtKeychain devel files.

%prep
%setup -q

%build
%cmake -DBUILD_WITH_QT4=ON
%cmake_build

%install
make install -C BUILD DESTDIR=%buildroot
%find_lang --with-qt qtkeychain

%files -f qtkeychain.lang
%doc COPYING
%_libdir/*.so.*

%files devel
%_libdir/cmake/*
%_libdir/*.so
/usr/include/*

%changelog
* Thu Sep 25 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- fix compile flags, translation packaging

* Thu Sep 11 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt1
- first build

