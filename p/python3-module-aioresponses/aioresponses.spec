%def_with check

Name: python3-module-aioresponses
Version: 0.7.8
Release: alt2

Summary: Helper to mock/fake web requests in python aiohttp package
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aioresponses/
VCS: https://github.com/pnuckowski/aioresponses

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr

%if check
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-ddt
%endif

%description
%summary

%prep
%setup

%build
export PBR_VERSION=%version
%pyproject_build

%install
export PBR_VERSION=%version
%pyproject_install

%check
# some are online
%pyproject_run_pytest -o=addopts= tests -k \
    "not test_address_as_instance_of_url_combined_with_pass_through and \
    not test_pass_through_with_origin_params and \
    not test_pass_through_unmatched_requests"

%files
%python3_sitelibdir/aioresponses
%python3_sitelibdir/aioresponses-%version.dist-info

%changelog
* Wed Jun 10 2026 Stanislav Levin <slev@altlinux.org> 0.7.8-alt2
- NMU: fixed FTBFS (aiohttp 3.14.0).

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.7.8-alt1.1
- Demodernized packaging.

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.8-alt1
- 0.7.8 released
