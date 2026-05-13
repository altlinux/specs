Name: python3-module-propcache
Version: 0.5.2
Release: alt1

Summary: Fast implementation of cached properties
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/propcache
VCS: https://github.com/aio-libs/propcache

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements/test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/propcache
%python3_sitelibdir/propcache-%version.dist-info

%changelog
* Wed May 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.2-alt1
- 0.5.2 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.1-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1.1
- Demodernized packaging.

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.1-alt1
- 0.4.1 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
