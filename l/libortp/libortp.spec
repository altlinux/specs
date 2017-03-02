Name: libortp
Version: 1.0.1
Release: alt1

Group: System/Libraries
Summary: Real-time Transport Protocol Stack
Url: http://www.linphone.org/eng/documentation/dev/ortp.html
License: LGPL

Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: doxygen glibc-devel libbctoolbox-devel

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
%doc AUTHORS COPYING ChangeLog NEWS README.md
%_libdir/*.so.*

%files devel
%exclude %_docdir/ortp*
%doc doc/html
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*

%changelog
* Fri Mar 03 2017 Alexei Takaseev <taf@altlinux.org> 1.0.1-alt1
- 1.0.1

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 0.27.0-alt1
- 0.27.0

* Fri May 27 2016 Alexei Takaseev <taf@altlinux.org> 0.26.0-alt1
- 0.26.0

* Tue Nov 03 2015 Alexei Takaseev <taf@altlinux.org> 0.25.0-alt1
- 0.25.0

* Fri May 08 2015 Alexei Takaseev <taf@altlinux.org> 0.24.2-alt1
- 0.24.2

* Wed Apr 01 2015 Alexei Takaseev <taf@altlinux.org> 0.24.1-alt1
- 0.24.1

* Thu Mar 12 2015 Alexei Takaseev <taf@altlinux.org> 0.24.0-alt1
- 0.24.0

* Mon Mar 03 2014 Alexei Takaseev <taf@altlinux.org> 0.22.0-alt3
- fix very stupid bugs in various place of oRTP

* Wed Feb 26 2014 Alexei Takaseev <taf@altlinux.org> 0.22.0-alt2
- Build for linphone 3.7.0

* Thu Jun 13 2013 Alexei Takaseev <taf@altlinux.org> 0.22.0-alt1
- 0.22.0

* Sat Mar 16 2013 Alexei Takaseev <taf@altlinux.org> 0.21.1-alt1
- 0.21.1

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

