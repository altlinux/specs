%define oname PyQt5_sip

Name: python3-module-PyQt5-sip
Version: 12.15.0
Release: alt1

Summary: The sip module support for PyQt5

License: GPL-3.0-only
Url: http://www.riverbankcomputing.co.uk/software/pyqt
Group: Development/Python

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 >= 0.1.9.2-alt1
BuildRequires: gcc-c++ python3-devel
BuildRequires: python3-module-setuptools
# for setuptools < 70.1.0
BuildRequires: python3-module-wheel

%description
The sip extension module provides support for the PyQt5 package.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%dir %python3_sitelibdir/PyQt5/
%python3_sitelibdir/PyQt5/sip*.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu Oct 31 2024 Anton Midyukov <antohami@altlinux.org> 12.15.0-alt1
- new version (12.15.0) with rpmgs script
- migration to PEP517

* Thu Nov 09 2023 Anton Midyukov <antohami@altlinux.org> 12.13.0-alt1
- new version (12.13.0) with rpmgs script

* Thu Aug 04 2022 Vitaly Lipatov <lav@altlinux.ru> 12.11.0-alt1
- new version 12.11.0 (with rpmrb script)

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 12.9.0-alt2
- don't need sip for build

* Tue Jul 13 2021 Vitaly Lipatov <lav@altlinux.ru> 12.9.0-alt1
- new version 12.9.0 (with rpmrb script)

* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 12.8.1-alt1
- initial separate build for ALT Sisyphus
