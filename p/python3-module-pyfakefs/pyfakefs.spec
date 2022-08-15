%define _unpackaged_files_terminate_build 1
%define pypi_name pyfakefs

%def_with check

Name: python3-module-%pypi_name
Version: 4.6.3
Release: alt1

Summary: Implements a fake file system that mocks the Python file system modules
License: Apache-2.0
Group: Development/Python3
# Source-git: https://github.com/jmcgeheeiv/pyfakefs.git
Url: https://pypi.org/project/pyfakefs/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
%pypi_name implements a fake file system that mocks the Python file system
modules. Using pyfakefs, your tests operate on a fake file system in memory
without touching the real disk. The software under test requires no
modification to work with pyfakefs.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
# don't package tests (useless)
rm -r %buildroot%python3_sitelibdir/%pypi_name/{tests,pytest_tests}

%check
%tox_check_pyproject

%files
%python3_sitelibdir/pyfakefs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 4.6.3-alt1
- 4.5.6 -> 4.6.3.

* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 4.5.6-alt1
- 4.5.5 -> 4.5.6.

* Thu Feb 24 2022 Stanislav Levin <slev@altlinux.org> 4.5.5-alt1
- 3.7.1 -> 4.5.5.

* Wed Feb 12 2020 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- Initial build.
