%define _unpackaged_files_terminate_build 1
%define pypi_name tempora

%def_with check

Name: python3-module-%pypi_name
Version: 5.8.1
Release: alt1.1
Summary: Objects and routines pertaining to date and time (tempora)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tempora/
VCS: https://github.com/jaraco/tempora
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-jaraco-functools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-freezer
BuildRequires: python3-module-python-dateutil
%endif

%description
Objects and routines pertaining to date and time (tempora).

%prep
%setup
%autopatch -p1
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
%pyproject_run_pytest -ra

%files
%_bindir/calc-prorate
%python3_sitelibdir/tempora/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.8.1-alt1.1
- Demodernized packaging.

* Mon Jun 23 2025 Stanislav Levin <slev@altlinux.org> 5.8.1-alt1
- 5.8.0 -> 5.8.1.

* Thu Jan 09 2025 Stanislav Levin <slev@altlinux.org> 5.8.0-alt1
- 5.7.0 -> 5.8.0.

* Fri Jul 26 2024 Stanislav Levin <slev@altlinux.org> 5.7.0-alt1
- 5.6.0 -> 5.7.0.

* Wed Jun 19 2024 Stanislav Levin <slev@altlinux.org> 5.6.0-alt1
- 5.5.1 -> 5.6.0.

* Tue Feb 20 2024 Stanislav Levin <slev@altlinux.org> 5.5.1-alt1
- 5.5.0 -> 5.5.1.

* Thu Jul 27 2023 Stanislav Levin <slev@altlinux.org> 5.5.0-alt1
- 5.3.0 -> 5.5.0.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 5.2.1 -> 5.3.0.

* Wed Mar 01 2023 Stanislav Levin <slev@altlinux.org> 5.2.1-alt1
- 5.0.2 -> 5.2.1.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 5.0.2-alt1
- 4.1.1 -> 5.0.2.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1
- 1.12 -> 4.1.1.
- Enabled testing.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.12-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
