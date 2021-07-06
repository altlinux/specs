%define oname click-didyoumean

Name: python3-module-click-didyoumean
Version: 0.0.3
Release: alt2

Summary: Enable git-like did-you-mean feature in click

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/click-didyoumean/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-click

%description
Enable git-like did-you-mean feature in click.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_test

%check
python3 setup.py test

%files
%doc README.*
%python3_sitelibdir/*

%changelog
* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt2
- initial build for ALT Sisyphus

