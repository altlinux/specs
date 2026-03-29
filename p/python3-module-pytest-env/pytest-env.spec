%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-env
%define mod_name pytest_env

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.0
Release: alt1.1
Summary: py.test plugin that allows you to add environment variables
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-env
Vcs: https://github.com/pytest-dev/pytest-env
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-python-dotenv
%endif

%description
This is a pytest plugin that enables you to set environment variables in a
pytest.ini or pyproject.toml file.

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
%pyproject_run_pytest -ra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1.1
- Demodernized packaging.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.5.0 -> 1.6.0.

* Mon Mar 02 2026 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.3.2 -> 1.5.0.

* Thu Feb 12 2026 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.2.0 -> 1.3.2.

* Wed Dec 03 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.5 -> 1.2.0.

* Thu Apr 03 2025 Stanislav Levin <slev@altlinux.org> 1.1.5-alt2
- fixed tests against pytest < 7.2.

* Wed Sep 18 2024 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- 1.1.4 -> 1.1.5.

* Tue Sep 10 2024 Stanislav Levin <slev@altlinux.org> 1.1.4-alt1
- 1.1.3 -> 1.1.4.

* Thu Feb 29 2024 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.1 -> 1.1.3.

* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 0.8.2 -> 1.1.1.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1
- 0.8.1 -> 0.8.2.

* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
