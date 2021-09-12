%define oname base58

Name: python3-module-base58
Version: 2.1.0
Release: alt1

Summary: Base58 and Base58Check implementation

Group: Development/Python
License: MIT
Url: https://pypi.org/project/base58/

# Source-url: %__pypi_url %oname
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
%_bindir/base58
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{oname}*.egg-info

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Linux Sisyphus
