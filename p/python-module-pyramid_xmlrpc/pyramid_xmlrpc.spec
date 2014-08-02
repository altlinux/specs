%define oname pyramid_xmlrpc

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2
Summary: XML-RPC support for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_xmlrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires pyramid

%description
XML-RPC allows you to expose one or more methods at a particular URL.
`pyramid_xmlrpc` has a simple usage pattern for exposing a single method
at a particular url, and a more complicated one for when you want to
expose multiple methods at a particular URL.

%package -n python3-module-%oname
Summary: XML-RPC support for the Pyramid web framework
Group: Development/Python3
%py3_requires pyramid

%description -n python3-module-%oname
XML-RPC allows you to expose one or more methods at a particular URL.
`pyramid_xmlrpc` has a simple usage pattern for exposing a single method
at a particular url, and a more complicated one for when you want to
expose multiple methods at a particular URL.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_xmlrpc
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
XML-RPC allows you to expose one or more methods at a particular URL.
`pyramid_xmlrpc` has a simple usage pattern for exposing a single method
at a particular url, and a more complicated one for when you want to
expose multiple methods at a particular URL.

This package contains tests for pyramid_xmlrpc.

%package tests
Summary: Tests for pyramid_xmlrpc
Group: Development/Python
Requires: %name = %version-%release

%description tests
XML-RPC allows you to expose one or more methods at a particular URL.
`pyramid_xmlrpc` has a simple usage pattern for exposing a single method
at a particular url, and a more complicated one for when you want to
expose multiple methods at a particular URL.

This package contains tests for pyramid_xmlrpc.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

