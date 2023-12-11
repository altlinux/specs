%define pypi_name napalm-huawei-vrp
%define mod_name napalm_huawei_vrp

# Tests require network
%def_without check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: NAPALM Driver for Huawei VRP5/VRP8 Routers and Switches
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/napalm-automation-community/napalm-huawei-vrp

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pylama
BuildRequires: python3-module-napalm
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch1: 0001-Fix-broken-tests.patch

%description
It's a NAPALM Community Driver for Huawei VRP5/VRP8 Enterprise/Service Provider
Routers and Switches.

%prep
%setup -n %pypi_name-%version
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-1.0.0.dist-info/

%changelog
* Fri Dec 08 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
