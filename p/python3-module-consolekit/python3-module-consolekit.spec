%define _unpackaged_files_terminate_build 1
%define pypi_name consolekit
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.13.0
Release: alt2

Summary: Additional utilities for click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/consolekit/
Vcs: https://github.com/domdfcoding/consolekit

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter backports-entry-points-selectable
%add_pyproject_deps_check_filter pytest-mypy-plugins
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 27 2026 Stanislav Levin <slev@altlinux.org> 1.13.0-alt2
- Fixed FTBFS (click 8.4.0).

* Fri Feb 20 2026 Stanislav Levin <slev@altlinux.org> 1.13.0-alt1
- 1.9.0 -> 1.13.0.

* Fri Jun 06 2025 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.1 -> 1.9.0.

* Thu May 22 2025 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1
- 1.7.2 -> 1.8.1.

* Tue Oct 22 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.2-alt1
- Updated to 1.7.2.

* Tue Aug 06 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.1-alt1
- Updated to 1.7.1.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.0-alt1
- Updated to 1.7.0.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Thu Nov 23 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.2-alt1
- Updated to 1.5.2.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.1-alt1
- Updated to 1.5.1.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt2
- enable tests
- fix requires

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- initial build for Sisyphus (temporary broken)

