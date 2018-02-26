%define oname pyramid_xmlrpc
Name: python-module-%oname
Version: 0.1
Release: alt1.1
Summary: XML-RPC support for the Pyramid web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_xmlrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid

%description
XML-RPC allows you to expose one or more methods at a particular URL.
`pyramid_xmlrpc` has a simple usage pattern for exposing a single method
at a particular url, and a more complicated one for when you want to
expose multiple methods at a particular URL.

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

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

