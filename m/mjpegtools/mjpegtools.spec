%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define shver 2.1

Name: mjpegtools
Version: 2.2.1
Release: alt2

Summary: Tools for recording, editing, playing back mpeg-encoding video under linux
License: GPLv2
Group: Video
Url: http://mjpeg.sourceforge.net

Source: http://prdownloads.sourceforge.net/mjpeg/%name-%version.tar
Patch0: mjpegtools-2.1.0-debian-disable-sse2.patch
Patch1: mjpegtools-2.2.0-debian-mplex-ftbfs.patch
Patch2: mjpegtools-2.2.0-lavtools-ftbfs.patch

%define libdv_ver 0.9

Requires: lib%name%shver = %version-%release 
Requires: libdv >= %libdv_ver

BuildPreReq: libdv-devel >= %libdv_ver

BuildRequires: glibc-kernheaders libjpeg-devel libSDL_gfx-devel gcc-c++
BuildRequires: libpng-devel libXxf86dga-devel libgtk+2-devel libSDL-devel
BuildRequires: libXt-devel libv4l-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to mpeg) video under linux. Recording can
be done with zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into mpeg1/2 or divx video.

%ifarch %ix86
NOTE:
This binaries does ***NOT*** compatible with a K5/K6 or Pentium CPU
(due to the lack of SSE instructions).
%endif

%package -n lib%name%shver
Summary: Shared libraries for the mjpegtools
Group: System/Libraries
Obsoletes: %name-libs
Provides: %name-libs = %version-%release

%description -n lib%name%shver
This package contains shared libraries needed to run mjpegtools.

%ifarch %ix86
NOTE:
This binaries does ***NOT*** compatible with a K5/K6 or Pentium CPU
(due to the lack of SSE instructions).
%endif

%package -n lib%name-devel
Summary: Development headers and libraries for the mjpegtools
Group: Development/C
Obsoletes: %name-devel
Provides: %name-devel = %version-%release
Requires: lib%name%shver = %version-%release

%description -n lib%name-devel
This package contains libraries and header files needed to compile
applications that use part of the libraries of the mjpegtools package.

%package -n lib%name-devel-static
Summary: Static libraries for the mjpegtools
Group: Development/C
Obsoletes: %name-static-libs
Provides: %name-static-libs = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static libraries needed to compile applications
that use part of the libraries of the mjpegtools package.

%ifarch %ix86
NOTE:
This binaries does ***NOT*** compatible with a K5/K6 or Pentium CPU
(due to the lack of SSE instructions).
%endif

%prep
%setup
%ifnarch %ix86 x86_64
%patch0 -p1
%endif
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-large-file \
	--with-x \
%ifarch %ix86 x86_64
	--enable-simd-accel
%else
	--disable-simd-accel
%endif

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
export LD_LIBRARY_PATH=$PWD/utils/.libs
%make_build

%install
%makeinstall

sed -i 's,local/bin/,/bin/,' %buildroot%_bindir/*.sh

# remove non-packaged files
rm -f %buildroot%_infodir/dir

# remove unsupported transcode
rm -f %buildroot%_bindir/lavtc.sh

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS BUGS CHANGES HINTS PLANS README TODO

%files -n lib%name%shver
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%_man5dir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Fri Oct 27 2023 Anton Farygin <rider@altlinux.ru> 2.2.1-alt2
- removed lavtc.sh due to unsupported transcode

* Mon Oct 04 2021 Anton Farygin <rider@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sat Apr 10 2021 Anton Farygin <rider@altlinux.org> 2.2.0-alt1
- 2.2.0
- added patches for explicit linking against FTBFS

* Sun Apr 21 2019 Michael Shigorin <mike@altlinux.org> 2.1.0-alt3
- disable SSE on non-x86 (by conditionally applying debian patch)
- enable SSE on x86_64
- tweak descriptions
- restore static subpackage silently lost in -alt2

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt2
- disable quicktime support
- rebuilt for ffmpeg

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1.1.1
- NMU: added BR: texinfo

* Fri Dec 05 2014 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1.1
- rebuilt against libSDL_gfx.so.15

* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9.0-alt6.qa1
- NMU: rebuilt for updated dependencies.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt6
- Rebuilt with libpng15

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt5
- Fixed build

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt4
- Removed bad RPATH

* Tue Dec 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt3
- Rebuilt for soname set-versions

* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.9.0-alt2.1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for mjpegtools

* Wed May 13 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.9.0-alt2
- 1.9.0 release.

* Tue Oct 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.9.0-alt1.rc3
- Fix path to transcode.

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.9.0-alt0.rc3
- 1.9.0 rc3.

* Mon Mar 12 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.9.0-alt0.rc2
- 1.9.0 rc2.
- Dropped patch2 and patch3, as they merged upstream.
- Fix BuildRequires.

* Fri Oct 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.8.0-alt1
- 1.8.0 release.
- Added patch3 fixing assert issue.
- Updated patch1 and patch2.

* Mon Feb 20 2006 Alex Yustasov <yust@altlinux.ru> 1.7.0-alt0.4.1
- rebuild with libquicktime-0.9.8

* Mon Feb 13 2006 Alex Yustasov <yust@altlinux.ru> 1.7.0-alt0.4
- fixed build dependencies

* Sun Nov 20 2005 Alex Yustasov <yust@altlinux.ru> 1.7.0-alt0.3
- rebuild with new libquicktime.

* Tue Feb 22 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.7.0-alt0.2
- build current cvs snapshot.

* Wed Jan 19 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.7.0-alt0.1
- build 1.7.0 from cvs.

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.2-alt1.1
- rebuild with libdv-0.102

* Sun Feb 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Sun Jan 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1.93-alt1
- new version.

* Tue Dec 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1.92-alt1
- 1.6.1.92
- do not package .la files.

* Mon Sep 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1.90-alt2
- mjpegtools-devel requires mjpegtools-static-libs (fix #3024).

* Mon Aug 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1.90-alt1
- 1.6.1.90

* Sun Nov 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt3
- Rebuilt with new libdirectfb.

* Sun Sep 08 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt2
- rebuild with new libdv (0.98), XFree86. 
- gcc-3.2 used.
- buildrequires updated.

* Sat May 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt1
- 1.6.0 release. 

* Fri May 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt0.5rc2
- First build for Sisyphus.
