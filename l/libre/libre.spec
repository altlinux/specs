%define oname re
Name: libre
Version: 0.5.7
Release: alt1

Summary: Library for real-time communications with async IO support and a complete SIP stack

License: BSD Revised
Group: System/Libraries
Url: http://www.creytiv.com/re.html


Source: http://www.creytiv.com/pub/%oname-%version.tar

BuildRequires: libssl-devel zlib-devel

%description
Libre is a portable and generic library for real-time communications
with async IO support and a complete SIP stack with support for SDP,
RTP/RTCP, STUN/TURN/ICE, BFCP and DNS Client.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %oname-%version

%build
%make_build RELEASE=1

%install
%makeinstall_std LIBDIR=%_libdir
rm -f %buildroot%_libdir/lib%oname.a

%files
%doc docs/*
# FIXME?
%_libdir/lib%oname.so

%files devel
%_includedir/%oname/
%_datadir/%oname/
#%_libdir/lib%oname.so
%_pkgconfigdir/*.pc

%changelog
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
