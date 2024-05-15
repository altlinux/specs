%define _unpackaged_files_terminate_build 1
%define pypi_name platformdirs

%def_with check

Name: python3-module-%pypi_name
Version: 4.2.2
Release: alt1
Summary: Determining appropriate platform-specific dirs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/platformdirs
VCS: https://github.com/platformdirs/platformdirs.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
A small Python module for determining appropriate platform-specific dirs, e.g.
a "user data dir". When writing desktop application, finding the right location
to store user data and configuration varies per platform. Even for
single-platform apps, there may by plenty of nuances in figuring out the right
location.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests -Wignore

%files
%doc README.rst
%python3_sitelibdir/platformdirs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 4.2.2-alt1
- 4.2.1 -> 4.2.2.

* Wed Apr 24 2024 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1
- 3.10.0 -> 4.2.1.

* Mon Jul 31 2023 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.1 -> 3.10.0.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 3.9.1-alt1
- 3.7.0 -> 3.9.1.

* Wed Jun 21 2023 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.5.3 -> 3.7.0.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1
- 3.5.1 -> 3.5.3.

* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.2.0 -> 3.5.1.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.0.0 -> 3.2.0.

* Tue Feb 14 2023 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.6.2 -> 3.0.0.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 2.6.2-alt1
- 2.6.0 -> 2.6.2.

* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.5.4 -> 2.6.0.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 2.5.4-alt1
- 2.5.2 -> 2.5.4.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 2.5.2-alt1
- 2.5.1 -> 2.5.2.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 2.5.1-alt1
- 2.5.0 -> 2.5.1.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.4.1 -> 2.5.0.

* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.1.0 -> 2.3.0.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.
