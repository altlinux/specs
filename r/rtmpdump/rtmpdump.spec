Name:		rtmpdump
Version:	2.4
Release:	alt1

Summary:	An utility toolkit for RTMP streams
License:	GPLv2
Group:		Sound

Source:		%name-%version-%release.tar

Requires: librtmp = %version-%release

BuildRequires: libssl-devel zlib-devel

%package -n librtmp
Summary: RTMPDump Real-Time Messaging Protocol API - shared library
License: LGPLv2+
Group: System/Libraries

%package -n librtmp-devel
Summary: RTMPDump Real-Time Messaging Protocol API - development headers
Group: Development/C
Requires: librtmp = %version-%release

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://

You can read the rtmpdump manpage and the rtmpgw manpage online as well.

rtmpsrv is a stub for a server; it logs the connect and play parameters
from a regular client that connects to it. It then invokes rtmpdump with
those parameters to retrieve the stream.

rtmpsuck is a transparent proxy; it intercepts connections from a client
and then makes an outbound connection to the real server. After all
handshaking is complete and encryption keys with both sides are
negotiated, it records the cleartext stream data into files while
relaying the data from the server to the client.

%description -n librtmp
rtmpdump is a toolkit for RTMP streams.

This package contains RTMPDump shared library.

%description -n librtmp-devel
rtmpdump is a toolkit for RTMP streams.

This package contains RTMPDump library development headers.

%prep
%setup

%build
%make_build prefix=/usr all

%install

%make_install DESTDIR=%buildroot prefix=/usr mandir=%_mandir libdir=%_libdir install

%files
%doc README ChangeLog *html
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man8dir/*

%files -n librtmp
%_libdir/*.so.*

%files -n librtmp-devel
%_libdir/*.so
%_includedir/librtmp
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Tue Oct 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 (semi-)released

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt for soname set-versions

* Thu Jul 01 2010 Konstantin Pavlov <thresh@altlinux.org> 2.3-alt1
- 2.3 release.

* Wed Jun 30 2010 Konstantin Pavlov <thresh@altlinux.org> 2.2f-alt1.svn524
- SVN build #524, past 2.2e release.
- Introduce shared library librtmp (plus devel and static subpackages).

* Thu May 06 2010 Fr. Br. George <george@altlinux.ru> 2.2d-alt1
- Initial build from scratch

