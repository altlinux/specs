%define oname uldaq
Name: python3-module-%oname
Version: 1.1.2
Release: alt1

Summary: Universal Library Python API for Measurement Computing DAQ devices

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/uldaq/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: libuldaq-devel
Requires: libuldaq >= 1.1.2

%description
The uldaq Python package contains an API (Application Programming Interface)
for interacting with Measurement Computing DAQ devices.
The package is implemented as an object-oriented wrapper
around the UL for Linux C API using the ctypes Python library.

%package examples
Summary: Examples for %oname
Group: Development/Documentation
Requires: %name = %EVR

%description examples
Examples for %name.


%prep
%setup
%__subst "s|libuldaq.so|libuldaq.so.1|" uldaq/ul_c_interface.py

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%files examples
%doc examples

%changelog
* Tue Mar 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for Sisyphus
