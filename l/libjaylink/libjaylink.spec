Name: libjaylink
Version: 0.3.1
Release: alt1

Summary: Access library for SEGGER J-Link and complatible devices
License: GPLv2
Group: System/Libraries
Url: https://gitlab.zapb.de/libjaylink/libjaylink

Source: %name-%version-%release.tar
BuildRequires: libusb-devel

%package devel
Summary: Access library for SEGGER J-Link and complatible devices
Group: Development/C

%description
%summary

%description devel
%summary
This package contains develkpment part.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%doc AUTHORS COPYING HACKING NEWS README* 
%_includedir/libjaylink
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Sep 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

* Tue Aug 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Mon Dec 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
