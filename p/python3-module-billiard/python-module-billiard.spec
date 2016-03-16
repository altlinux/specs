Name: python3-module-billiard
Version: 3.4.0.0
Release: alt2.a1.git20141013.1

Summary: billiard is a fork of the Python 2.7 multiprocessing package
Source: %name-%version.tar
BuildArch: noarch
License: GPL
Group: Development/Python3
Url: https://github.com/celery/billiard/

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel gcc-c++ python-module-sphinx-devel
BuildPreReq: python3-module-setuptools

%description
billiard is a fork of the Python 2.7 multiprocessing package.
The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package. This standalone variant is intended
to be compatible with Python 2.4 and 2.5, and will draw it's
fixes/improvements from python-trunk.

%package tests
Summary: Tests for billiard
Group: Development/Python3
Requires: %name = %EVR

%description tests
billiard is a fork of the Python 2.7 multiprocessing package.
The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package. This standalone variant is intended
to be compatible with Python 2.4 and 2.5, and will draw it's
fixes/improvements from python-trunk.

This package contains tests for billiard.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv Doc/

%build
#rm -f billiard/tests/test_multiprocessing.py
%python3_build
python setup.py build_sphinx --builder="html" --source-dir=Doc

%install
mv build/sphinx/html html
%python3_install

%files
%doc html LICENSE.txt CHANGES.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/funtests
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0.0-alt2.a1.git20141013.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.0-alt2.a1.git20141013
- New snapshot

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0.0-alt2.a1.git20140528
- Initial build for Sisyphus

