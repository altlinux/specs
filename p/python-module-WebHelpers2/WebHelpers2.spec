%define oname WebHelpers2

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.0
Release: alt2.git20150117.1.1
Summary: Functions for web apps: generating HTML tags, showing results a pageful at a time, etc.
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/WebHelpers2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mikeorr/WebHelpers2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-markupsafe python-module-six
BuildPreReq: python-module-tox python-module-wheel
BuildPreReq: python-module-unidecode
BuildPreReq: python-module-sphinx-devel pylons_sphinx_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-markupsafe python3-module-six
BuildPreReq: python3-module-tox python3-module-wheel
BuildPreReq: python3-module-unidecode
%endif

%py_provides webhelpers2
Provides: python-module-webhelpers2 = %EVR

%description
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Functions for web apps: generating HTML tags, showing results a pageful at a time, etc.
Group: Development/Python3
%py3_provides webhelpers2
Provides: python3-module-webhelpers2 = %EVR

%description -n python3-module-%oname
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
WebHelpers2 is the successor to the widely-used WebHelpers utilities. It
contains convenience functions to make HTML tags, process text, format
numbers, do basic statistics, work with collections, and more.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
python setup.py test
%if_with python3
pushd ../python3
rm -fR build
python3 setup.py test
popd
%endif

%files
%doc CHANGELOG README.*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README.*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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

