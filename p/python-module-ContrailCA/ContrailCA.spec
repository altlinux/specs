# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define oname ContrailCA

%def_disable check

Name: python-module-%oname
Version: 0.1.0
#Release: alt1
Summary: Certificate Authority
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ContrailCA/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-module-pyasn1
BuildPreReq: python-module-ndg-httpsclient python-module-OpenSSL
BuildPreReq: python-modules-logging

%py_provides contrail.security.ca
Requires: python-module-contrail.security = %EVR
%py_requires ndg.httpsclient pyasn1 logging OpenSSL

%description
Provides a simple implementation of a Certificate Authority. It uses the
PyOpenSSL for bindings to OpenSSL but also includes the ability to
callout direct to an openssl command for more fine-grained control over
the certificate issuing process if required.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides a simple implementation of a Certificate Authority. It uses the
PyOpenSSL for bindings to OpenSSL but also includes the ability to
callout direct to an openssl command for more fine-grained control over
the certificate issuing process if required.

This package contains tests for %oname.

%package -n python-module-contrail.security
Summary: Core files of contrail.security
Group: Development/Python
%py_provides contrail.security
Requires: python-module-contrail = %EVR

%description -n python-module-contrail.security
Core files of contrail.security.

%package -n python-module-contrail
Summary: Core files of contrail
Group: Development/Python
%py_provides contrail

%description -n python-module-contrail
Core files of contrail.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/contrail/security/ca
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/contrail/security/ca/test

%files tests
%python_sitelibdir/contrail/security/ca/test

%files -n python-module-contrail.security
%dir %python_sitelibdir/contrail/security
%python_sitelibdir/contrail/security/__init__.py*

%files -n python-module-contrail
%dir %python_sitelibdir/contrail
%python_sitelibdir/contrail/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.1
- (AUTO) subst_x86_64.

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

