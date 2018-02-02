%define oname flask_jsontools

%def_with python3

Name: python-module-%oname
Version: 0.1.1.0
Release: alt1.git20141008.1.1
Summary: JSON API tools for Flask
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/flask_jsontools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kolypto/py-flask-jsontools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-flask python-module-nose
BuildPreReq: python-module-wheel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-flask python3-module-nose
BuildPreReq: python3-module-wheel
%endif

%py_provides %oname

%description
JSON API tools for Flask.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JSON API tools for Flask.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JSON API tools for Flask
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JSON API tools for Flask.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JSON API tools for Flask.

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
%make test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
%make test3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1.0-alt1.git20141008.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1.0-alt1.git20141008.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1.0-alt1.git20141008
- Initial build for Sisyphus

