%define oname buildozer

Name: python3-module-buildozer
Version: 1.5.0
Release: alt1

Summary: Generic Python packager for Android and iOS

Group: Development/Python3
License: MIT License
Url: https://github.com/kivy/buildozer

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%description
Buildozer is a tool that aim to package mobiles application easily.
It automates the entire build process, download the prerequisites like python-for-android, Android SDK, NDK, etc.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.md
%_bindir/buildozer
%_bindir/buildozer-remote
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info/

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- initial build for ALT Sisyphus

* Tue Apr 20 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 1.2.0-alt1
- new version (1.2.0) with rpmgs script

