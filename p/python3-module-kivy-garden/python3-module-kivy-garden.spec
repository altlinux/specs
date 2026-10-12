%define oname kivy-garden

Name: python3-module-kivy-garden
Version: 0.1.5
Release: alt1

Summary: The kivy garden installation script

Group: Development/Python3
License: MIT License
Url: https://github.com/kivy-garden

BuildArch: noarch

# Source-url: https://files.pythonhosted.org/packages/source/k/kivy-garden/Kivy%20Garden-%version.tar.gz
Source: %name-%version.tar
Patch: fix-ez_setup.patch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel


%description
The kivy garden installation script, split into its own package for convenient use in buildozer.

%prep
%setup
%patch -p1

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
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.5-alt1
- new version 0.1.5
- fix Source-url (sdist is named Kivy Garden)
- add patch to drop missing ez_setup import

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt2
- initial build for ALT Sisyphus

* Sat Apr 17 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 0.1.4-alt1
- new version (0.1.4) with rpmgs script


