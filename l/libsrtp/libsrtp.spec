#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: libsrtp
Summary: Secure Real-time Transport Protocol implementation
Version: 1.5.4
Release: alt1
License: BSD-like
Group: System/Libraries
BuildRequires: gcc-c++ libstdc++-devel
Packager: Denis Smirnov <mithraen@altlinux.ru>
Url: https://github.com/cisco/libsrtp
Source: %name-%version.tar
Source100: %name.watch
Patch1: %name-%version-%release.patch

%package devel
Summary: %summary
Group: System/Libraries

%description devel
%summary

%package devel-static
Summary: %summary
Group: System/Libraries
Requires: %name-devel

%description devel-static
%summary

%package -n libsrtp1
Summary: %summary
Group: System/Libraries
Obsoletes: libsrtp < %version-%release
Conflicts: libsrtp < %version-%release
Provides:  libsrtp = %version-%release

%description -n libsrtp1
%summary

%description
The libSRTP library is an open-source implementation of the Secure Real-time
Transport Protocol (SRTP) originally authored by Cisco Systems, Inc. It is
available under a BSD-style license.
SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is specified in RFC
3711


%prep
%setup
%patch1 -p1

%build
touch NEWS AUTHORS ChangeLog
%autoreconf
export CFLAGS
CFLAGS="$CFLAGS -fPIC -Wall -O2 -fexpensive-optimizations -funroll-loops"
%configure --enable-pic
%make_build all shared_library
%check

%install
%makeinstall

%files devel
%dir %_includedir/srtp
%_includedir/srtp/*.h
%_libdir/libsrtp.so
%_pkgconfigdir/libsrtp.pc

%files devel-static
%_libdir/libsrtp.a

%files -n libsrtp1
%_libdir/libsrtp.so.*

%changelog
* Mon Feb 08 2016 Denis Smirnov <mithraen@altlinux.ru> 1.5.4-alt1
- new version 1.5.4

* Mon Feb 08 2016 Denis Smirnov <mithraen@altlinux.ru> 1.5.3-alt2
- fix watch file

* Sat Nov 28 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.3-alt1
- 1.5.3
- CVE-2015-6360

* Mon Nov 23 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt2
- Fix shared library (ALT #31448)

* Sun Nov 08 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt1
- 1.5.2
- add watch-file
- Build shared library (ALT #31448)

* Sat Jan 17 2015 Denis Smirnov <mithraen@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Thu Oct 18 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt2
- build with -fPIC

* Mon Oct 15 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt2
- cleanup spec
- add auto tests

* Sun May 28 2006 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt1
- first build for Sisyphus

