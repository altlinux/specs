Name: qwit
Version: 1.1
Release: alt0.pre2
URL: http://code.google.com/p/qwit/
Source: %name-%version.tar.gz

Summary: Qt4 cross-platform client for Twitter
License: GPLv3
Group: Networking/Instant messaging
Packager: Sergey Irupin <lamp@altlinux.org>

BuildRequires: libqt4-devel gcc-c++ qoauth-devel

%description
Qt4 cross-platform client for Twitter

%prep
%setup

%build
%_libdir/qt4/bin/qmake
%make_build
%_libdir/qt4/bin/lrelease translations/*.ts

%install
mkdir -p %buildroot%_datadir/%name/
install -D %name %buildroot%_bindir/%name
install translations/*.qm %buildroot%_datadir/%name/
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -D images/%name.png %buildroot%_niconsdir/%name.png

%files
%doc AUTHORS COPYING INSTALL README
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_niconsdir/%name.png

%post

%postun

%changelog
* Thu Mar 03 2011 Anton Farygin <rider@altlinux.ru> 1.1-alt0.pre2
- new version

* Mon May 24 2010 Sergey Irupin <lamp@altlinux.org> 0.9-alt1
- Initial build for ALT Linux

