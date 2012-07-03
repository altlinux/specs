%define oname webhelpers
Name: python-module-%oname
Version: 1.3
Release: alt1.1
Summary: Helper functions intended to make writing templates in web applications easier
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/WebHelpers
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: WebHelpers-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel texlive-latex-recommended

%description
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier. It's the standard function library
for Pylons and TurboGears 2. It also contains a large number of
functions not specific to the web, including text processing, number
formatting, date calculations, container objects, etc.

%package tests
Summary: Tests for Web Helpers
Group: Development/Python
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
Group: Development/Python
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

%prepare_sphinx docs

%build
%python_build

export PYTHONPATH=$PWD
%make -C docs latex

%install
%python_install

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG LICENSE PKG-INFO *.txt TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%doc tests

%files docs
%doc docs/_build/latex/*.pdf
%doc docs/_build/html

%files pickles
%python_sitelibdir/%oname/pickle

%changelog
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

