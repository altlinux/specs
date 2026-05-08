Name: python3-module-mashumaro
Version: 3.21
Release: alt1

Summary: Fast and well tested serialization library
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/mashumaro
VCS: https://github.com/Fatal1ty/mashumaro

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_check_filter codespell dataclasses-json pytablewriter termtables
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/mashumaro
%python3_sitelibdir/mashumaro-%version.dist-info

%changelog
* Fri May 08 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.21-alt1
- 3.21 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.20-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.20-alt1.1
- Demodernized packaging.

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.20-alt1
- 3.20 released

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.17-alt1
- 3.17 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.15-alt1
- 3.15 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.14-alt1
- 3.14 released
