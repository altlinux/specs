%define oname josepy

Name: python3-module-%oname
Version: 1.13.0
Release: alt1

Summary: JOSE protocol implementation in Python using cryptography

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/certbot/josepy

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.1.3
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel python3-module-setuptools

%py3_provides %oname

%description
JOSE protocol implementation in Python using cryptography.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/*/*test*
rm -rf %buildroot%python3_sitelibdir/*/*/*test*
rm -rf %buildroot%_bindir/

%check
%python3_check
# Make sure the script uses the expected python version
#grep -q python3 %buildroot%_bindir/jws

%files
%doc README*
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Sat Oct 09 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- build python3 module separately, drop tests subpackage

* Thu Jul 23 2020 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- moved tests from python3-module-%oname package
- fix for License tag according to SPDX

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

