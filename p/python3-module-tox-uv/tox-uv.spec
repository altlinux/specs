%define _unpackaged_files_terminate_build 1
%define pypi_name tox-uv
%define mod_name tox_uv_meta

%def_with check

Name: python3-module-%pypi_name
Version: 1.33.4
Release: alt1.1
Summary: Integration of uv with tox (meta package)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-uv
Vcs: https://github.com/tox-dev/tox-uv
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

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

BuildRequires: python3-module-tox-uv-bare
BuildRequires: python3-module-uv
%endif

%description
tox-uv is a tox plugin, which replaces virtualenv and pip with uv in your tox
environments. Note that you will get both the benefits (performance) or
downsides (bugs) of uv.

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
pushd meta
popd

%build
pushd meta
%pyproject_build
popd

%install
pushd meta
%pyproject_install
popd

%check
pushd meta
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
pushd ..
export UV_OFFLINE=1
export UV_NO_BUILD_ISOLATION=1
python -m pytest -vra meta/tests/
popd
ENDTESTS
popd

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.33.4-alt1.1
- Demodernized packaging.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 1.33.4-alt1
- 1.33.2 -> 1.33.4.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 1.33.2-alt1
- 1.29.0 -> 1.33.2.

* Thu Dec 11 2025 Stanislav Levin <slev@altlinux.org> 1.29.0-alt1
- 1.28.0 -> 1.29.0.

* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 1.28.0-alt1
- Initial build for Sisyphus.
