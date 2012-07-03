%define oname GnuPGInterface
Name: python-module-%oname
Version: 0.3.2
Release: alt2.1

Summary: A Python module to interface with GnuPG

License: LGPL
Group: Development/Python
Url: http://py-gnupg.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://dl.sf.net/py-gnupg/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Sun Oct 28 2007
BuildRequires: python-devel python-modules-compiler

%description
GnuPGInterface is a Python module to interface with GnuPG. It concentrates
on interacting with GnuPG via filehandles, providing access to control
GnuPG via versatile and extensible means.

%prep
%setup -q -n %oname-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%doc NEWS README THANKS
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.3.2-alt1.1
- Rebuilt with python-2.5.

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus
