Name: libggi
Version: 2.2.2
Release: alt3.1
Packager: Fr. Br. George <george@altlinux.ru>
%define gii_ver 1.0.2

BuildPreReq: libgii >= %gii_ver

Summary:  A fast, simple, small and flexible user-space graphics library (General Graphics Interface)

License:	GPL
Group: System/Libraries
URL: http://www.ggi-project.org/
Source:		http://www.ggi-project.org/ftp/ggi/v2.2/%name-%version.src.tar.bz2

Patch0: libggi-2.0.1-no-lcd823-ppc.patch
Patch1:	libggi-2.1.0-gcc4.patch
Patch2:	libggi-2.1.0-libtool.patch
Patch3:	libggi-2.0.3-xpath.patch
Patch4:	libggi-2.1.0-lib64.patch
Patch5:	libggi-2.1.1-glibc2.4-fix.patch

# Automatically added by buildreq on Fri Aug 20 2010
BuildRequires: aalib-devel imake libICE-devel libXext-devel libXt-devel libXxf86dga-devel libXxf86vm-devel libgii-devel libncurses-devel xorg-cf-files

%description
LibGGI is a fast, simple, small and flexible user-space graphics
library developed by the GGI Project <http://www.ggi-project.org/>.
It attempts to abstract the many different graphics output systems
existing under Unix (and in the future, other platforms). The support
for all of these different types of displays and hardware are provided
by dynamically-loaded mini-libraries.

LibGGI can transparently (to the LibGGI-using application) display
graphics on an X window, fbcon (Linux framebuffer driver), or the 
glide library, through their respective graphics drivers, or targets. 
There are also some other targets which display through another 
target, such as multi to display simultaneously on multiple displays 
at once, and tile to tile your display to different monitors.

LibGGI supports acceleration of graphics primitives where possible.

LibGGI is a very generic piece of software, that will run on about
every platform that has remotely heard of POSIX (ports to other systems
such as Win32 are underway) and on many display subsystems.

%package devel
Summary: development part of %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgii-devel >= %gii_ver

%description devel
development files for %name

%package devel-static
Summary: development part of %name, static build
Group: Development/C
Requires: %name = %version-%release
Requires: libgii-devel >= %gii_ver

%description devel-static
development files for %name, static build

%package -n ggi-utils
Group: Graphics
Summary: some usefull utils from %name
Provides: %name-utils = %version
Obsoletes: %name-utils

%description -n ggi-utils
some usefull utils from %name

%prep
%setup -q
#add_optflags -I/usr/include/directfb-internal
%patch0 -p1 -b .ppc
#%patch1 -p1 -b .gcc4
#%patch2 -p1 -b .libtool
%patch3 -p1 -b .xpath
#%patch4 -p1 -b .lib64
#%patch5 -p1 -b .glibc2.4
# regenerate configure script
#./autogen.sh
#cat m4/[^l]*.m4 > acinclude.m4
#sed -i 's@PROG_RANLIB@PROG_LIBTOOL@
#/^LT_/d' configure.in

%build
#autoreconf -fisv
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall

%files
%doc FAQ NEWS README doc/env.txt doc/targets.txt
%config(noreplace) %_sysconfdir/ggi/*.conf
%config(noreplace) %_sysconfdir/ggi/targets/*.conf
%_libdir/*.so.*
%_libdir/ggi/default/*.so
%_libdir/ggi/display/*.so
%_libdir/ggi/helper/*.so
%_libdir/ggi/default/fbdev/*.so
%_mandir/man?/*

%files devel
%_includedir/*
%_libdir/*.so

%files devel-static
%_libdir/*.a
#_libdir/ggi/*/*.a
#_libdir/ggi/*/*/*.a

%files -n ggi-utils
%_bindir/*

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt3.1
- Removed bad RPATH

* Fri Aug 20 2010 Fr. Br. George <george@altlinux.ru> 2.2.2-alt3
- Resurrect build

* Sun Jan 11 2009 Fr. Br. George <george@altlinux.ru> 2.2.2-alt2
- Some libtool hacks, thanks ldv@

* Sun Jan 11 2009 Fr. Br. George <george@altlinux.ru> 2.2.2-alt1.1
- Rebuild after falling from Sisyphus

* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 2.2.2-alt1
- Fix build
- Fix version mismatch

* Sun Jun 03 2007 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Resurrect from orphaned
- New version

* Fri Dec 09 2005 Kachalov Anton <mouse@altlinux.ru> 1:2.1.1-alt1
- 2.1.1

* Wed Dec 29 2004 Stanislav Ievlev <inger@altlinux.org> 1:2.1.0-alt1
- 2.1.0

* Wed Oct 06 2004 Stanislav Ievlev <inger@altlinux.org> 1:2.0.6-alt1
- 2.0.6

* Thu Jun 24 2004 Stanislav Ievlev <inger@altlinux.org> 1:2.0.4-alt3
- fixed #3864 (added missed helper subdirectory)

* Tue Mar 23 2004 Stanislav Ievlev <inger@altlinux.org> 1:2.0.4-alt2
- rename libgii-utils to gii-utils (#3734)
- added requires on libgii-devel to libggi-devel package (#3658)

* Tue Jan 13 2004 Stanislav Ievlev <inger@altlinux.org> 1:2.0.4-alt1
- 2.0.4

* Wed Dec 17 2003 Stanislav Ievlev <inger@altlinux.org> 1:2.0.3-alt3
- rebuild without .la files

* Tue Sep 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1:2.0.3-alt2
- fix build in hasher

* Wed Apr 23 2003 Stanislav Ievlev <inger@altlinux.ru> 1:2.0.3-alt1
- 2.0.3

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 1:2.0.2-alt4
- fixed ldconfig usage according packaging policy

* Tue Feb 25 2003 Stanislav Ievlev <inger@altlinux.ru> 1:2.0.2-alt3
- 2.0.2
- added hack for broken directfb-headers

* Wed Oct 16 2002 Stanislav Ievlev <inger@altlinux.ru> 1:2.0.1-alt3
- rebuild without svgalib

* Thu Sep 26 2002 Stanislav Ievlev <inger@altlinux.ru> 1:2.0.1-alt2
- rebuild with gcc3

* Mon Sep 17 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon Aug 13 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0-alt1
- 2.0 final
- Added Serial. Wrong numbers was before.

* Thu Aug 09 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0b4-alt2
- Added buildreqs

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0b4-alt1
- beta4

* Wed Jul 04 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0b3-alt1
- Inital release for ALT Linux
