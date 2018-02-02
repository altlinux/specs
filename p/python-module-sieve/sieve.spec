%define oname sieve

%def_with python3

Name: python-module-%oname
Version: 0.1.9
Release: alt1.git20130911.1.1
Summary: XML Comparison Utils
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sieve/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ralphbean/sieve.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-lxml python-module-six
BuildPreReq: python-module-markupsafe python-module-nose
BuildPreReq: python-modules-multiprocessing python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-lxml python3-module-six
BuildPreReq: python3-module-markupsafe python3-module-nose
%endif

%py_provides %oname
%py_requires lxml six markupsafe

%description
XML Comparison Utils.

Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
XML Comparison Utils.

Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: XML Comparison Utils
Group: Development/Python3
%py3_provides %oname
%py3_requires lxml six markupsafe

%description -n python3-module-%oname
XML Comparison Utils.

Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
XML Comparison Utils.

Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.9-alt1.git20130911.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9-alt1.git20130911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.git20130911
- Initial build for Sisyphus

