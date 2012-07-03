Packager: Denis Smirnov <mithraen@altlinux.ru>

Name: libsrtp
Version: 1.4.2
Release: alt2

Summary: Secure Real-time Transport Protocol implementation
License: BSD-like
Group: System/Libraries

Url: http://srtp.sourceforge.net/srtp.html
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jun 19 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
The libSRTP library is an open-source implementation of the Secure Real-time
Transport Protocol (SRTP) originally authored by Cisco Systems, Inc. It is
available under a BSD-style license.

SRTP is a security profile for RTP that adds confidentiality, message
authentication, and replay protection to that protocol. It is specified in RFC
3711

%prep
%setup

%build
touch NEWS AUTHORS ChangeLog
%autoreconf
%configure --enable-pic
%make_build

%check
make runtest

%install
%makeinstall

%files
%dir %_includedir/srtp
%_includedir/srtp/*.h
%_libdir/libsrtp.a

%changelog
* Sun Jul 25 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt2
- cleanup spec
- add auto tests

* Sun May 28 2006 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt1
- first build for Sisyphus
