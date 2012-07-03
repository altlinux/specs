%define modulename python-memcached

Name: python-module-memcached
Version: 1.45
Release: alt1.1

Summary: A Python module for memcached daemon
Group: Development/Python
License: GPL
Url: ftp://ftp.tummy.com/pub/python-memcached/
Packager: Python Development Team <python at packages.altlinux.org>

%setup_python_module %modulename

Source: %modulename-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2005
BuildRequires: python-devel python-modules-compiler python-modules-encodings

BuildPreReq: python-module-setuptools

%description
%modulename is a Python module that interfaces to the memcached - 
distributed memory object caching system.

%prep
%setup

%build
export CFLAGS="%optflags"
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc README PKG-INFO ChangeLog *.html

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.45-alt1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.45-alt1
- Version 1.45 (ALT #17271)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.tummy5.2
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt2.tummy5.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt2.tummy5
- Build as noarch.

* Mon Nov 14 2005 LAKostis <lakostis at altlinux.ru> 1.2-alt1.tummy5
- First build for Sisyphus.

