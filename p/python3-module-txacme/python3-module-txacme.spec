%define modulename txacme

Name: python3-module-txacme
Version: 0.9.3
Release: alt2

Summary: ACME protocol implementation for Twisted

Url: https://github.com/twisted/txacme
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/t/%modulename/%modulename-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
txacme is an implementation of the protocol for Twisted,
the event-driven networking engine for Python.

%prep
%setup

# hotfix for python3.12
sed -i 's/SafeConfigParser/ConfigParser/' versioneer.py
sed -i 's/readfp/read_file/' versioneer.py

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/integration/
rm -rfv %buildroot%python3_sitelibdir/txacme/test/

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/twisted/plugins/*
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt2
- Fixed FTBFS.

* Fri Sep 18 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt2
- drop tests from the package

* Sun Aug 04 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Sisyphus
