Name: libuldaq
Version: 1.2.1
Release: alt2

Summary: MCC Universal Library for Linux
License: MIT
Group: System/Libraries

Url: https://github.com/mccdaq/uldaq

# Source-url: https://github.com/mccdaq/uldaq/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libusb-devel

%description
Contains a library to access and control supported Measurement Computing DAQ devices.


%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Headers for building software that uses %name.

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary

%prep
%setup
sed -i -e "s@udevadm@false@" Makefile.am
sed -i -e "s@ldconfig@true@" Makefile.am
sed -i -e "s@/lib/udev/rules.d@%_udevrulesdir@" Makefile.am

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
#LD_LIBRARY_PATH=. ./botan-test

%files
#%dir /etc/uldaq/
#/etc/uldaq/fpga/
%_udevrulesdir/*.rules
%_libdir/*.so.*

%files devel
#_bindir/*
%_docdir/%name/
%_includedir/uldaq.h
%_libdir/*.so
%_pkgconfigdir/*.pc

#files doc
#%doc %_defaultdocdir/botan-%version

%changelog
* Sun Sep 01 2024 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- use _udevrulesdir to install udev rules

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Mon May 11 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Tue Mar 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt2
- fix summary

* Tue Mar 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for Sisyphus

