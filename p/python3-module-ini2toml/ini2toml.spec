%define _unpackaged_files_terminate_build 1
%define pypi_name ini2toml

%def_with check

Name: python3-module-%pypi_name
Version: 0.16
Release: alt1.1
Summary: Automatically conversion of .ini/.cfg files to TOML equivalents
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/ini2toml
VCS: https://github.com/abravalheri/ini2toml.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-configupdater
BuildRequires: python3-module-packaging
BuildRequires: python3-module-tomli-w
BuildRequires: python3-module-tomlkit
BuildRequires: python3-module-isort
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-randomly
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-tomli
BuildRequires: python3-module-validate-pyproject
%endif

%add_python3_req_skip distutils

%description
The original purpose of this project is to help migrating setup.cfg files to
PEP621, but by extension it can also be used to convert any compatible .ini/.cfg
file to TOML.

%package lite
Summary: %summary
Group: Development/Python3
Requires: %name
Provides: %name+lite = %EVR

%description lite
Extra 'lite' for %pypi_name.

%package full
Summary: %summary
Group: Development/Python3
Requires: %name
Provides: %name+full = %EVR

%description full
Extra 'full' for %pypi_name.

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
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc README.rst
%_bindir/%pypi_name
%python3_sitelibdir/ini2toml/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files lite
%files full
%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.16-alt1.1
- Demodernized packaging.

* Thu Jul 04 2024 Stanislav Levin <slev@altlinux.org> 0.16-alt1
- 0.15 -> 0.16.

* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 0.15-alt1
- 0.14 -> 0.15.

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 0.14-alt1
- 0.13 -> 0.14.

* Fri Oct 27 2023 Stanislav Levin <slev@altlinux.org> 0.13-alt1
- 0.12 -> 0.13.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 0.12-alt1
- 0.11.3 -> 0.12.

* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 0.11.3-alt1
- 0.11.1 -> 0.11.3.

* Tue Nov 15 2022 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1
- 0.11 -> 0.11.1.

* Fri Aug 12 2022 Stanislav Levin <slev@altlinux.org> 0.11-alt1
- 0.10 -> 0.11.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.10-alt1
- Initial build for Sisyphus.
