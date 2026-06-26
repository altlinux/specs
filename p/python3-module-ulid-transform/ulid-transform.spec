Name: python3-module-ulid-transform
Version: 2.2.9
Release: alt1

Summary: Fast ULID transformations
License: MIT
Group: Development/Python
URL: https://pypi.org/project/ulid-transform
VCS: https://github.com/bluetooth-devices/ulid-transform

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
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
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/ulid_transform
%python3_sitelibdir/ulid_transform-%version.dist-info

%changelog
* Fri Jun 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.9-alt1
- 2.2.9 released

* Mon May 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.1-alt1
- 2.2.1 released

* Mon Apr 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.0-alt1
- 2.2.0 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.2-alt1
- 1.5.2 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.2-alt1
- 0.7.2 released
