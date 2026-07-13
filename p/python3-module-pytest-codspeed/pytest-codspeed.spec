Name:    python3-module-pytest-codspeed
Version: 5.0.3
Release: alt1

Summary: Pytest plugin to create CodSpeed benchmarks
License: MIT
Group: Development/Python
URL: https://pypi.org/project/pytest-codspeed
VCS: https://github.com/CodSpeedHQ/pytest-codspeed

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/pytest_codspeed
%python3_sitelibdir/pytest_codspeed-%version.dist-info

%changelog
* Mon Jul 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 5.0.3-alt1
- 5.0.3 released

* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus.
