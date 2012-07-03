%def_disable static
%def_enable pixman

Name: evas
Version: 1.2.1
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif
Serial: 1

Summary: Multi-platform Canvas Library
License: BSD
Group: System/Libraries
URL: http://www.enlightenment.org

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildPreReq: libedb-devel >= 1.0.5.007-alt1.20070731
BuildPreReq: libeet-devel >= 1.6.0 libeina-devel >= 1.2.0
BuildRequires: fontconfig-devel libX11-devel libXrender-devel libXext-devel libICE-devel libGL-devel
BuildRequires: libungif-devel libpng-devel libjpeg-devel librsvg-devel
BuildRequires: libtiff-devel libcairo-devel libSDL-devel doxygen
%{?_enable_pixman:BuildRequires: libpixman-devel}

%description
Evas is a clean display canvas API for several target display systems that
can draw anti-aliased text, smooth super and sub-sampled scaled images,
alpha-blend objects much and more.

%package -n lib%name
Summary: Enlightened Canvas Library
Group: System/Libraries

%description -n lib%name
Evas is a clean display canvas API for several target display systems that
can draw anti-aliased text, smooth super and sub-sampled scaled images,
alpha-blend objects much and more.

%package -n lib%name-devel
Summary: Enlightened Canvas Library development files
Group: Development/C
Requires: lib%name = %serial:%version-%release

%description -n lib%name-devel
Enlightened Canvas Library headers and development libraries.

%package -n lib%name-devel-static
Summary: Static version of Enlightened Canvas Library
Group: Development/C
Requires: lib%name-devel = %serial:%version-%release

%description -n lib%name-devel-static
This package contains library needed to build applications statically
linked with Enlightened Canvas Library.

%package -n lib%name-doc
Summary: Enlightened Canvas Library development documentation
Group: Books/Computer books
Conflicts: lib%name < %serial:%version-%release
BuildArch: noarch

%description -n lib%name-doc
This package contains Enlightened Canvas Library development
documentation

%define customdocdir %_docdir/lib%name-%version

%prep
%ifdef cvs_date
%setup -q -n %name
%else
%setup -q -n %name-%version
%endif

%build
%autoreconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
	--enable-image-loader-gif \
	--enable-image-loader-png \
	--enable-image-loader-jpeg \
	--enable-image-loader-xpm \
	--enable-image-loader-svg \
	--enable-image-loader-eet \
	--enable-image-loader-edb \
	--enable-pthreads \
%ifarch %ix86 x86_64
	--enable-cpu-mmx \
	--enable-cpu-sse \
%endif
	--enable-cpu-c \
	--enable-scale-smooth \
	--enable-scale-sample \
	--enable-convert-8-rgb-332 \
	--enable-convert-8-rgb-666 \
	--enable-convert-8-rgb-232 \
	--enable-convert-8-rgb-222 \
	--enable-convert-8-rgb-221 \
	--enable-convert-8-rgb-121 \
	--enable-convert-8-rgb-111 \
	--enable-convert-16-rgb-565 \
	--enable-convert-16-rgb-555 \
	--enable-convert-16-rgb-rot-0 \
	--enable-convert-16-rgb-rot-90 \
	--enable-convert-16-rgb-rot-270 \
	--enable-convert-32-rgb-8888 \
	--enable-convert-32-rgbx-8888 \
	--enable-convert-32-bgr-8888 \
	--enable-convert-32-bgrx-8888 \
	--enable-convert-32-rgb-rot-0 \
	--enable-convert-32-rgb-rot-90 \
	--enable-convert-32-rgb-rot-270 \
	%{subst_enable pixman} \
	%{subst_enable static}

	#--enable-gl-glew \
	#--enable-gl-sdl \
	#--enable-gl-xlib \

%make_build

%install
%makeinstall

rm -rf %buildroot%_datadir/%name/doc
mkdir -p %buildroot%customdocdir
cp -R doc %buildroot%customdocdir

%files -n lib%name
%_bindir/evas_cserve
%_bindir/evas_cserve_tool
%_libdir/*.so.*
%_libdir/evas

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name-doc
%customdocdir

%exclude %_datadir/evas/examples/evas-buffer-simple.c

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.1-alt1
- 1.2.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.0-alt1
- 1.2.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.1-alt1
- 1.0.1

* Tue Apr 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt6
- updated buildreqs

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt5
- rebuilt for debuginfo

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jun 07 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.49539-alt1
- 0.9.9.49539

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.063-alt1
- 0.9.9.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.062-alt1
- 0.9.9.062

* Tue Jun 23 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.050-alt4
- rebuild

* Tue Apr 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.050-alt3
- removed useless libsvg-cairo-devel from buildreqs

* Thu Feb 19 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.050-alt2
- removed obsolete %%post{,un}_ldconfig
- don't build assembler if not x86* (sbolshakov@)

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.050-alt1
- 0.9.9.050

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.041-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.041-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.040-alt1.20070731
- CVS from 20070731.
- Stricted eet build-requires version.
- Stricted edb build-requires version.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.038-alt1.20070509
- CVS from 20070509.
- Fixed building.
- Fixed BuildRequires.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 1:0.9.9.032-alt1.20060920
- 20060910 -> 20060920
- fix build for x86_64

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 1:0.9.9.032-alt1.20060910
- update from cvs (0.9.9.026 20060412 -> 0.9.9.032 20060910)
- buildreq

* Thu Apr 13 2006 Igor Zubkov <icesik@altlinux.ru> 1:0.9.9.026-alt1.20060412
- updated from cvs

* Mon Apr 03 2006 Igor Zubkov <icesik@altlinux.ru> 1:0.9.9-alt0.1_003_20060327
- updated from cvs

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050530
- updated from cvs.

* Tue May 24 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050524
- updated from cvs.
- bug #6929 fixed.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050516
- updated from cvs.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050428
- updated from cvs.
- minor spec fixes.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050421
- updated from cvs

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 1:0.9.9-alt0.1_003_20050329
- updated from cvs.
- added serial due to version downgrade
- removed INSTALL, TODO from doc
- added touch README

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre13_20050122
- updated from cvs.

* Tue Dec 28 2004 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre13_20041228
- updated from cvs.

* Fri Dec 17 2004 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre13_20041216
- updated from cvs.

* Sun Oct 24 2004 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre13_20041022
- updated from cvs.
- spec cleaning
- don't build libevas-devel-static by default

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_20030613
- Updated from cvs.

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_20030315
- Updated from cvs.
- Change configure
- Removed aclocal
- Changed arial font to n019003l.ttf (val-ttf) in source

* Fri Nov 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- First build for Sisyphus.
