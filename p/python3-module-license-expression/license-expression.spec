%define _unpackaged_files_terminate_build 1
%define pypi_name license-expression

%def_with check

Name: python3-module-%pypi_name
Version: 30.0.0
Release: alt1

Summary: Comprehensive utility library to parse, compare, simplify and normalize license expressions
License: Apache-2.0
Group: Development/Python3
VCS: https://github.com/nexB/license-expression.git
Url: https://pypi.org/project/license-expression

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools-scm)

%if_with check
# deps
BuildRequires: python3(boolean.py)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%py3_provides %pypi_name

%description
license-expression is a comprehensive utility library to parse, compare,
simplify and normalize license expressions (such as SPDX license expressions)
using boolean logic.

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/license_expression/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 05 2022 Stanislav Levin <slev@altlinux.org> 30.0.0-alt1
- Initial build for Sisyphus.
