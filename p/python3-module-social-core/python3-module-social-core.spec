%define pypi_name social-core

%def_with check

Name:    python3-module-%pypi_name
Version: 4.8.7
Release: alt1

Summary: Python Social Auth - Core
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/python-social-auth/social-core

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-requests
BuildRequires: python3-module-requests-oauthlib
BuildRequires: python3-module-openid
BuildRequires: python3-module-oauthlib
BuildRequires: python3-module-jose
BuildRequires: python3-module-jwt
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-saml
BuildRequires: python3-module-xmlsec
BuildRequires: python3-module-google-auth-library-python
BuildRequires: python3-module-responses
BuildRequires: libxmlsec1-openssl-devel
%endif

# optional dependency
%add_python3_req_skip shopify

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Python Social Auth is an easy to setup social authentication/registration
mechanism with support for several frameworks and auth providers.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %version-%release

%description tests
This package contains tests for %name.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_steam.py"

%files
%doc *.md
%python3_sitelibdir/social_core/py.typed
%python3_sitelibdir/social_core/*.py
%python3_sitelibdir/social_core/__pycache__/
%python3_sitelibdir/social_core/backends/
%python3_sitelibdir/social_core/pipeline/
%python3_sitelibdir/%{pyproject_distinfo social_auth_core}

%files tests
%python3_sitelibdir/social_core/tests/

%changelog
* Tue Apr 28 2026 Alexander Burmatov <thatman@altlinux.org> 4.8.7-alt1
- Update to version 4.8.7.

* Wed Feb 18 2026 Alexander Burmatov <thatman@altlinux.org> 4.8.5-alt1
- Update to version 4.8.5.

* Wed Dec 24 2025 Alexander Burmatov <thatman@altlinux.org> 4.8.3-alt1
- Update to version 4.8.3.

* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 4.8.1-alt1
- Update to version 4.8.1.

* Mon Jul 28 2025 Alexander Burmatov <thatman@altlinux.org> 4.7.0-alt1
- Update to version 4.7.0.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 4.6.1-alt1
- Update to version 4.6.1.

* Fri Mar 14 2025 Alexander Burmatov <thatman@altlinux.org> 4.5.6-alt1
- Update to version 4.5.6.

* Tue Dec 12 2023 Alexander Burmatov <thatman@altlinux.org> 4.5.1-alt1
- Update to version 4.5.1.

* Tue Oct 03 2023 Alexander Burmatov <thatman@altlinux.org> 4.4.2-alt1
- Initial build for Sisyphus.
