Name: python3-module-asyncstdlib
Version: 3.14.0
Release: alt1

Summary: Async-compatible stdlib reimplementation
License: MIT
Group: Development/Python
URL: https://pypi.org/project/asyncstdlib
VCS: https://github.com/maxfischer2781/asyncstdlib

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra tests
%pyproject_builddeps_metadata_extra typetest

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
%pyproject_run_pytest unittests

%files
%python3_sitelibdir/asyncstdlib
%python3_sitelibdir/asyncstdlib-%version.dist-info

%changelog
* Wed Apr 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.14.0-alt1
- 3.14.0 released

* Mon Oct 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.13.1-alt1
- 3.13.1 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.12.5-alt1
- 3.12.5 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.12.0-alt1
- 3.12.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.8-alt1
- 3.10.8 released

* Thu Sep 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.10.5-alt1
- 3.10.5 released
