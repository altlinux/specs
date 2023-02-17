%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-metadata
%define mod_name pyproject_metadata

%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1
Summary: PEP 621 metadata parsing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-metadata
VCS: https://github.com/FFY00/python-pyproject-metadata.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# PyPI wellknown name
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# dependencies
BuildRequires: python3(packaging)

BuildRequires: python3(pytest)
%if %tomli
BuildRequires: python3(tomli)
%endif
%endif

%description
This project does not implement the parsing of pyproject.toml containing PEP 621
metadata.

Instead, given a Python data structure representing PEP 621 metadata (already
parsed), it will validate this input and generate a PEP 643-compliant metadata
file (e.g. PKG-INFO).

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests/

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
