%define oname pep517

Name: python3-module-pep517
Version: 0.10.0
Release: alt2

Summary: API to call PEP 517 hooks for building Python packages

Group: Development/Python3
License: MIT License
Url: https://github.com/pypa/pep517

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel


%description
PEP 517 specifies a standard API for systems which build Python packages.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info/

%changelog
* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- initial build for ALT Sisyphus

* Tue Apr 20 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 0.10.0-alt1
- new version (0.10.0) with rpmgs script



