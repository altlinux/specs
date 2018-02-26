Name: PythonCAD
Version: 0.1.36
Release: alt2.1.qa1.1

%define tarname %name-DS1-R36

Summary: An open-source CAD package built designed around Python

License: GPL
Group: Graphics
Url: http://www.pythoncad.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.pythoncad.org/releases/%tarname.tar.bz2

# manually removed: eric
# Automatically added by buildreq on Sat Jan 06 2007
BuildRequires: python-devel python-modules-encodings

BuildPreReq: rpm-build-compat >= 1.2
%add_python_req_skip AppKit Foundation Generic PyObjCTools objc PythonCAD
AutoProv: yes, nopython

BuildArch: noarch
BuildRequires: desktop-file-utils

%description
PythonCAD is an open-source CAD package built designed around Python.
As such, it aims to be a fully scriptable and customizable CAD
program. It is initially designed to run under Linux, one of the BSD
flavors, or Unix.

%prep
%setup -q -n %tarname

%build
%python_build

%install
install -d %buildroot%_bindir
%python_install

install gtkpycad.py %buildroot%_bindir/pycad
mkdir -p %buildroot{%_pixmapsdir,%_sysconfdir/pythoncad,%_desktopdir}
cp prefs.py %buildroot%_sysconfdir/pythoncad/
cat pythoncad.desktop | sed -e "s|gtkpycad.py|pycad|" > %buildroot%_desktopdir/%name.desktop
cp gtkpycad.png %buildroot%_pixmapsdir/
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=Engineering \
	%buildroot%_desktopdir/PythonCAD.desktop

%files
%doc README NEWS
%_bindir/pycad
%python_sitelibdir/%name/
%_desktopdir/*
%_pixmapsdir/*
%_sysconfdir/pythoncad/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.36-alt2.1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.36-alt2.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for PythonCAD

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.36-alt2.1
- Rebuilt with python 2.6

* Sat Dec 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.36-alt2
- fix exec name in desktop (bug #18200)
- use python build/install macroses

* Tue Jul 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.36-alt1
- new version 0.1.36 (with rpmrb script)

* Sat Jan 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.35-alt1
- new version (0.1.35)
- replace menu file with desktop file

* Fri Feb 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.28-alt1
- new version

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1.23-alt1
- rebuild with python 2.4

* Sun Dec 26 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.20-alt1
- new version

* Fri Dec 03 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1.19-alt1
- first build for ALT Linux Sisyphus (original spec from PLD)

