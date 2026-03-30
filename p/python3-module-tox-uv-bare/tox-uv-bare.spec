%define _unpackaged_files_terminate_build 1
%define pypi_name tox-uv-bare
%define mod_name tox_uv

%def_with check

Name: python3-module-%pypi_name
Version: 1.33.4
Release: alt1.1
Summary: Integration of uv with tox (bare package, bring your own uv)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-uv-bare
Vcs: https://github.com/tox-dev/tox-uv
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# tox_uv directory was previously packaged in tox-uv
Conflicts: python3-module-tox-uv <= 1.29.0-alt1

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-devpi-process
BuildRequires: python3-module-diff-cover
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock

BuildRequires: python3-module-packaging
BuildRequires: python3-module-tox
# install system uv
BuildRequires: uv
%endif

%description
%summary.

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
export UV_OFFLINE=1
%pyproject_run_pytest -vra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.33.4-alt1.1
- Demodernized packaging.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 1.33.4-alt1
- 1.33.2 -> 1.33.4.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 1.33.2-alt1
- Initial build for sisyphus.
