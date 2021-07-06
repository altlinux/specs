%define oname changefinder

Name: python3-module-changefinder
Version: 0.03
Release: alt1

Summary: Online Change-Point Detection Library based on ChangeFinder Algorithm

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/shunsukeaihara/changefinder

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
Online Change-Point Detection Library based on ChangeFinder Algorithm.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
#python3 setup.py test

%files
%doc README.rst
%python3_sitelibdir/*


%changelog
* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.03-alt1
- initial build for ALT Sisyphus
