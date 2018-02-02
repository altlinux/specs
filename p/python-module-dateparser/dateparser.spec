%define oname dateparser

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141125.1.1
Summary: Python parser for human readable dates 
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dateparser
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/scrapinghub/dateparser.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-nose-parameterized python-module-wheel
BuildPreReq: python-module-dateutil
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-nose-parameterized python3-module-wheel
BuildPreReq: python3-module-dateutil
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Date parsing library designed to parse dates from HTML pages.

%package -n python3-module-%oname
Summary: Python parser for human readable dates
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Date parsing library designed to parse dates from HTML pages.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Date parsing library designed to parse dates from HTML pages.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Date parsing library designed to parse dates from HTML pages.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.git20141125.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141125.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141125
- Initial build for Sisyphus

