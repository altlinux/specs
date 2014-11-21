%define oname jsonrpcserver

%def_with python3
%def_without python2

Name: python-module-%oname
Version: 1.0.3
Release: alt1
Summary: JSON-RPC 2.0 server library
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonrpcserver
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jsonschema python-module-flask
BuildPreReq: python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jsonschema python3-module-flask
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
A JSON-RPC 2.0 server library for Python 3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A JSON-RPC 2.0 server library for Python 3.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JSON-RPC 2.0 server library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A JSON-RPC 2.0 server library for Python 3.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A JSON-RPC 2.0 server library for Python 3.

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
rm -fR build
py.test
%endif
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version
popd
%endif

%if_with python2
%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*_test.*

%files tests
%python_sitelibdir/*/*_test.*
%endif

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/*_test.*
#exclude %python3_sitelibdir/*/*/*_test.*

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*_test.*
#python3_sitelibdir/*/*/*_test.*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

