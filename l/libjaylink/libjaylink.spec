Name: libjaylink
Version: 0.4.0
Release: alt2

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
install -pm0644 -D contrib/60-libjaylink.rules %buildroot%_udevrulesdir/60-libjaylink.rules

%pre
/usr/sbin/groupadd -r -f plugdev &>/dev/null ||:

%files
%_udevrulesdir/*.rules
%_libdir/*.so.*

%files devel
%doc AUTHORS COPYING HACKING NEWS README* 
%_includedir/libjaylink
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Dec 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.0-alt2
- create plugdev group used in udev rules (closes: 52357)

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.0-alt1
- 0.4.0 released

* Wed Sep 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

* Tue Aug 16 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Mon Dec 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
