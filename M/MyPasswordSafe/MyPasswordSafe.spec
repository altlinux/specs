Name: MyPasswordSafe
Version: 20061216
Release: alt3.1
Summary: Password Safe
Url: http://freshmeat.net/projects/myps/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://freshmeat.net/projects/myps/%name-%version.tar.bz2
Patch0: %name-Makefile.patch
Patch1: %name-qmake-alt.patch
License: GPL
Group: Databases
BuildRequires: libqt3-devel gcc-c++ libXScrnSaver-devel

%description
MyPasswordSafe is a straightforward, easy-to-use password
keychain/manager that uses the Blowfish algorithm to store
encrypted passwords. It uses the same file format as Password Safe.

%prep
%setup -q -n %name-%version
%patch0
%patch1 -p1

%build
make PREFIX=%buildroot/usr QTDIR=%_libdir/qt3

%install
%makeinstall PREFIX=%buildroot/usr QTDIR=%_libdir/qt3

%files
%_bindir/MyPasswordSafe
%_datadir/MyPasswordSafe/locale/*
%doc COPYING ChangeLog CHANGES README
%doc doc/*.html

%changelog
* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20061216-alt3.1
- Fixed build

* Mon May 11 2009 Denis Klimov <zver@altlinux.org> 20061216-alt3
- fixes build by gcc4.4

* Mon Dec 15 2008 Denis Klimov <zver@altlinux.org> 20061216-alt2
- fixes build by gcc4.3

* Wed Oct 17 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 20061216-alt1
- Initial build for ALT

* Wed Jan 15 2005 Zalavary Gabor <gabor@zalavary> 20050615
- Initial build.
