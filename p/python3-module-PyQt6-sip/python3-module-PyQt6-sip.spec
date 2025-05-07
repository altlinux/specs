%define oname PyQt6_sip

Name: python3-module-PyQt6-sip
Version: 13.6.0
Release: alt1.1

Summary: The sip module support for PyQt6

License: GPLv3
Url: http://www.riverbankcomputing.co.uk/software/pyqt
Group: Development/Python3

# Source0-url: %__pypi_url %oname
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
The sip extension module provides support for the PyQt6 package.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%dir %python3_sitelibdir/PyQt6/
%python3_sitelibdir/PyQt6/sip*.so
%python3_sitelibdir/%{pyproject_distinfo PyQt6-sip}/

%changelog
* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 13.6.0-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Mon Nov 13 2023 Anton Midyukov <antohami@altlinux.org> 13.6.0-alt1
- new version (13.6.0) with rpmgs script

* Mon Apr 24 2023 Anton Midyukov <antohami@altlinux.org> 13.5.1-alt1
- initial build
