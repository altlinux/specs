%define _unpackaged_files_terminate_build 1
%define oname argon2-cffi

%def_without check

Name: python3-module-%oname
Version: 20.1.0
Release: alt1

Summary: The secure Argon2 password hashing algorithm

License: MIT
Group: Development/Python3
Url: https://github.com/hynek/argon2-cffi

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: libargon2-devel >= 20171227

%py3_use cffi >= 1.0.0

%if_with check
%endif

%description
CFFI-based Argon2 Bindings for Python.

Argon2 won the Password Hashing Competition
and argon2-cffi is the simplest way to use it in Python and PyPy.

%prep
%setup
# remove bundled libs in favor of system ones
rm -r extras/

%build
export ARGON2_CFFI_USE_SYSTEM=1
%python3_build_debug

%install
%python3_install

%check
%if_with check
%python3_check
%endif

%files
%doc *.rst
%python3_sitelibdir/argon2*-%version-py%_python3_version.egg-info/
%python3_sitelibdir/argon2/

%changelog
* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 20.1.0-alt1
- initial build for ALT Sisyphus
