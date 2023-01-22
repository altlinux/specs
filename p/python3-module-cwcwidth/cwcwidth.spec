%define oname cwcwidth

%def_without check

Name: python3-module-cwcwidth
Version: 0.1.8
Release: alt1

Summary: Python bindings for wc(s)width

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cwcwidth/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

%description
cwcwidth provides Python bindings for wcwidth and wcswidth functions
defined in POSIX.1-2001 and POSIX.1-2008 based on Cython.
These functions compute the printable length of a unicode character/string on a terminal.
The module provides the same functions as wcwidth and its behavior is compatible.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --no-deps -s false -- -vra

%files
%doc README.md LICENSE
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 0.1.8-alt1
- new version 0.1.8 (with rpmrb script)

* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- new version 0.1.7 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- new version 0.1.6 (with rpmrb script)

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- initial build for ALT Sisyphus
