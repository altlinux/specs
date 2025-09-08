%define pypi_name libcng-dpapi
%define mod_name libcng-dpapi

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.1
Release: alt1

Summary: Wrapper around DPAPI-CNG Library
License: GPLv2
Group:   Development/Python3
URL:     https://github.com/august-alt/libcng-dpapi

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: python3(dnspython)
BuildRequires: python3(spnego)

%if_with check
BuildRequires: python3(pytest-cov)
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
An alternative Python library for DPAPI NG (CNG DPAPI) encryption and decription, replicating the behavior of Windows' NCryptUnprotectSecret and NCryptProtectSecret. This solution enables cross-platform decryption of DPAPI NG-protected secrets on non-Windows systems, including PFX user-protected passwords and LAPS encrypted credentials.

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
* Mon Sep 08 2025 Vladimir Rubanov <august@altlinux.org> 0.0.1-alt1
- Initial build

