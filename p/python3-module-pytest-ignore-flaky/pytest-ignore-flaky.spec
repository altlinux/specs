%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-ignore-flaky
%define mod_name pytest_ignore_flaky

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1.1
Summary: Ignore failures from flaky tests
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-ignore-flaky
Vcs: https://github.com/schettino72/pytest-ignore-flaky
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Ignore failures from flaky tests (pytest plugin).

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1.1
- Demodernized packaging.

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.2.0 -> 2.2.1.

* Mon Apr 08 2024 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.0.0 -> 2.2.0.

* Fri Jul 21 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
