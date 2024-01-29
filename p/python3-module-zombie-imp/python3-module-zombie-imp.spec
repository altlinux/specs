# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%def_with check

%define srcname zombie-imp
%define modulename zombie_imp

Name:    python3-module-%srcname
Version: 0.0.2
Release: alt1

Summary: A copy of the `imp` module that was removed in Python 3.12

License: Python-2.0.1
Group:   Development/Python3
URL:     https://pypi.org/project/zombie-imp
VCS:     https://github.com/encukou/zombie-imp

Source: %name-%version.tar

# Make the tests pass with Python 3.13.0a1+, 3.12.1+, 3.11.6+
# https://github.com/encukou/zombie-imp/commit/d45295faf4.patch
Patch: 0001-Make_the_tests_pass_with_Python_3.13.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-test
%endif

%description
A copy of the imp module that was removed in Python 3.12.
This is a compat package to ease transition to Python 3.12.
It shouldn't be used and packages using `imp` module
should use `importlib.metadata` instead.

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
%doc *.md
%python3_sitelibdir/imp.py
%python3_sitelibdir/__pycache__/*.pyc
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus (thx to antohami@).
