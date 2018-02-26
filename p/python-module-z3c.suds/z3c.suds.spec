%define oname z3c.suds
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Manages a pool of suds SOAP clients within the context of a Zope application
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.suds/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires suds

%description
z3c.suds manages a connection pool of suds client objects in the context
of a ZODB-based application. (suds is a lightweight client library for
consuming SOAP web services in Python.) Using it avoids the need for
instantiating a new client for the same webservice in multiple requests
(which may be expensive due to parsing WSDL, etc.)

%package tests
Summary: Tests for z3c.suds
Group: Development/Python
Requires: %name = %version-%release

%description tests
z3c.suds manages a connection pool of suds client objects in the context
of a ZODB-based application. (suds is a lightweight client library for
consuming SOAP web services in Python.) Using it avoids the need for
instantiating a new client for the same webservice in multiple requests
(which may be expensive due to parsing WSDL, etc.)

This package contains tests for z3c.suds.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

