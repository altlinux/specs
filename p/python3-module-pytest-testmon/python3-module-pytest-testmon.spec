%define _unpackaged_files_terminate_build 1
%global pypi_name pytest-testmon

Name: python3-module-%pypi_name
Version: 2.0.9
Release: alt1
Summary: A py.test plug-in which executes only tests affected by recent changes
License: AGPL-3.0
Group: Development/Python
Url: https://pypi.org/project/pytest-testmon/
VCS: https://github.com/tarpas/pytest-testmon.git
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-%release.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# upstream no longer provides the test suite

%files
%doc README.md
%python3_sitelibdir/testmon/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jun 15 2023 Stanislav Levin <slev@altlinux.org> 2.0.9-alt1
- 2.0.8 -> 2.0.9.

* Thu May 18 2023 Stanislav Levin <slev@altlinux.org> 2.0.8-alt1
- 1.4.2 -> 2.0.8.

* Fri Nov 18 2022 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.4.0 -> 1.4.2.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.7 -> 1.4.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 1.3.7-alt1
- 1.3.6 -> 1.3.7.

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 1.3.6-alt1
- 1.3.4 -> 1.3.6.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 1.3.4-alt1
- 1.2.2 -> 1.3.4.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 1.2.2-alt2
- Fixed FTBFS (Python3.10).

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.0.3 -> 1.2.2

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1
- 0.9.18 -> 1.0.3.

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 0.9.18-alt1
- first build for ALT

