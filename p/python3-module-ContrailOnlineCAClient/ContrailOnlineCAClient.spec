%define oname ContrailOnlineCAClient

%def_without docs

Name: python3-module-%oname
Version: 0.5.1
Release: alt1

Summary: Certificate Authority Web Service
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/ContrailOnlineCAClient/

# https://github.com/cedadev/online_ca_client.git
Source: %name-%version.tar
Patch0: fix-concat-types.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-requests-oauthlib python3-module-requests

%add_python3_req_skip requests.packages.urllib3.exceptions


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

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Provides the client interface for an online Certificate Authority
web-service.

This package contains documentation for %oname.
%endif

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Provides the client interface for an online Certificate Authority
web-service.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%if_with docs
%make -C documentation
%endif

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/contrail/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/contrail/security/onlineca/client/test

%files tests
%python3_sitelibdir/contrail/security/onlineca/client/test

%if_with docs
%files docs
%doc documentation/*
%endif


%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt1
- Version updated to 0.5.1
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.git20150320.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150320.1
- (AUTO) subst_x86_64.

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150320
- Initial build for Sisyphus

