%define oname re
Name: libre
Version: 3.15.0
Release: alt1

Summary: Generic library for real-time communications with async IO support

License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/baresip/re

# Source-url: %url/archive/refs/tags/v%version.tar.gz
Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libssl-devel zlib-devel

%description
Libre is a portable and generic library for real-time communications
with async IO support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n %oname-%version

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
rm -f %buildroot/%_libdir/%name.a

%files
%doc CHANGELOG.md LICENSE README.md
%_libdir/%name.so.2*

%files devel
%_includedir/%oname/
%_libdir/%name.so
%_libdir/cmake/%name/
%_libdir/cmake/%oname/
%_pkgconfigdir/%name.pc

%changelog
* Tue Sep 10 2024 Ilya Demyanov <turbid@altlinux.org> 3.15.0-alt1
- new version 3.15.0

* Tue Jul 30 2024 Ilya Demyanov <turbid@altlinux.org> 3.14.0-alt1
- new version 3.14.0

* Thu Jun 27 2024 Ilya Demyanov <turbid@altlinux.org> 3.13.0-alt1
- new version 3.13.0

* Thu Apr 18 2024 Ilya Demyanov <turbid@altlinux.org> 3.11.0-alt1
- new version 3.11.0
- switch to cmake build system
- update description, urls and license

* Mon Mar 30 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.9-alt1
- new version 0.5.9 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.8-alt1
- new version 0.5.8 (with rpmrb script)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.5.7-alt1
- new version 0.5.7 (with rpmrb script)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.5-alt1
- new version 0.5.5 (with rpmrb script)

* Thu Jun 08 2017 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.5.3-alt1
- new version 0.5.3 (with rpmrb script)

* Tue Aug 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.17-alt1
- new version 0.4.17 (with rpmrb script)

* Fri Jan 02 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.11-alt1
- 0.4.11

* Mon May 26 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.7-alt1
- 0.4.8

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- initial build for ALT Linux Sisyphus
