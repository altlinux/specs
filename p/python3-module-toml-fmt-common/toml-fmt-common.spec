%define _unpackaged_files_terminate_build 1
%define pypi_name toml-fmt-common
%define mod_name toml_fmt_common

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1.1
Summary: Common logic to the TOML formatter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/toml-fmt-common
Vcs: https://github.com/tox-dev/toml-fmt-common
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
%endif

%description
Contains Python code common to all formatters under the toml-fmt umbrella (meant
to only be used by that project).

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
%pyproject_run_pytest -vra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1.1
- Demodernized packaging.

* Tue Mar 03 2026 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- 1.2.0 -> 1.3.1.

* Tue Feb 03 2026 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Thu Dec 11 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0.

* Tue Nov 05 2024 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
