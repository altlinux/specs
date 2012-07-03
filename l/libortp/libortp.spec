Name: libortp
Version: 0.20.0
Release: alt1

Group: System/Libraries
Summary: Real-time Transport Protocol Stack
Url: http://www.linphone.org/eng/documentation/dev/ortp.html
License: LGPL

Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: doxygen glibc-devel libssl-devel

%description
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

%package devel
Summary: Headers, libraries and docs for the oRTP library
Group: Development/C
Requires: %name = %version-%release
Conflicts: libortp0.7-devel

%description devel
oRTP is a LGPL licensed C library implementing the RTP protocol
(rfc1889). It is available for most unix clones (primilarly Linux and
HP-UX), and Microsoft Windows.

This package contains header files and development libraries needed to
develop programs using the oRTP library.

%prep
%setup
%patch0 -p1

%build
%define _optlevel 3
%add_optflags %optflags_shared %optflags_strict %optflags_notraceback -fno-schedule-insns -fschedule-insns2
%ifarch %ix86
%add_optflags -malign-double
%endif
./autogen.sh
%configure \
    --disable-static \
    --enable-shared
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%make install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_libdir/*.so.*

%files devel
%exclude %_docdir/ortp
%doc doc/html
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*

%changelog
* Sun Jun 24 2012 Alexei Takaseev <taf@altlinux.org> 0.20.0-alt1
- 0.20.0

* Sat Jan 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Fri Jul 22 2011 Egor Glukhov <kaman@altlinux.org> 0.16.5-alt1
- 0.16.5

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 0.16.4-alt1
- 0.16.4

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.3-alt1.git.53407402.1
- Rebuilt for soname set-versions

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 0.16.3-alt1.git.53407402
- updated from upstream git

* Thu Apr 01 2010 Sergey V Turchin <zerg@altlinux.org> 0.16.1-alt1
- initial specfile

