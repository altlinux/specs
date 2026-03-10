# TODO: aggdraw
%define  modulename psd_tools

Name:    python3-module-psd-tools
Version: 1.14.0
Release: alt1

Summary: Python package for reading Adobe Photoshop PSD files

License: MIT
Group:   Development/Python3
URL:     https://github.com/psd-tools/psd-tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: gcc-c++

%py3_use docopt >= 0.6.0
%py3_use attrs >= 23.0.0
%py3_use Pillow >= 10.0.0
%py3_use aggdraw
%py3_use numpy
%py3_use scipy
%py3_use scikit-image

# Source-url: https://github.com/psd-tools/psd-tools/archive/v%version.tar.gz
Source: %name-%version.tar

%description
psd-tools is a Python package for working with
Adobe Photoshop PSD files as described in specification.

Note:
In order to extract images from 32bit PSD files PIL/Pillow
must be built with LITTLECMS or LITTLECMS2 support.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/psd-tools
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.dist-info

%changelog
* Sat Mar 07 2026 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- new version 1.14.0

* Sun Mar 03 2024 Vitaly Lipatov <lav@altlinux.ru> 1.9.31-alt1
- new version 1.9.31
- switch to pyproject_build

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1.9.28-alt1
- new version 1.9.28 (with rpmrb script)

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1.9.24-alt1
- new version 1.9.24 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.9.23-alt1
- new version 1.9.23 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt1
- new version 1.9.21 (with rpmrb script)

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt1
- new version 1.9.18 (with rpmrb script)

* Wed Jun 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt1
- new version 1.9.17 (with rpmrb script)

* Sat Oct 17 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.16-alt1
- initial build for ALT Sisyphus
