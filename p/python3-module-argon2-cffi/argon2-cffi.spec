%define oname argon2-cffi

%def_with check

Name: python3-module-%oname
Version: 23.1.0
Release: alt1

Summary: The secure Argon2 password hashing algorithm

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/argon2-cffi
VCS: https://github.com/hynek/argon2-cffi

Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme
BuildRequires: python3-module-hatch-vcs
BuildRequires: python3-module-setuptools-scm
BuildRequires: libargon2-devel >= 20171227

%if_with check
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-argon2-cffi-bindings
%endif

BuildArch: noarch

%description
CFFI-based Argon2 Bindings for Python.

Argon2 won the Password Hashing Competition
and argon2-cffi is the simplest way to use it in Python and PyPy.

%prep
%setup

%build
export ARGON2_CFFI_USE_SYSTEM=1
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/argon2_cffi-%version.dist-info
%python3_sitelibdir/argon2

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 23.1.0-alt1
- Build new version.
- Build with check.

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 20.1.0-alt1
- initial build for ALT Sisyphus
