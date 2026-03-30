%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.classes
%define ns_name jaraco
%define mod_name classes

%def_with check

Name: python3-module-%pypi_name
Version: 3.4.0
Release: alt1.2
Summary: Utility functions for Python class constructs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.classes/
Vcs: https://github.com/jaraco/jaraco.classes
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-enabler
BuildRequires: python3-module-pytest-mypy
%endif

%description
%summary

%prep
%setup
%patch0 -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1.2
- Demodernized packaging.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Mon Apr 01 2024 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.3.0 -> 3.3.1.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.2.2 -> 3.3.0.

* Mon Sep 12 2022 Danil Shein <dshein@altlinux.org> 3.2.2-alt1
- update version to 3.2.2
  + migrate to pyproject macroses

* Wed Nov 18 2020 Danil Shein <dshein@altlinux.org> 3.1.0-alt1
- update version to 3.1.0
- build with check enabled

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- first build for ALT

