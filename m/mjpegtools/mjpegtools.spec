%def_enable static
%def_with quicktime

Name: mjpegtools
Version: 1.9.0
Release: alt4

Summary: Tools for recording, editing, playing back mpeg-encoding video under linux
License: GPL
Group: Video
Url: http://mjpeg.sourceforge.net
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: http://prdownloads.sourceforge.net/mjpeg/%name-%version.tar.gz
Patch4: 0003-Fix-path-to-transcode.patch
Patch5: 0001-Fix-build-with-new-gcc.patch

%define quicktime_ver 0.9.7
%define libdv_ver 0.9

Requires: libquicktime >= %quicktime_ver
Requires: lib%name = %version-%release 
Requires: libdv >= %libdv_ver

BuildPreReq: libquicktime-devel >= %quicktime_ver
BuildPreReq: libdv >= %libdv_ver

BuildRequires: glibc-kernheaders libjpeg-devel libSDL_gfx-devel gcc-c++
BuildRequires: libpng-devel libXxf86dga-devel libgtk+2-devel libSDL-devel
BuildRequires: libXt-devel

#BuildRequires: libICE-devel libSDL-devel libSM-devel libX11-devel libXext-devel libXt-devel libXxf86dga-devel libatk-devel libcairo-devel libdv-devel libgtk+2-devel libpango-devel libpng-devel libquicktime-devel libstdc++-devel pkg-config xorg-cf-files xorg-x11-proto-devel zlib-devel libjpeg-mmx-devel
   
%description
The MJPEG-tools are a basic set of utilities for recording, editing,
playing back and encoding (to mpeg) video under linux. Recording can
be done with zoran-based MJPEG-boards (LML33, Iomega Buz, Pinnacle
DC10(+), Marvel G200/G400), these can also playback video using the
hardware. With the rest of the tools, this video can be edited and
encoded into mpeg1/2 or divx video.

%ifarch %ix86
NOTE:
The resultant binaries will ***NOT*** run on a K6 or Pentium CPU
%endif

%package -n lib%name
Summary: Shared libraries for the mjpegtools
Group: System/Libraries
Obsoletes: %name-libs
Provides: %name-libs = %version-%release

%description -n lib%name
This package contains shared libraries needed to run mjpegtools.

%ifarch %ix86
NOTE:
This binaries does ***NOT*** compatible with a K6 or Pentium CPU
%endif

%package -n lib%name-devel
Summary: Development headers and libraries for the mjpegtools
Group: Development/C
Obsoletes: %name-devel
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

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
This binaries does ***NOT*** compatible with a K6 or Pentium CPU
%endif

#set_verify_elf_method textrel=relaxed

%prep
%setup -q
%patch4 -p2
%patch5 -p2

%build
%configure \
	%{subst_enable static} \
	%{subst_with quicktime} \
	--enable-large-file \
%ifarch %ix86
	--enable-simd-accel
%endif

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
# SMP-incompatible build
%make

%install
%makeinstall

# remove non-packaged files
rm -f %buildroot%_infodir/dir

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS BUGS CHANGES HINTS PLANS README TODO

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%_man5dir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
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
