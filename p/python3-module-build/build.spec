%define _unpackaged_files_terminate_build 1
%define pypi_name build
%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.0
Release: alt1
Summary: Simple, correct PEP 517 build frontend
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/build
VCS: https://github.com/pypa/build.git
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

%if %tomli
# rebuild against Python 3.11 is required to get rid of old dependency
%py3_requires tomli
%endif
%py3_requires packaging

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit-core)

%if_with check
# install_requires:
BuildRequires: python3(packaging)
BuildRequires: python3(pyproject_hooks)
%if %tomli
BuildRequires: python3(tomli)
%endif

# synced to .[test]
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_rerunfailures)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(filelock)
BuildRequires: python3(toml)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools)
%endif

%description
A simple, correct PEP 517 build frontend.

build will invoke the PEP 517 hooks to build a distribution package. It is a
simple build tool and does not perform any dependency management.

%package -n pyproject-build
Summary: Executable for python-build
Group: Development/Python3
# not autodetected dep
Requires: python3-module-%pypi_name

%description -n pyproject-build
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%python3_sitelibdir/build/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n pyproject-build
%_bindir/pyproject-build

%changelog
* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.0 -> 0.10.0.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.0 -> 0.9.0.

* Mon Sep 26 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt2
- Fixed FTBFS (missing tests dependency on toml).

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.0 -> 0.8.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
