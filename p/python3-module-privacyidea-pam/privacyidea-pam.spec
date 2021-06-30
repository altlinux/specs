%define oname privacyidea-pam

Name: python3-module-%oname
Version: 2.11.0
Release: alt2

Summary: This module can be used to authenticate with OTP against privacyIDEA

License: AGPLv3
Group: Development/Python
Url: https://github.com/privacyidea/pam_python

# Source-git: https://github.com/privacyidea/pam_python.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro

# for test
BuildRequires: python3 >= 2.7
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-responses >= 0.10.9
BuildRequires: python3-module-passlib
BuildRequires: python3-module-requests

Requires: pam_python

%description
This module is to be used with http://pam-python.sourceforge.net/.
It can be used to authenticate with OTP against privacyIDEA.
It will also cache future OTP values to enable offline authentication.

%prep
%setup

%build
%python3_build

%install
%python3_install
#mkdir -p %buildroot/etc/privacyidea

%check
%python3_test

%files
%python3_sitelibdir/*

%changelog
* Fri Mar 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt2
- build python3 module

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt1
- initial build for ALT Sisyphus
