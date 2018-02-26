%define oname python-utmp
Name: python-module-utmp
Version: 0.7
Release: alt1.1.2.1.1

Summary: Python module for working with utmp

License: GPL
Group: Development/Python
Url: http://melkor.dnp.fmph.uniba.sk/~garabik/python-utmp/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://melkor.dnp.fmph.uniba.sk/~garabik/python-utmp/python-utmp_%version.tar.bz2
Patch: %name.patch

# Automatically added by buildreq on Wed Jan 16 2008
BuildRequires: python-devel

%description
This package provides 3 python modules to access utmp and wtmp
records.  utmpaccess is lowlevel module wrapping glibc functions,
UTMPCONST provides useful constants, and utmp is module build on top
of utmpaccess module, providing object oriented interface.

%prep
%setup -n %oname-%version
%patch

%build
%make_build -f Makefile.glibc \
	PYTHONVER="%_python_version" \
	PYTHONDIR="%python_sitelibdir"

%install
%makeinstall -f Makefile.glibc \
	PYTHONVER="%_python_version" \
	PYTHONDIR="%buildroot%python_sitelibdir"

%files
%doc README TODO examples/*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1.2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.1.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.1.1
- Rebuilt with python 2.6

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.7-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- initial build for ALT Linux Sisyphus

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1.2 #4303
- Rebuild for Fedora Core 5.

* Wed Jan 05 2005 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
