%define pypi_name dpapi-ng
%define mod_name dpapi_ng

%def_with check

Name:    python3-module-%pypi_name
Version: 0.2.0
Release: alt3

Summary: Python DPAPI NG Decryptor for non-Windows Platforms
License: MIT
Group:   Development/Python3
URL:     https://github.com/jborean93/dpapi-ng

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3(dnspython)
BuildRequires: python3(cryptography)
BuildRequires: python3(spnego)

%if_with check
# see requirements-test.txt
BuildRequires: python3(pytest-cov)
BuildRequires: python3-module-pytest-asyncio
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Library for DPAPI NG, also known as CNG DPAPI, de- and encryption in Python.
It is designed to replicate the behaviour of NCryptUnprotectSecret and
NCryptProtectSecret. This can be used on non-Windows hosts to de-/encrypt
DPAPI NG protected secrets, like PFX user protected password, or LAPS
encrypted password. It can either decrypt any DPAPI NG blobs using an offline
copy of the domain's root key or de-/encrypt by using the credentials of the
supplied user to retrieve the required information over RPC.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 11 2025 Stanislav Levin <slev@altlinux.org> 0.2.0-alt3
- NMU: fixed FTBFS (pytest 8.4.0).

* Mon Jun 09 2025 Michael Shigorin <mike@altlinux.org> 0.2.0-alt2
- Fix BR: regarding %%check

* Sun Jul 09 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
