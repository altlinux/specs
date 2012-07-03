%define oname zc.icp
Name: python-module-%oname
Version: 1.0.0
Release: alt2.1
Summary: Small, pluggable ICP (Internet Cache Protocol) server
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.icp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zope.component zope.interface zope.testing

%description
In multi-machine (or multi-process) web server installations some set of
web servers will likely be more able to quickly service an HTTP request
than others. HTTP accelerators (reverse proxies) like Squid can use ICP
queries to find the most appropriate server(s) to handle a particular
request. This package provides a small UDP server that can respond to
ICP queries based on pluggable policies.

%package tests
Summary: Tests for zc.icp
Group: Development/Python
Requires: %name = %version-%release

%description tests
In multi-machine (or multi-process) web server installations some set of
web servers will likely be more able to quickly service an HTTP request
than others. HTTP accelerators (reverse proxies) like Squid can use ICP
queries to find the most appropriate server(s) to handle a particular
request. This package provides a small UDP server that can respond to
ICP queries based on pluggable policies.

This package contains tests for zc.icp.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

