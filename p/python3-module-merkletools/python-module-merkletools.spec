%define oname merkletools

Name: python3-module-merkletools
Version: 1.0.3
Release: alt1

Summary: Merkle Tools

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/merkletools/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
Merkle Tools

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{oname}*.egg-info

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Linux Sisyphus
