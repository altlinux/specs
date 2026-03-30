%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-mock
%define mod_name pytest_mock

%def_with check

Name: python3-module-%pypi_name
Version: 3.15.1
Release: alt1.1
Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-mock/
Vcs: https://github.com/pytest-dev/pytest-mock/
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%py3_provides %pypi_name

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-asyncio

BuildRequires: python3-module-pytest
%endif

%description
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%prep
%setup
%patch -p1
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
%pyproject_run_pytest -ra -Wignore tests

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.15.1-alt1.1
- Demodernized packaging.

* Wed Dec 03 2025 Stanislav Levin <slev@altlinux.org> 3.15.1-alt1
- 3.15.0 -> 3.15.1.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 3.15.0-alt1
- 3.14.1 -> 3.15.0.

* Tue May 27 2025 Stanislav Levin <slev@altlinux.org> 3.14.1-alt1
- 3.14.0 -> 3.14.1.

* Fri Mar 22 2024 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.12.0 -> 3.14.0.

* Mon Jan 29 2024 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1
- 3.11.1 -> 3.12.0.

* Fri Jun 16 2023 Stanislav Levin <slev@altlinux.org> 3.11.1-alt1
- 3.10.0 -> 3.11.1.

* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.0 -> 3.10.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.8.2 -> 3.9.0.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.7.0 -> 3.8.2.

* Fri Mar 18 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt2
- Fixed FTBFS (Pytest 7.1.1).

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.5.1 -> 3.7.0.

* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.3.1 -> 3.5.1.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 1.10.4 -> 3.3.1.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt2
- Added missing dep on Pytest.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt1
- 1.10.1 -> 1.10.4.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Thu Apr 12 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.6.2 -> 1.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt1
- Updated to upstream version 1.6.2.

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
