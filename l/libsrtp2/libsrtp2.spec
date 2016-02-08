#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: libsrtp2
Summary: Secure Real-time Transport Protocol implementation
Version: 2.0.0
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

%package -n libsrtp2_1
Summary: %summary
Group: System/Libraries

%description -n libsrtp2_1
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
sed -i 's/#include "srtp_priv.h"/#include "srtp.h"/' %buildroot%_includedir/srtp2/ekt.h

%files devel
%dir %_includedir/srtp2
%_includedir/srtp2/*.h
%_libdir/libsrtp2.so
%_pkgconfigdir/libsrtp2.pc

%files devel-static
%_libdir/libsrtp2.a

%files -n libsrtp2_1
%_libdir/libsrtp2.so.1*

%changelog
* Mon Feb 08 2016 Denis Smirnov <mithraen@altlinux.ru> 2.0.0-alt1
- 2.0.0

