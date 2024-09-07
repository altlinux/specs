%define _unpackaged_files_terminate_build 1

%define pypi_name msal
%def_disable check

Name: python3-module-%pypi_name
Version: 1.31.0
Release: alt1

Summary: Microsoft Authentication Library (MSAL) for Python
License: MIT
Group: Development/Python3
Url:  https://pypi.org/project/msal
Vcs: https://github.com/AzureAD/microsoft-authentication-library-for-python.git

Source: https://pypi.io/packages/source/m/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)

%description
The Microsoft Authentication Library for Python enables applications to
integrate with the Microsoft identity platform. It allows you to sign in
users or apps with Microsoft identities (Azure AD, Microsoft Accounts
and Azure AD B2C accounts) and obtain tokens to call Microsoft APIs such
as Microsoft Graph or your own APIs registered with the Microsoft
identity platform. It is built using industry standard OAuth2 and OpenID
Connect protocols.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 tests/

%files
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Sep 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.31.0-alt1
- 1.31.0

* Wed Jul 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.29.0-alt1
- 1.29.0

* Tue Jun 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1.28.1-alt1
- 1.28.1

* Tue Mar 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.28.0-alt1
- 1.28.0

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.27.0-alt1
- 1.27.0

* Thu Dec 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0

* Mon Nov 06 2023 Yuri N. Sedunov <aris@altlinux.org> 1.25.0-alt1
- first build for Sisyphus


