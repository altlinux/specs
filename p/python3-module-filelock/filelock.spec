%define _unpackaged_files_terminate_build 1
%define pypi_name filelock
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.25.2
Release: alt1.1
Summary: A platform independent file lock for Python
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/filelock/
VCS: https://github.com/tox-dev/py-filelock
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-virtualenv
%endif

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%setup
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
%pyproject_run_pytest -vra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.25.2-alt1.1
- Demodernized packaging.

* Thu Mar 12 2026 Stanislav Levin <slev@altlinux.org> 3.25.2-alt1
- 3.25.1 -> 3.25.2.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 3.25.1-alt1
- 3.25.0 -> 3.25.1.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 3.25.0-alt1
- 3.24.3 -> 3.25.0.

* Thu Feb 19 2026 Stanislav Levin <slev@altlinux.org> 3.24.3-alt1
- 3.24.2 -> 3.24.3.

* Mon Feb 16 2026 Stanislav Levin <slev@altlinux.org> 3.24.2-alt1
- 3.21.2 -> 3.24.2.

* Fri Feb 13 2026 Stanislav Levin <slev@altlinux.org> 3.21.2-alt1
- 3.20.3 -> 3.21.2.

* Wed Jan 14 2026 Stanislav Levin <slev@altlinux.org> 3.20.3-alt1
- 3.20.1 -> 3.20.3 (fixes: CVE-2026-22701).

* Tue Dec 16 2025 Stanislav Levin <slev@altlinux.org> 3.20.1-alt1
- 3.20.0 -> 3.20.1 (fixes: CVE-2025-68146).

* Wed Oct 29 2025 Stanislav Levin <slev@altlinux.org> 3.20.0-alt1
- 3.19.1 -> 3.20.0.

* Tue Sep 02 2025 Stanislav Levin <slev@altlinux.org> 3.19.1-alt1
- 3.18.0 -> 3.19.1.

* Fri Mar 14 2025 Stanislav Levin <slev@altlinux.org> 3.18.0-alt1
- 3.17.0 -> 3.18.0.

* Wed Jan 22 2025 Stanislav Levin <slev@altlinux.org> 3.17.0-alt1
- 3.16.1 -> 3.17.0.

* Wed Sep 18 2024 Stanislav Levin <slev@altlinux.org> 3.16.1-alt1
- 3.16.0 -> 3.16.1.

* Tue Sep 10 2024 Stanislav Levin <slev@altlinux.org> 3.16.0-alt1
- 3.15.4 -> 3.16.0.

* Mon Jun 24 2024 Stanislav Levin <slev@altlinux.org> 3.15.4-alt1
- 3.15.3 -> 3.15.4.

* Thu Jun 20 2024 Stanislav Levin <slev@altlinux.org> 3.15.3-alt1
- 3.14.0 -> 3.15.3.

* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.13.4 -> 3.14.0.

* Wed Apr 10 2024 Stanislav Levin <slev@altlinux.org> 3.13.4-alt1
- 3.13.3 -> 3.13.4.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 3.13.3-alt1
- 3.13.1 -> 3.13.3.

* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 3.13.1-alt1
- 3.12.2 -> 3.13.1.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 3.12.2-alt1
- 3.12.0 -> 3.12.2.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1
- 3.9.0 -> 3.12.0.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.8.2 -> 3.9.0.

* Tue Dec 06 2022 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.8.1 -> 3.8.2.

* Mon Dec 05 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1
- 3.8.0 -> 3.8.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 3.8.0-alt1
- 3.6.0 -> 3.8.0.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.4.2 -> 3.6.0.

* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
- 3.3.2 -> 3.4.2.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 3.3.2-alt1
- 3.3.1 -> 3.3.2.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.0.10 -> 3.3.1.

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.10-alt2
- Drop python2 support.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.0.10-alt1
- 3.0.9 -> 3.0.10.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 3.0.9-alt1
- Initial build.

