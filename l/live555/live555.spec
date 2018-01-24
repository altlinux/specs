Name: live555
Version: 20140725
Release: alt2

Summary: Live555.com Streaming Media Library Utilities
License: LGPL
Group: System/Libraries
Url: http://www.live555.com/liveMedia/

Source: %name-%version-%release.tar

Requires: lib%name = %version-%release
# renamed...
Provides: live = %version-%release
Obsoletes: live < %version-%release

BuildRequires: gcc-c++

%description
This code forms a set of C++ libraries for multimedia streaming, using
open standard protocols (RTP/RTCP, RTSP, SIP). These libraries - which
can be compiled for Unix (including Linux and Mac OS X), Windows, and
QNX (and other POSIX-compliant systems) - can be used to build
streaming applications.

This package contains the example apps of live555.com.

%package -n lib%name
Summary: Live555.com Streaming Media Library
Group: System/Libraries
Provides: liblive555-0 = %version-%release
Obsoletes: liblive555-0

%package -n lib%name-devel
Summary: Development files of the Live555.com Streaming Media Library
Group: Development/C++
Requires: lib%name = %version-%release
Provides: liblive-devel = %version-%release
Obsoletes: liblive-devel < %version-%release

%description -n lib%name
This code forms a set of C++ libraries for multimedia streaming, using
open standard protocols (RTP/RTCP, RTSP, SIP). These libraries - which
can be compiled for Unix (including Linux and Mac OS X), Windows, and
QNX (and other POSIX-compliant systems) - can be used to build
streaming applications.

This package contains live555 libraries.

%description -n lib%name-devel
This code forms a set of C++ libraries for multimedia streaming, using
open standard protocols (RTP/RTCP, RTSP, SIP). These libraries - which
can be compiled for Unix (including Linux and Mac OS X), Windows, and
QNX (and other POSIX-compliant systems) - can be used to build
streaming applications.

This package contains all needed files to build programs based on live555.com.

%prep
%setup

%build
./genMakefiles linux
%make_build CFLAGS='%optflags %optflags_shared'

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir

for f in BasicUsageEnvironment UsageEnvironment groupsock; do
echo 'INPUT(AS_NEEDED(%_libdir/libliveMedia.so))' >%buildroot%_libdir/lib$f.so
done

%files
%doc COPYING README
%_bindir/*

%files -n lib%name
%_libdir/libliveMedia.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/BasicUsageEnvironment
%_includedir/UsageEnvironment
%_includedir/groupsock
%_includedir/liveMedia

%changelog
* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20140725-alt2
- Fixed build with new glibc.

* Sat Jun 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 20140725-alt1
- 20140725 snapshot

* Wed Dec 10 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 20140527-alt1
- 20140527 snapshot

* Tue Oct 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 20120913-alt1
- 20120913 snapshot

* Wed Jan 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 20120125-alt1
- 20120125 snapshot

* Fri Dec 16 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 20111202-alt1
- 20111202 snapshot

* Tue Nov 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 20111108-alt1
- 20111108 snapshot

* Wed Oct 19 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 20111018-alt1
- 20111118 snapshot

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt0.2009.04.20.1
- Rebuilt for soname set-versions

* Tue May 12 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2009.04.20
- 2009.04.20 version.
- Introduced shared library (thanks Fedora and Debian folks for patches).

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2008.07.25
- 2008.07.25 version.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2007.11.01
- 2007.11.01 version.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2007.08.03a
- 2007.08.03a version.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2007.05.24
- 2007.05.24 version.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2007.04.24a
- 2007.04.24a version.

* Sun Mar 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2007.02.20
- 2007.02.20 version.

* Thu Sep 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2006.09.07
- 2006.09.07 version.

* Sun Aug 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2006.08.07
- 2006.08.07 version.
- Renamed to live555.

* Mon Jul 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2006.07.04
- 2006.07.04 version.

* Fri Jun 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2006.05.17
- 2006.05.17 version.

* Tue May 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2006.05.15
- 2006.05.15 version.

* Sat Dec 10 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.0.0-alt0.2005.12.09
- Initial build for ALT Linux.
- specfile is based on Mandriva's spec.

