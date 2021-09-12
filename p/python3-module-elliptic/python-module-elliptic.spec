%define oname pyelliptic

Name: python3-module-elliptic
Version: 2.0.1
Release: alt1

Summary: Python OpenSSL wrapper for modern cryptography with ECC, AES, HMAC, Blowfish

Group: Development/Python3
License: MIT
Url: https://github.com/radfish/pyelliptic

# Source-url: https://github.com/radfish/pyelliptic/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
Base58 and Base58Check implementation compatible with
what is used by the bitcoin network.
Any other alternative alphabet (like the XRP one) can be used.


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{oname}*.egg-info

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Linux Sisyphus
