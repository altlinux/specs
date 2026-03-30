Name: python3-module-expandvars
Version: 1.1.2
Release: alt2

Summary: Expand system variables Unix style
License: MIT
Group: Development/Python
Url: https://pypi.org/project/expandvars
VCS: https://github.com/sayanarijit/expandvars

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra tests

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/expandvars.*
%python3_sitelibdir/*/expandvars.*
%python3_sitelibdir/expandvars-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1.1
- Demodernized packaging.

* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt1
- 1.1.2 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

