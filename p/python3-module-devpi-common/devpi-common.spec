%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-common
%define mod_name devpi_common

%def_with check

Name: python3-module-%pypi_name
Version: 4.1.1
Release: alt1.1
Summary: This package contains utility functions used by devpi-server and devpi-client
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-common
Vcs: https://github.com/devpi/devpi
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest

BuildRequires: python3-module-lazy
BuildRequires: python3-module-packaging-legacy
BuildRequires: python3-module-requests
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt1.1
- Demodernized packaging.

* Tue Feb 10 2026 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 4.1.0 -> 4.1.1.

* Mon May 19 2025 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1
- 4.0.4 -> 4.1.0.

* Thu May 30 2024 Stanislav Levin <slev@altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus.
