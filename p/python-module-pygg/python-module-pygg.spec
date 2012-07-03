Name: python-module-pygg
Version: 0.4
Release: alt3.1

Summary: Python module intended to ease the usage of Glade with PyGTK

Group: Development/Python
License: LGPL
Url: http://www.univ-paris12.fr/lacl/pommereau/soft/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.univ-paris12.fr/lacl/pommereau/soft/PyGG-%version.tar.gz

BuildArch: noarch

%setup_python_module pygg

# manually removed: eric
# Automatically added by buildreq on Sat Nov 26 2005
BuildRequires: python-base python-modules-encodings

%description
PyGG (PyGTK and Glade) is a Python module intended to ease the usage of
Glade with PyGTK. It transparently handles the loading of Glade files
and the connection of callbacks.

%prep
%setup -q -n PyGG-%version

%build
%python_build

%install
%python_install

%files
%_bindir/*
%doc README NEWS TODO helloworld*
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt3.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt3
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt2
- Build as noarch.

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- updated 2007-05-14

* Sun Nov 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt0.1
- new version

* Sat Nov 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt0.1
- initial build for ALT Linux Sisyphus
