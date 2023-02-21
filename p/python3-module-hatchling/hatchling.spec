%define _unpackaged_files_terminate_build 1
%define pypi_name hatchling

%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

Name: python3-module-%pypi_name
Version: 1.13.0
Release: alt1
Summary: Modern, extensible Python build backend
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatchling
VCS: https://github.com/pypa/hatch
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# try-except import
%py3_requires editables
%if %tomli
# rebuild against Python 3.11 is required to get rid of old dependency
%py3_requires tomli
%endif

BuildRequires(pre): rpm-build-python3

# self-bootstraps deps
# see backend/src/hatchling/ouroboros.py
BuildRequires: python3(editables)
BuildRequires: python3(packaging)
BuildRequires: python3(pathspec)
BuildRequires: python3(pluggy)
%if %tomli
BuildRequires: python3(tomli)
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# Requires Internet, see tests/downstream/integrate.py

%files
%doc README.md
%_bindir/hatchling
%python3_sitelibdir/hatchling/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 20 2023 Stanislav Levin <slev@altlinux.org> 1.13.0-alt1
- 1.12.2 -> 1.13.0.

* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 1.12.2-alt1
- 1.11.1 -> 1.12.2.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 1.11.1-alt1
- 1.11.0 -> 1.11.1.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1
- 1.10.0 -> 1.11.0.

* Mon Sep 19 2022 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Mon Sep 12 2022 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.1 -> 1.9.0.

* Thu Aug 25 2022 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1
- 1.8.0 -> 1.8.1.

* Tue Aug 16 2022 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.7.1 -> 1.8.0.

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 1.7.1-alt1
- 0.22.0 -> 1.7.1.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.22.0-alt1
- Initial build for Sisyphus.
