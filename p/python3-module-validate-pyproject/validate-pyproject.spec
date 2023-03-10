%define _unpackaged_files_terminate_build 1
%define pypi_name validate-pyproject
%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 0.12.1
Release: alt1
Summary: Validation pyproject.toml files using JSON Schema
License: MPL-2.0 and MIT and BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/validate-pyproject
VCS: https://github.com/abravalheri/validate-pyproject.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

# PEP503 name
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
# deps
BuildRequires: python3(fastjsonschema)

# extra: all
BuildRequires: python3(trove-classifiers)
BuildRequires: python3(packaging)
%if %tomli
BuildRequires: python3(tomli)
%endif
# extra: testing
BuildRequires: python3(setuptools)
BuildRequires: python3(pytest)
%endif

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
%pyproject_run_pytest -vra

%files
%doc README.rst
%_bindir/validate-pyproject
%python3_sitelibdir/validate_pyproject/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Mar 10 2023 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1
- 0.12 -> 0.12.1.

* Thu Jan 26 2023 Stanislav Levin <slev@altlinux.org> 0.12-alt1
- 0.10.1 -> 0.12.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.9 -> 0.10.1.

* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 0.9-alt1
- 0.7.1 -> 0.9.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
