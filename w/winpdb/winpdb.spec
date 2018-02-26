Summary: The frontend to an advanced Python debugger (rpdb2).
Name: winpdb
Version: 1.4.8
Release: alt2.1
%setup_python_module %name
Source0: http://winpdb.googlecode.com/files/%name-%version.tar.gz
Source1: %name.desktop
License: GPL
Group: Development/Python
BuildArch: noarch
URL: http://winpdb.org/
Packager: Fr. Br. George <george@altlinux.ru>

%description
Winpdb is a GUI frontend to rpdb2 -- an advanced Python debugger with
smart breakpoints, thread support, modifiable namespace, and secure
connections.

%package -n rpdb2
Summary: An advanced Python debugger.
Group: Development/Python

%description -n rpdb2
Rpdb2 is an advanced Python debugger with smart breakpoints, 
thread support, modifiable namespace, and secure connections.

%prep
%setup  -q

%build
%python_build

%install
%python_install
for N in 16 32 64; do install -D artwork/%name-icon-$N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name-icon-$N.png; done
install -D artwork/%name-icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name-icon.svg
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/winpdb
%python_sitelibdir/winpdb.py*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%files -n rpdb2
%_bindir/rpdb2
%python_sitelibdir/rpdb2.py*
%doc README.txt

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.8-alt2.1
- Rebuild with Python-2.7

* Wed Apr 13 2011 Paul Wolneykien <manowar@altlinux.ru> 1.4.8-alt2
- Split up the package into GUI and CLI parts.

* Wed Aug 25 2010 Fr. Br. George <george@altlinux.ru> 1.4.8-alt1
- Version up

* Tue Dec 01 2009 Fr. Br. George <george@altlinux.ru> 1.4.6-alt1
- Version up

* Sun Jan 04 2009 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Version up
- Stupid desktop bug fixed

* Thu Sep 25 2008 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Version up

* Sat Sep 09 2006 Fr. Br. George <george@altlinux.ru> 1.0.6-alt1
- Initial release

