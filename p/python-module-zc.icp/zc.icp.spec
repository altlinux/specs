%define oname zc.icp

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt3.1
Summary: Small, pluggable ICP (Internet Cache Protocol) server
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.icp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc zope.component zope.interface zope.testing

%description
In multi-machine (or multi-process) web server installations some set of
web servers will likely be more able to quickly service an HTTP request
than others. HTTP accelerators (reverse proxies) like Squid can use ICP
queries to find the most appropriate server(s) to handle a particular
request. This package provides a small UDP server that can respond to
ICP queries based on pluggable policies.

%package -n python3-module-%oname
Summary: Small, pluggable ICP (Internet Cache Protocol) server
Group: Development/Python3
%py3_requires zc zope.component zope.interface zope.testing

%description -n python3-module-%oname
In multi-machine (or multi-process) web server installations some set of
web servers will likely be more able to quickly service an HTTP request
than others. HTTP accelerators (reverse proxies) like Squid can use ICP
queries to find the most appropriate server(s) to handle a particular
request. This package provides a small UDP server that can respond to
ICP queries based on pluggable policies.

%package -n python3-module-%oname-tests
Summary: Tests for zc.icp
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
In multi-machine (or multi-process) web server installations some set of
web servers will likely be more able to quickly service an HTTP request
than others. HTTP accelerators (reverse proxies) like Squid can use ICP
queries to find the most appropriate server(s) to handle a particular
request. This package provides a small UDP server that can respond to
ICP queries based on pluggable policies.

This package contains tests for zc.icp.

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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
rm -f %buildroot%python3_sitelibdir/*/__init__.py
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

