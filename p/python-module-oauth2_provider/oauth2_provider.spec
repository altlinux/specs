%define oname oauth2_provider

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0
Release: alt1.git20120909
Summary: Python implementation of the server side of OAUTH2 spec
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/oauth2_provider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eventray/oauth2_provider.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-webtest
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Python implementation of the server side of OAUTH2 spec.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Python implementation of the server side of OAUTH2 spec.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python implementation of the server side of OAUTH2 spec
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python implementation of the server side of OAUTH2 spec.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Python implementation of the server side of OAUTH2 spec.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt1.git20120909
- Initial build for Sisyphus

