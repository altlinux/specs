%define _unpackaged_files_terminate_build 1
%define oname mergedeep

%def_with check

Name: python3-module-%oname
Version: 1.3.4
Release: alt2

Summary: Deep merge function
License: MIT
Group: Development/Python3
# Source-git: https://github.com/clarketm/mergedeep.git
Url: https://pypi.org/project/mergedeep/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
Deep merge function.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm %buildroot%python3_sitelibdir/%oname/test_mergedeep.py

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt2
- Moved on modern pyproject macros.

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 1.3.4-alt1
- Initial build.
