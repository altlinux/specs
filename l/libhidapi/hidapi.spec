# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/fox-config gcc-c++ libusb-compat-devel pkgconfig(fox17) pkgconfig(libudev) pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname hidapi
%global commit d17db57b9d4354752e0af42f5f33007a42ef2906
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libhidapi
Version:        0.8.0
Release:        alt1_0.2.%{shortcommit}
Summary:        Library for communicating with USB and Bluetooth HID devices

Group:          Development/C
License:        GPLv3 or BSD
URL:            http://www.signal11.us/oss/hidapi/

Source0:        https://github.com/signal11/hidapi/archive/%{commit}/%{oldname}-%{version}-%{shortcommit}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
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
Requires: %{name}%{?_isa} = %{version}
Provides: hidapi-devel = %{version}-%{release}

%description devel
This package contains development files for hidapi which provides access to
USB and Bluetooth HID-class devices.

%prep
%setup -n %{oldname}-%{version} -qn %{oldname}-%{commit}

%build
autoreconf -vif
%configure --disable-testgui --disable-static
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_defaultdocdir}/%{oldname}

%files
%doc AUTHORS.txt README.txt LICENSE*.txt
%{_libdir}/libhidapi-*.so.*

%files devel
%{_includedir}/hidapi
%{_libdir}/libhidapi-hidraw.so
%{_libdir}/libhidapi-libusb.so
%{_libdir}/pkgconfig/hidapi-hidraw.pc
%{_libdir}/pkgconfig/hidapi-libusb.pc

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.2.d17db57
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.1.d17db57
- update to new release by fcimport

* Mon Dec 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_4.a88c724
- new version

