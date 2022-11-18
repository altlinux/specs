%define _unpackaged_files_terminate_build 1
%global pypi_name pytest-testmon

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1
Summary: A py.test plug-in which executes only tests affected by recent changes
Group: Development/Python
License: AGPL-3.0
Url: http://testmon.org/
VCS: https://github.com/tarpas/pytest-testmon.git

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%py3_provides pytest_testmon
%py3_provides %pypi_name

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%prep
%setup
%patch0 -p1

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

