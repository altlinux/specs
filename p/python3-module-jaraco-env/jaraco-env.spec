%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.env
%define norm_name jaraco-env
%define ns_name jaraco
%define mod_name env

%def_with check

Name: python3-module-%norm_name
Version: 1.0.0
Release: alt1.2
Summary: Facilities for environment variables
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-env
Vcs: https://github.com/jaraco/jaraco.env
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-enabler
BuildRequires: python3-module-pytest-mypy
%endif

%description
This library facilitates handling of environment variables.

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
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name.py
%dir %python3_sitelibdir/%ns_name/__pycache__/
%python3_sitelibdir/%ns_name/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1.2
- Demodernized packaging.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
