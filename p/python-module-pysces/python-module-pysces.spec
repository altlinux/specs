%define oname PyCClass
Name: python-module-pysces
Version: 0.5.2
Release: alt3.1

Summary: Making object oriented python bindings to an object oriented C API

License: GPL
Group: Development/Python
Url: http://www.nongnu.org/pysces/

Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://download.savannah.nongnu.org/releases/pysces/%oname-%version.tar.bz2

BuildArch: noarch

%setup_python_module pysces

# Automatically added by buildreq on Tue Mar 20 2007
BuildRequires: python-devel python-modules-encodings

%description
PyCClass is a library to aid in the task of making object
oriented python bindings to an object oriented C API.

%prep
%setup -q -n %oname-%version

%build
CFLAGS="%optflags" python setup.py build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt3.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt3
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.5.2-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.5.2-alt2
- Build as noarch.

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial build for ALT Linux Sisyphus
