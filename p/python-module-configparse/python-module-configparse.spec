%define oname configparse
Name: python-module-%oname
Version: 0.3
Release: alt2.1

Summary: A configfile and command-line parsing library based on optparse

License: BSD
Group: Development/Python
Url: http://www.gustaebel.de/lars/configparse/

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://www.gustaebel.de/lars/configparse/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module %oname

# Automatically added by buildreq on Sat Oct 13 2007
BuildRequires: python-devel python-modules-compiler python-modules-encodings

%description
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%prep
%setup -q -n %oname-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.3-alt1.1
- Rebuilt with python-2.5.

* Sat Oct 13 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
