%define oname kivy-garden

Name: python3-module-kivy-garden
Version: 0.1.4
Release: alt2

Summary: The kivy garden installation script

Group: Development/Python3
License: MIT License
Url: https://github.com/kivy-garden

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel


%description
The kivy garden installation script, split into its own package for convenient use in buildozer.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -v %buildroot%_bindir/garden.bat

%files
%doc README.md
%_bindir/garden
%python3_sitelibdir/garden/
%python3_sitelibdir/*.egg-info/

%changelog
* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt2
- initial build for ALT Sisyphus

* Sat Apr 17 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 0.1.4-alt1
- new version (0.1.4) with rpmgs script


