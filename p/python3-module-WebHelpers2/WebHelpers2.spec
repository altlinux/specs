%define oname WebHelpers2

%def_disable check

Name: python3-module-%oname
Version: 2.0
Release: alt3.git20150117
Summary: Functions for web apps: generating HTML tags, showing results a pageful at a time, etc.
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/WebHelpers2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mikeorr/WebHelpers2.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-markupsafe python3-module-six
BuildPreReq: python3-module-tox python3-module-wheel pylons_sphinx_theme
BuildPreReq: python3-module-unidecode python3-module-sphinx

%py3_provides webhelpers2
Provides: python3-module-webhelpers2 = %EVR

%description
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc CHANGELOG README.*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 2.0-alt3.git20150117
- Transfer on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0-alt2.git20150117.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.git20150117
- Version 2.0

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.rc3.git20150113
- Version 2.0rc3

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.rc2.git20141111
- Version 2.0rc2

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.rc1.git20141005
- Initial build for Sisyphus

