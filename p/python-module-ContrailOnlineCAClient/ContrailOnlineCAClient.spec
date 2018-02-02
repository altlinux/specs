# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20150320.1.1
%define oname ContrailOnlineCAClient

%def_disable check

Name: python-module-%oname
Version: 0.2.1
#Release: alt1.git20150320
Summary: Certificate Authority Web Service
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ContrailOnlineCAClient/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cedadev/online_ca_client.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools python-module-epydoc
BuildPreReq: python-module-ndg-httpsclient graphviz
BuildPreReq: python-modules-logging

%py_provides contrail.security.onlineca.client
%py_requires contrail.security.onlineca ndg.httpsclient logging

%description
Provides the client interface for an online Certificate Authority
web-service.

Web service calls can be made to request a certificate. The web service
interface is RESTful using GET and POST operations. To request a
certificate, a Certificate Signing Request is sent as a field with a
HTTP POST call. The service should be hosted over HTTPS. The client
authenticates using HTTP Basic Auth or SSL client authentication. In the
first case, username and password are sent. For the latter, at least a
username should be set as this needed to configure the subject name of
the certificate requested. If authentication succeeds, an X.509
certificate is returned.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Provides the client interface for an online Certificate Authority
web-service.

This package contains documentation for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides the client interface for an online Certificate Authority
web-service.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%make -C documentation

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.md
%python_sitelibdir/contrail/security/onlineca/client
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/contrail/security/onlineca/client/test

%files tests
%python_sitelibdir/contrail/security/onlineca/client/test

%files docs
%doc documentation/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.git20150320.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150320.1
- (AUTO) subst_x86_64.

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150320
- Initial build for Sisyphus

