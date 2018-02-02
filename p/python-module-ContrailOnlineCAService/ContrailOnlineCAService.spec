# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20141211.1.1
%define oname ContrailOnlineCAService

%def_disable check

Name: python-module-%oname
Version: 0.1.1
#Release: alt1.git20141211
Summary: Certificate Authority Web Service
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ContrailOnlineCAService/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cedadev/online_ca_service.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-module-ContrailCA
BuildPreReq: python-module-PasteScript python-module-webob
BuildPreReq: python-module-repoze.who python-module-epydoc
BuildPreReq: python-module-PasteDeploy
BuildPreReq: python-modules-logging

%py_provides contrail.security.onlineca.server
Requires: python-module-contrail.security.onlineca = %EVR
Requires: python-module-ContrailCA
%py_requires paste.script webob repoze.who logging paste.deploy

%description
Provides a simple web service interface to a Certificate Authority. This
is suitable for use as a SLCS (Short-Lived Credential Service).

The interface is implemented as a WSGI application which fronts a
Certificate Authority.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides a simple web service interface to a Certificate Authority. This
is suitable for use as a SLCS (Short-Lived Credential Service).

The interface is implemented as a WSGI application which fronts a
Certificate Authority.

This package contains tests for %oname.

%package -n python-module-contrail.security.onlineca
Summary: Core files of python-module-contrail.security.onlineca
Group: Development/Python
%py_provides contrail.security.onlineca
%py_requires contrail.security

%description -n python-module-contrail.security.onlineca
Core files of python-module-contrail.security.onlineca.

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
%doc *.md
%python_sitelibdir/contrail/security/onlineca/server
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/contrail/security/onlineca/server/test

%files tests
%python_sitelibdir/contrail/security/onlineca/server/test

%files -n python-module-contrail.security.onlineca
%dir %python_sitelibdir/contrail/security/onlineca
%python_sitelibdir/contrail/security/onlineca/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.git20141211.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20141211.1
- (AUTO) subst_x86_64.

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141211
- Initial build for Sisyphus

