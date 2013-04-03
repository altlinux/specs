%define oname ndg-httpsclient

Name: python-module-%oname
Version: 0.3.2
Release: alt1

Summary: Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/ndg-httpsclient/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-distribute python-module-epydoc

%setup_python_module %oname

Requires: python-module-ndg = %EVR

%description
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

%package tests
Summary: Tests for ndg-httpsclient
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

This package contains tests for ndg-httpsclient.

%package docs
Summary: Documentation for ndg-httpsclient
Group: Development/Documentation

%description docs
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

This package contains documentation for ndg-httpsclient.

%package -n python-module-ndg
Summary: Core module of ndg
Group: Development/Python

%description -n python-module-ndg
This package contains core module of ndg.

%prep
%setup

%build
%python_build_debug

%make -C documentation

%install
%python_install

touch %buildroot%python_sitelibdir/ndg/__init__.py

rm -f documentation/Makefile

%files
%doc LICENSE
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/ndg/__init__.py*

%files tests
%python_sitelibdir/*/*/test

%files docs
%doc documentation/*

%files -n python-module-ndg
%python_sitelibdir/ndg/__init__.py*

%changelog
* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

