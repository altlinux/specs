%define _name hidapi

Name: libhidapi
Version: 0.14.0
Release: alt1

Summary: Library for communicating with USB and Bluetooth HID devices
License: GPLv3 or BSD
Group: Development/Other
Url: https://github.com/libusb/hidapi
Packager: Yuri N. Sedunov <aris@altlinux.org>

Vcs: https://github.com/libusb/hidapi.git

Source: https://github.com/libusb/hidapi/archive/%_name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ctest
BuildRequires: /usr/bin/fox-config
BuildRequires: libudev-devel
BuildRequires: libusb-devel

Provides: hidapi = %EVR

%description
HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X. On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.

%package devel
Group: Development/C
Summary: Development files for hidapi
Requires: %name = %EVR
Provides: %_name-devel = %EVR

%description devel
This package contains development files for hidapi which provides access to
USB and Bluetooth HID-class devices.

%prep
%setup -n %_name-%_name-%version

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%_libdir/lib%_name-*.so.*
%doc AUTHORS.txt README.md LICENSE*.txt

%files devel
%_includedir/%_name/
%_libdir/cmake/%_name
%_libdir/lib%_name-hidraw.so
%_libdir/lib%_name-libusb.so
%_pkgconfigdir/%_name-hidraw.pc
%_pkgconfigdir/%_name-libusb.pc

%changelog
* Sat Mar 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0
- spec adapted for ALT

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 0.12.0-alt1_1
- update to new release by fcimport

* Fri Jan 21 2022 Igor Vlasenko <viy@altlinux.org> 0.11.2-alt1_1
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.11.0-alt1_1
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_2
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_2
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.10.d17db57
- update to new release by fcimport

* Thu Nov 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1_0.6.d17db57
- Rebuild with stable libfox-1.6.x.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.5.d17db57
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.3.d17db57
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.2.d17db57
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.1.d17db57
- update to new release by fcimport

* Mon Dec 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_4.a88c724
- new version

