Name: libqtkeychain 
Version: 0.4.0
Release: alt1

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
###From CVS only
suffix=`echo %_libdir | sed s/[^0-9]*//`
cmake -DCMAKE_INSTALL_PREFIX=/usr/  -DLIB_SUFFIX="$suffix" .
make

%install
make install DESTDIR=%buildroot

%files
%doc COPYING
%_libdir/*.so.*
/usr/share/qt4/translations/*

%files devel
%_libdir/cmake/*
%_libdir/*.so
/usr/include/*

%changelog
* Thu Sep 11 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4.0-alt1
- first build

