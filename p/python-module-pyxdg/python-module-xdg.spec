Version: 0.19
Release: alt1.1
%setup_python_module pyxdg
Name: %packagename

Summary: Implementations of freedesktop.org standards in python
License: LGPLv2
Group: Development/Python
URL: http://freedesktop.org/Software/pyxdg

Source0: http://www.freedesktop.org/~lanius/%modulename-%version.tar.gz

Packager: Python Development Team <python@packages.altlinux.org>

BuildArch: noarch

Provides: pyxdg = %version-%release

# Automatically added by buildreq on Sat Sep 29 2007 (-bi)
BuildRequires: python-devel python-modules-compiler

%description
PyXDG contains implementations of freedesktop.org standards in python.

%prep
%setup -q -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS ChangeLog README TODO
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.19-alt1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19-alt1
- Version 0.19

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.1
- Rebuilt with python 2.6

* Tue Jun 02 2009 Fr. Br. George <george@altlinux.ru> 0.17-alt1
- Version up

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.15-alt1.1
- Rebuilt with python-2.5.

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 0.15-alt1
- build for Sisyphus

