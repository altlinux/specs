%define _unpackaged_files_terminate_build 1
%global pypi_name pytest-testmon

Name: python3-module-%pypi_name
Version: 1.2.2
Release: alt2
Summary: A py.test plug-in which executes only tests affected by recent changes
Group: Development/Python
License: MIT
Url: http://testmon.org/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides pytest_testmon

%description
This is a py.test plug-in which automatically selects and re-
executes only tests affected by recent changes.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install

%check
# upstream no longer provides the test suite

%files
%doc README.rst LICENSE
%python3_sitelibdir/testmon/
%python3_sitelibdir/pytest_testmon-%version-py%_python3_version.egg-info/

%changelog
* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 1.2.2-alt2
- Fixed FTBFS (Python3.10).

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.0.3 -> 1.2.2

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1
- 0.9.18 -> 1.0.3.

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 0.9.18-alt1
- first build for ALT

