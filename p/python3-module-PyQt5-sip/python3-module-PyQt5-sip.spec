%define oname PyQt5_sip

Name: python3-module-PyQt5-sip
Version: 12.8.1
Release: alt1

Summary: The sip module support for PyQt5

License: GPLv3
Url: http://www.riverbankcomputing.co.uk/software/pyqt
Group: Development/Python

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

BuildRequires: python3-module-sip5 >= 5.4.0

BuildRequires(pre): rpm-build-python3 >= 0.1.9.2-alt1
BuildRequires: gcc-c++ python3-devel

%description
The sip extension module provides support for the PyQt5 package.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%dir %python3_sitelibdir/PyQt5/
%python3_sitelibdir/PyQt5/sip*.so
%python3_sitelibdir/%oname-%version-*.egg-info

%changelog
* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 12.8.1-alt1
- initial separate build for ALT Sisyphus
