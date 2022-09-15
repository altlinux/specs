%define _unpackaged_files_terminate_build 1
%define pypi_name validate-pyproject

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.1
Release: alt1

Summary: Validation pyproject.toml files using JSON Schema
License: MPL-2.0 and MIT and BSD-3-Clause
Group: Development/Python3
# Source-git: https://github.com/abravalheri/validate-pyproject.git
Url: https://pypi.org/project/validate-pyproject

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(trove-classifiers)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

# hide vendored packages
%add_findprov_skiplist %python3_sitelibdir/validate_pyproject/_vendor/*

%description
Validation library and CLI tool for checking on 'pyproject.toml' files using
JSON Schema.

%prep
%setup
%autopatch -p1

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%_bindir/validate-pyproject
%python3_sitelibdir/validate_pyproject/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.9 -> 0.10.1.

* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.7.1 -> 0.9.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
