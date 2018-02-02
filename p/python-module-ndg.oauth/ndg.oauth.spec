# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20131210.1.1
%define mname ndg
%define oname %mname.oauth
Name: python-module-%oname
Version: 0.5.1
#Release: alt1.git20131210
Summary: Python OAuth 2.0 Implementation including client and server packages
License: BSD
Group: Development/Python
# in pypi:
# https://pypi.python.org/pypi/ndg-oauth-server/
# https://pypi.python.org/pypi/ndg-oauth-client/
Url: https://github.com/cedadev/ndg_oauth
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cedadev/ndg_oauth.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-ndg-httpsclient python-module-PasteScript
BuildPreReq: python-module-beaker python-module-webob
BuildPreReq: python-module-OpenSSL python-module-pyasn1
BuildPreReq: python-module-repoze.who python-module-genshi
BuildPreReq: python-module-nose python-module-PasteDeploy
BuildPreReq: python-modules-json python-modules-logging

%py_provides %oname
%py_requires %mname
# for client:
%py_requires ndg.httpsclient paste.script beaker webob OpenSSL json
%py_requires logging
# for server:
%py_requires repoze.who genshi json logging paste.deploy
# for server examples:
%py_requires contrail.security.onlineca.server

%description
This is a core package of OAuth 2.0 server and client libraries.

These include WSGI wrappers for easy integration with Python frameworks
such as Pylons/Pyramid or Django.

%package -n python-module-%oname.server
Summary: OAuth 2.0 server
Group: Development/Python
%py_provides %oname.server
Requires: %name = %EVR

%description -n python-module-%oname.server
This is an OAuth 2.0 server library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added for a specialised use case to enable a SLCS (Short-lived
Credential Service) to issue delegated X.509-based credentials with
OAuth.

%package -n python-module-%oname.server.examples
Summary: Examples for OAuth 2.0 server
Group: Development/Python
%py_provides %oname.server.examples
Requires: python-module-%oname.server = %EVR

%description -n python-module-%oname.server.examples
This is an OAuth 2.0 server library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added for a specialised use case to enable a SLCS (Short-lived
Credential Service) to issue delegated X.509-based credentials with
OAuth.

This package contains examples for %oname.server.

%package -n python-module-%oname.client
Summary: OAuth 2.0 client
Group: Development/Python
%py_provides %oname.client
Requires: %name = %EVR

%description -n python-module-%oname.client
This is an OAuth 2.0 client library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added to enable a SLCS (Short-lived Credential Service) to issue
delegated X.509-based credentials using OAuth.

%package -n python-module-%oname.client.examples
Summary: Examples for OAuth 2.0 client
Group: Development/Python
%py_provides %oname.client.examples
Requires: python-module-%oname.client = %EVR

%description -n python-module-%oname.client.examples
This is an OAuth 2.0 client library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added to enable a SLCS (Short-lived Credential Service) to issue
delegated X.509-based credentials using OAuth.

This package contains examples for %oname.client.

%prep
%setup

%build
for i in ndg_oauth_server ndg_oauth_client; do
	pushd $i
	%python_build_debug
	popd
done

%install
for i in ndg_oauth_server ndg_oauth_client; do
	pushd $i
	%python_install
	popd
done

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
for i in ndg_oauth_server ndg_oauth_client; do
	pushd $i
	python setup.py test
	popd
done

%files
%doc README.md
%dir %python_sitelibdir/ndg/oauth
%python_sitelibdir/ndg/oauth/__init__.py*

%files -n python-module-%oname.server
%python_sitelibdir/ndg/oauth/server
%python_sitelibdir/ndg_oauth_server*.egg-info
%exclude %python_sitelibdir/ndg/oauth/server/examples
%exclude %python_sitelibdir/ndg/oauth/server/*/*/test*

%files -n python-module-%oname.server.examples
%python_sitelibdir/ndg/oauth/server/examples
%python_sitelibdir/ndg/oauth/server/*/*/test*

%files -n python-module-%oname.client
%python_sitelibdir/ndg/oauth/client
%python_sitelibdir/ndg_oauth_client*.egg-info
%exclude %python_sitelibdir/ndg/oauth/client/examples

%files -n python-module-%oname.client.examples
%python_sitelibdir/ndg/oauth/client/examples

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20131210.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20131210.1
- (AUTO) subst_x86_64.

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20131210
- Initial build for Sisyphus

