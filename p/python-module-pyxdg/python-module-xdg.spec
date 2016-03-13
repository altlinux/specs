Version: 0.25
Release: alt1.1
%setup_python_module pyxdg
Name: %packagename

Summary: Implementations of freedesktop.org standards in Python
License: LGPLv2
Group: Development/Python
URL: http://freedesktop.org/Software/pyxdg

Source0: %modulename-%version.tar

Packager: Python Development Team <python@packages.altlinux.org>

BuildArch: noarch

Provides: pyxdg = %version-%release

# Automatically added by buildreq on Sat Sep 29 2007 (-bi)
BuildRequires: python-devel python-modules-compiler

# Build dependencies specific to Python 3
BuildRequires: rpm-build-python3 python3-devel

%description
PyXDG contains implementations of freedesktop.org standards in Python.

%package -n python3-module-%modulename
Summary: Implementations of freedesktop.org standards in Python 3
Group: Development/Python3

%description -n python3-module-%modulename
PyXDG contains implementations of freedesktop.org standards in Python 3.

%prep
%setup -n %modulename-%version
%setup -D -c -n %modulename-%version
mv %modulename-%version py3build

%build
%python_build
pushd py3build
%python3_build

%install
%python_install
pushd py3build
%python3_install

%files
%doc AUTHORS ChangeLog README TODO
%python_sitelibdir/*

%files -n python3-module-%modulename
%doc AUTHORS ChangeLog README TODO
%python3_sitelibdir/*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.25-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 11 2013 Paul Wolneykien <manowar@altlinux.org> 0.25-alt1
- Dual build: python + python3.
- Use plain tar packaging.
- Fresh up to v0.25 with the help of cronbuild and update-source-functions.

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

