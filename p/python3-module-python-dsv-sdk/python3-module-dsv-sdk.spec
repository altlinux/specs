%define pypi_name python-dsv-sdk

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.4
Release: alt2

Summary: The Delinea DevOps Secret Vault Python SDK
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/python-dsv-sdk
VCS: https://github.com/DelineaXPM/python-dsv-sdk

BuildArch: noarch

Source: %pypi_name-%version.tar
# https://github.com/DelineaXPM/python-dsv-sdk/pull/42
Patch0: python-dsv-sdk-1.0.4-support-flit-core-4-by-migrating-metadata.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-python-dotenv
BuildRequires: python3-module-requests
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# Tests need network access
export DSV_CLIENT_ID=""
export DSV_CLIENT_SECRET=""
export DSV_BASE_URL="http://localhost"
%pyproject_run_pytest -v -k "\
not test_get_secret \
and not test_access_token_authorizer \
and not test_get_nonexistent_secret \
and not test_get_secret_path_has_no_leading_slash"

%files
%doc README.*
%python3_sitelibdir/delinea
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 25 2026 Stanislav Levin <slev@altlinux.org> 1.0.4-alt2
- NMU: fixed FTBFS (flit-core 4).

* Wed Jul 24 2024 Anton Vyatkin <toni@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
