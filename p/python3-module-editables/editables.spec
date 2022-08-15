%define _unpackaged_files_terminate_build 1
%define pypi_name editables

%def_with check

Name: python3-module-%pypi_name
Version: 0.3
Release: alt1

Summary: Editable installations
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pfmoore/editables.git
Url: https://pypi.org/project/editables

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
A Python library for creating "editable wheels".
This library supports the building of wheels which, when installed, will expose
packages in a local directory on sys.path in "editable mode". In other words,
changes to the package source will be reflected in the package visible to
Python, without needing a reinstall.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream's tox configuration (requires too many fixes)
%tox_create_default_config
%tox_check_pyproject -- -vra tests

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.3-alt1
- 0.2 -> 0.3.

* Mon Apr 04 2022 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
