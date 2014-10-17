%define oname WSGIProxy2

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.2
Release: alt1.dev0.git20131221
Summary: A WSGI Proxy with various http client backends
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/WSGIProxy2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gawel/WSGIProxy2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-webob python-module-six
BuildPreReq: python-module-restkit python-module-http-parser
BuildPreReq: python-module-urllib3 python-module-requests
BuildPreReq: python-module-webtest python-module-nose
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-webob python3-module-six
BuildPreReq: python3-module-restkit python3-module-http-parser
BuildPreReq: python3-module-urllib3 python3-module-requests
BuildPreReq: python3-module-webtest python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides wsgiproxy
Conflicts: python-module-wsgiproxy

%description
A WSGI Proxy with various http client backends.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A WSGI Proxy with various http client backends
Group: Development/Python3
%py3_provides wsgiproxy
Conflicts: python3-module-wsgiproxy

%description -n python3-module-%oname
A WSGI Proxy with various http client backends.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A WSGI Proxy with various http client backends.

This package contains tests for %oname.

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
%make -C docs html

%check
nosetests
#if_with python3
%if 0
pushd ../python3
nosetests3
popd
%endif

%files
%doc *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.dev0.git20131221
- Initial build for Sisyphus

