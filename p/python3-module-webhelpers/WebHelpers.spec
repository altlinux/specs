%define oname webhelpers

Name: python3-module-%oname
Version: 1.3
Release: alt3
Summary: Helper functions intended to make writing templates in web applications easier
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/WebHelpers

Source: WebHelpers-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: /usr/bin/2to3

%description
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier. It's the standard function library
for Pylons and TurboGears 2. It also contains a large number of
functions not specific to the web, including text processing, number
formatting, date calculations, container objects, etc.

%package tests
Summary: Tests for Web Helpers
Group: Development/Python3
BuildArch: noarch
Requires: %name = %version-%release

%description tests
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier. It's the standard function library
for Pylons and TurboGears 2. It also contains a large number of
functions not specific to the web, including text processing, number
formatting, date calculations, container objects, etc.

This package contains tests for Web Helpers.

%package docs
Summary: Documentation for Web Helpers
Group: Development/Documentation
BuildArch: noarch

%description docs
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier. It's the standard function library
for Pylons and TurboGears 2. It also contains a large number of
functions not specific to the web, including text processing, number
formatting, date calculations, container objects, etc.

This package contains documentation for Web Helpers.

%package pickles
Summary: Pickles for Web Helpers
Group: Development/Python3
BuildArch: noarch

%description pickles
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier. It's the standard function library
for Pylons and TurboGears 2. It also contains a large number of
functions not specific to the web, including text processing, number
formatting, date calculations, container objects, etc.

This package contains pickles for Web Helpers.

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build

export PYTHONPATH=$PWD
touch tests/__init__.py
%make SPHINXBUILD="sphinx-build-3" -C docs html

%install
%python3_install

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc CHANGELOG LICENSE PKG-INFO *.txt TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/pickle

%files tests
%doc tests

%files docs
#doc docs/_build/latex/*.pdf
%doc docs/_build/html

%files pickles
%python3_sitelibdir/%oname/pickle

%changelog
* Thu Jun 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.3-alt3
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt2.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt2.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Rebuilt with python-module-sphinx-devel

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Wed Jul 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Version 1.0
- Added tests and docs

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

