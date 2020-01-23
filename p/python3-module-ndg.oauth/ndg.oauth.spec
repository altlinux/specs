%define mname ndg
%define oname %mname.oauth

Name: python3-module-%oname
Version: 0.5.1
Release: alt2

Summary: Python OAuth 2.0 Implementation including client and server packages
License: BSD
Group: Development/Python3
# in pypi:
# https://pypi.python.org/pypi/ndg-oauth-server/
# https://pypi.python.org/pypi/ndg-oauth-client/
Url: https://github.com/cedadev/ndg_oauth

# https://github.com/cedadev/ndg_oauth.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-ndg-httpsclient python3-module-PasteScript
BuildRequires: python3-module-beaker python3-module-webob
BuildRequires: python3-module-OpenSSL python3-module-pyasn1
BuildRequires: python3-module-repoze.who python3-module-genshi
BuildRequires: python3-module-nose python3-module-PasteDeploy

%py3_provides %oname
%py3_requires %mname

# for client:
%py3_requires ndg.httpsclient paste.script beaker webob OpenSSL json
%py3_requires logging

# for server:
%py3_requires repoze.who genshi json logging paste.deploy


%description
This is a core package of OAuth 2.0 server and client libraries.

These include WSGI wrappers for easy integration with Python frameworks
such as Pylons/Pyramid or Django.

%package -n python3-module-%oname.server
Summary: OAuth 2.0 server
Group: Development/Python3
%py3_provides %oname.server
Requires: %name = %EVR

%description -n python3-module-%oname.server
This is an OAuth 2.0 server library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added for a specialised use case to enable a SLCS (Short-lived
Credential Service) to issue delegated X.509-based credentials with
OAuth.

%package -n python3-module-%oname.server.examples
Summary: Examples for OAuth 2.0 server
Group: Development/Python3
%py3_provides %oname.server.examples
Requires: python3-module-%oname.server = %EVR

%description -n python3-module-%oname.server.examples
This is an OAuth 2.0 server library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added for a specialised use case to enable a SLCS (Short-lived
Credential Service) to issue delegated X.509-based credentials with
OAuth.

This package contains examples for %oname.server.

%package -n python3-module-%oname.client
Summary: OAuth 2.0 client
Group: Development/Python3
%py3_provides %oname.client
Requires: %name = %EVR

%description -n python3-module-%oname.client
This is an OAuth 2.0 client library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added to enable a SLCS (Short-lived Credential Service) to issue
delegated X.509-based credentials using OAuth.

%package -n python3-module-%oname.client.examples
Summary: Examples for OAuth 2.0 client
Group: Development/Python3
%py3_provides %oname.client.examples
Requires: python3-module-%oname.client = %EVR

%description -n python3-module-%oname.client.examples
This is an OAuth 2.0 client library and WSGI middleware filter.

It supports simple string-based bearer token and a custom extension to
enable the use of X.509 certificates as tokens. The latter has been
added to enable a SLCS (Short-lived Credential Service) to issue
delegated X.509-based credentials using OAuth.

This package contains examples for %oname.client.

%prep
%setup
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
for i in ndg_oauth_server ndg_oauth_client; do
	pushd $i
	%python3_build_debug
	popd
done

%install
for i in ndg_oauth_server ndg_oauth_client; do
	pushd $i
	%python3_install
	popd
done

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if 0
for i in ndg_oauth_server ndg_oauth_client; do
	pushd $i
	python3 setup.py test
	popd
done
%endif

%files
%doc README.md
%dir %python3_sitelibdir/ndg/oauth
%python3_sitelibdir/ndg/oauth/__init__.py*

%files -n python3-module-%oname.server
%python3_sitelibdir/ndg/oauth/server
%python3_sitelibdir/ndg_oauth_server*.egg-info
%exclude %python3_sitelibdir/ndg/oauth/server/examples
%exclude %python3_sitelibdir/ndg/oauth/server/*/*/test*

%files -n python3-module-%oname.server.examples
%python3_sitelibdir/ndg/oauth/server/examples
%python3_sitelibdir/ndg/oauth/server/*/*/test*

%files -n python3-module-%oname.client
%python3_sitelibdir/ndg/oauth/client
%python3_sitelibdir/ndg_oauth_client*.egg-info
%exclude %python3_sitelibdir/ndg/oauth/client/examples

%files -n python3-module-%oname.client.examples
%python3_sitelibdir/ndg/oauth/client/examples


%changelog
* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20131210.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20131210.1
- (AUTO) subst_x86_64.

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20131210
- Initial build for Sisyphus

