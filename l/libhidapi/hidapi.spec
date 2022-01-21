# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/fox-config gcc-c++
# END SourceDeps(oneline)
Group: Development/Other
%add_optflags %optflags_shared
%define oldname hidapi
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libhidapi
Version:        0.11.2
Release:        alt1_1
Summary:        Library for communicating with USB and Bluetooth HID devices

License:        GPLv3 or BSD
URL:            https://github.com/libusb/hidapi

Source0:        https://github.com/libusb/hidapi/archive/%{oldname}-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: libudev-devel
BuildRequires: libusb-devel
BuildRequires: m4
Source44: import.info
Provides: hidapi = %{version}-%{release}

%description
HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X.  On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.

%package devel
Group: Development/C
Summary: Development files for hidapi
Requires: %{name} = %{version}-%{release}
Provides: hidapi-devel = %{version}-%{release}

%description devel
This package contains development files for hidapi which provides access to
USB and Bluetooth HID-class devices.

%prep
%setup -q -n %{oldname}-%{oldname}-%{version}


%build
autoreconf -vif
%configure --disable-testgui --disable-static
%make_build V=1

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_defaultdocdir}/%{oldname}



%files
%doc AUTHORS.txt README.md LICENSE*.txt
%{_libdir}/libhidapi-*.so.*

%files devel
%{_includedir}/hidapi
%{_libdir}/libhidapi-hidraw.so
%{_libdir}/libhidapi-libusb.so
%{_libdir}/pkgconfig/hidapi-hidraw.pc
%{_libdir}/pkgconfig/hidapi-libusb.pc

%changelog
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

