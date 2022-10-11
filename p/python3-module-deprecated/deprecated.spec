%define _unpackaged_files_terminate_build 1
%define pypi_name Deprecated
%define mod_name deprecated

%def_with check

Name: python3-module-%mod_name
Version: 1.2.13
Release: alt1

Summary: Decorators to deprecate old python classes, functions or methods
License: MIT
Group: Development/Python3
# Source-git: https://github.com/tantale/deprecated.git
Url: https://pypi.org/project/Deprecated/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires
BuildRequires: python3(wrapt)

BuildRequires: python3(pytest)
%endif

BuildArch: noarch

# PyPI's name begins with capital letter
%py3_provides Deprecated

%description
Python @deprecated decorator to deprecate old python classes, functions or
methods.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.md CHANGELOG.rst
%python3_sitelibdir/deprecated/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 1.2.13-alt1
- 1.2.12 -> 1.2.13.

* Tue Jun 22 2021 Stanislav Levin <slev@altlinux.org> 1.2.12-alt1
- Initial build for Sisyphus.
