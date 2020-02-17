%define oname tyoiOAuth2

Name: python3-module-%oname
Version: 0.2.1
Release: alt2

Summary: Implements the "client" side of OAuth 2.0
License: MIT
Group: Development/Python3
Url: https://github.com/ryanhorn/tyoiOAuth2
BuildArch: noarch

# https://github.com/ryanhorn/tyoiOAuth2.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
Requires: python3-module-tyoi = %EVR


%description
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

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/tyoi/oauth2
%python3_sitelibdir/*.egg-info

%files -n python3-module-tyoi
%python3_sitelibdir/tyoi
%exclude %python3_sitelibdir/tyoi/oauth2


%changelog
* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt1.git20110417.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20110417.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20110417
- Initial build for Sisyphus

