%define oname tyoiOAuth2

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20110417.1
Summary: Implements the "client" side of OAuth 2.0
License: MIT
Group: Development/Python
Url: https://github.com/ryanhorn/tyoiOAuth2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ryanhorn/tyoiOAuth2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

Requires: python-module-tyoi = %EVR

%description
This module provides a set of components, which together serve as an
OAuth2 "Client" capable of issuing access token requests to an OAuth2
"Authorization Server" on behalf of a "Resource Owner" (see
http://tools.ietf.org/html/draft-ietf-oauth-v2-12#section-1.1 for the
various role definitions). It is designed for flexibility and
extensibility by decoupling the different parts of an access token
request.

%package -n python-module-tyoi
Summary: Core files of tyoi
Group: Development/Python

%description -n python-module-tyoi
Core files of tyoi.

%package -n python3-module-%oname
Summary: Implements the "client" side of OAuth 2.0
Group: Development/Python3
Requires: python3-module-tyoi = %EVR

%description -n python3-module-%oname
This module provides a set of components, which together serve as an
OAuth2 "Client" capable of issuing access token requests to an OAuth2
"Authorization Server" on behalf of a "Resource Owner" (see
http://tools.ietf.org/html/draft-ietf-oauth-v2-12#section-1.1 for the
various role definitions). It is designed for flexibility and
extensibility by decoupling the different parts of an access token
request.

%package -n python3-module-tyoi
Summary: Core files of tyoi
Group: Development/Python3

%description -n python3-module-tyoi
Core files of tyoi.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.md
%python_sitelibdir/tyoi/oauth2
%python_sitelibdir/*.egg-info

%files -n python-module-tyoi
%python_sitelibdir/tyoi
%exclude %python_sitelibdir/tyoi/oauth2

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/tyoi/oauth2
%python3_sitelibdir/*.egg-info

%files -n python3-module-tyoi
%python3_sitelibdir/tyoi
%exclude %python3_sitelibdir/tyoi/oauth2
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20110417.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20110417
- Initial build for Sisyphus

