%define oname webhelpers

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt2
Summary: Helper functions intended to make writing templates in web applications easier
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/WebHelpers
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: WebHelpers-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sphinx-devel texlive-latex-recommended
BuildPreReq: python-module-sphinx-devel python-module-nose
BuildPreReq: python-module-routes python-module-webob
BuildPreReq: python-module-pysqlite2 python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Web Helpers is a library of helper functions intended to make writing
templates in web applications easier. It's the standard function library
for Pylons and TurboGears 2. It also contains a large number of
functions not specific to the web, including text processing, number
formatting, date calculations, container objects, etc.

%package -n python3-module-%oname
Summary: Helper functions intended to make writing templates in web applications easier
Group: Development/Python3

%description -n python3-module-%oname
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

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH=$PWD
touch tests/__init__.py
%make -C docs html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CHANGELOG LICENSE PKG-INFO *.txt TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files tests
%doc tests

%files docs
#doc docs/_build/latex/*.pdf
%doc docs/_build/html

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG LICENSE PKG-INFO *.txt TODO
%python3_sitelibdir/*
%endif

%changelog
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

