Name: python3-module-aioresponses
Version: 0.7.8
Release: alt3

Summary: Helper to mock/fake web requests in python aiohttp package
License: MIT
Group: Development/Python
URL: https://pypi.org/project/aioresponses
VCS: https://github.com/pnuckowski/aioresponses

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter asynctest typing
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
export PBR_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt

%build
export PBR_VERSION=%version
%pyproject_build

%install
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
* Thu Jun 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.8-alt3
- revert unsolicited changes

* Wed Jun 10 2026 Stanislav Levin <slev@altlinux.org> 0.7.8-alt2
- NMU: fixed FTBFS (aiohttp 3.14.0).

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.7.8-alt1.1
- Demodernized packaging.

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.8-alt1
- 0.7.8 released
