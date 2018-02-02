%define oname hawkauthlib

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20131112.1.1
Summary: Low-level library for implementing MAC Access Authentication
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/hawkauthlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mozilla-services/hawkauthlib.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-webob python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-webob python3-module-requests
%endif

%py_provides %oname

%description
This is a low-level library for implementing Hawk Access Authentication,
a simple HTTP request-signing scheme described in:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and a secret
key. They use these credentials to make signed requests to the server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a low-level library for implementing Hawk Access Authentication,
a simple HTTP request-signing scheme described in:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and a secret
key. They use these credentials to make signed requests to the server.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Low-level library for implementing MAC Access Authentication
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is a low-level library for implementing Hawk Access Authentication,
a simple HTTP request-signing scheme described in:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and a secret
key. They use these credentials to make signed requests to the server.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a low-level library for implementing Hawk Access Authentication,
a simple HTTP request-signing scheme described in:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and a secret
key. They use these credentials to make signed requests to the server.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.git20131112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20131112.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20131112
- Initial build for Sisyphus

