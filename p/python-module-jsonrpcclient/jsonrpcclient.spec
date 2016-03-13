%define oname jsonrpcclient

%def_with python3
%def_without python2

Name: python-module-%oname
Version: 1.1.2
Release: alt2.1
Summary: JSON-RPC 2.0 client library for Python 3
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonrpcclient/
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-jsonschema
BuildPreReq: python-module-nose python-module-rednose
BuildPreReq: python-module-nose-cov python-module-responses
BuildPreReq: python-module-cov-core python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-jsonschema
BuildPreReq: python3-module-nose python3-module-rednose
BuildPreReq: python3-module-nose-cov python3-module-responses
BuildPreReq: python3-module-cov-core python3-module-coverage
%endif

%py_provides %oname

%description
JSON-RPC 2.0 client library for Python 3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JSON-RPC 2.0 client library for Python 3.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JSON-RPC 2.0 client library for Python 3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JSON-RPC 2.0 client library for Python 3.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JSON-RPC 2.0 client library for Python 3.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
rm -fR build
py.test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/*/*_test.*

#files tests
#python_sitelibdir/*/*_test.*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/*_test.*
#exclude %python3_sitelibdir/*/*/*_test.*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*_test.*
#python3_sitelibdir/*/*/*_test.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 1.1.2-alt2
- Rebuild into Sisyphus

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt1
- Version 1.0.12

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1
- Version 1.0.10

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Version 1.0.7

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus

