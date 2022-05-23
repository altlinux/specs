Name: netpbm
Version: 10.85.04
Release: alt2

Summary: Tools for manipulating graphics files in netpbm supported formats
License: BSD-like
Group: Graphics

Url: http://netpbm.sourceforge.net

# Source-url: https://github.com/t6/netpbm/archive/v10.85.04.tar.gz
Source: %name-%version.tar

Requires: lib%{name}11 = %EVR

BuildRequires: flex libjasper-devel libjbig-devel >= 2.0
BuildRequires: libjpeg-devel libpng-devel libtiff-devel libxml2-devel libX11-devel

%package -n lib%{name}11
Summary: A library for handling different graphics file formats
Group: System/Libraries
Requires: xorg-x11-rgb
Provides: libnetpbm = %version-%release

%package -n lib%name-devel
Summary: A library for handling different graphics file formats
Group: Development/C
Requires: lib%{name}11 = %EVR

%package -n lib%name-devel-static
Summary: A library for handling different graphics file formats
Group: Development/C
Requires: lib%name-devel = %EVR

%description
The netpbm package contains programs for handling various graphics file
formats, including .pbm (portable bitmaps), .pgm (portable graymaps),
.pnm (portable anymaps), .ppm (portable pixmaps) and others.

%description -n lib%{name}11
This package contains a library of functions which support programs for
handling various graphics file formats, including .pbm (portable bitmaps),
.pgm (portable graymaps), .pnm (portable anymaps), .ppm (portable pixmaps)
and others.

%description -n lib%name-devel
This package contains the header files and programmer's documentation
for developing programs which can handle the various graphics file
formats supported by the netpbm library.

%description -n lib%name-devel-static
This package contains the static library for developing statically linked
programs which can handle the various graphics file formats supported by
the netpbm library.

%prep
%setup
# use system jasper library
rm -rf converter/other/jpeg2000/libjasper/
# use system jbig library
rm -rf converter/other/jbig/libjbig/

# hide nss-utils require (ALT bug 29475)
subst "s| atob| a= atob|" converter/other/anytopnm

# rename conflicting functions and variables
#sed -i 's/\<getline\>/ppm_&/g' converter/ppm/xpmtoppm.c

%build
cat <<__EOF__ >lib/compile.h
#define COMPILE_TIME "The same time"
#define COMPILED_BY "%packager, %vendor"
__EOF__

cp -av config.mk.in config.mk
cat <<__EOF__ >>config.mk
#
# ALT
#
DEFAULT_TARGET = nonmerge
NETPBMLIBTYPE=unixshared
NETPBMLIBSUFFIX=so
#STATICLIB_TOO=N
CFLAGS = %optflags -D_GNU_SOURCE
CFLAGS_SHLIB = %optflags_shared

LDRELOC = ld --reloc
LINKER_CAN_DO_EXPLICIT_LIBRARY=Y
LINKERISCOMPILER = Y

CC = gcc
SHLIB_CLIB = -lm
TIFFLIB = libtiff.so
JPEGLIB = libjpeg.so
ZLIB = libz.so

JBIGHDR_DIR = %_includedir
JBIGLIB = %_libdir/libjbig.so

JASPERHDR_DIR = %_includedir/jasper
JASPERLIB = %_libdir/libjasper.so

STRIPFLAG =
pkgdir = %buildroot%prefix

PNGHDR_DIR = USE_PKG_CONFIG.a
PNGLIB = USE_PKG_CONFIG.a
X11HDR_DIR = USE_PKGCONFIG.a
X11LIB = USE_PKGCONFIG.a
NETPBM_DOCURL = http://netpbm.sourceforge.net/doc/
#WANT_SSE = Y

__EOF__

%make_build

%install
%make_install install.bin install.data install.hdr
mkdir -p %buildroot%_libdir %buildroot%_datadir
%if_enabled static
cp -av lib/lib%name.a %buildroot%_libdir
%endif
cp -av lib/lib%name.so* %buildroot%_libdir

mv %buildroot%prefix/misc %buildroot%_datadir/%name
rm -fv %buildroot%_bindir/manweb

# install netpbm-config
sed	-e '/^@/d'				\
	-e 's|@VERSION@|%version|'		\
	-e 's|@DATADIR@|%_datadir/%name|'	\
	-e 's|@LINKDIR@|%_libdir|'		\
	-e 's|@INCLUDEDIR@|%_includedir/netpbm|'	\
	-e 's|@BINDIR@|%_bindir|'		\
		buildtools/config_template >%buildroot%_bindir/netpbm-config
grep -E '@[A-Z]+@' %buildroot%_bindir/netpbm-config && exit 1
chmod +x %buildroot%_bindir/netpbm-config
test "$(%buildroot%_bindir/netpbm-config --datadir)" = %_datadir/%name

mkdir -p %buildroot%_man1dir
install -p -m644 man/*.1 %buildroot%_man1dir

%files -n lib%{name}11
%_libdir/lib%name.so.11
%_libdir/lib%name.so.11.*
%doc doc/copyright_summary doc/COPYRIGHT.PATENT README

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/netpbm/
%_includedir/netpbm/*.h
#_man3dir/*.*
%doc doc/Netpbm.programming

%files
%_bindir/*
%_man1dir/*.*
#_man5dir/*.*
%_datadir/%name/
%doc doc/HISTORY

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Mon May 23 2022 Fr. Br. George <george@altlinux.ru> 10.85.04-alt2
- Fix egrep warning

* Tue Mar 26 2019 Vitaly Lipatov <lav@altlinux.ru> 10.85.04-alt1
- NMU: build new version 10.85.04 (ALT bug 33079)
- drop doc subpackage and generated from it man3, man5
- hide nss-utils require (ALT bug 29475)

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 10.35.97-alt1.qa1
- NMU: applied repocop patch

* Mon Nov 16 2015 Fr. Br. George <george@altlinux.ru> 10.35.97-alt1
- Autobuild version bump to 10.35.97

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 10.35.96-alt1
- Autobuild version bump to 10.35.96

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 10.35.95-alt1
- Autobuild version bump to 10.35.95

* Mon Sep 29 2014 Fr. Br. George <george@altlinux.ru> 10.35.94-alt1
- Autobuild version bump to 10.35.94
- Fix patches

* Tue Aug 19 2014 Fr. Br. George <george@altlinux.ru> 10.35.93-alt1
- Autobuild version bump to 10.35.93

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 10.35.92-alt1
- Autobuild version bump to 10.35.92

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 10.35.91-alt1
- Autobuild version bump to 10.35.91

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 10.35.90-alt1
- Autobuild version bump to 10.35.90
- Fix documentation for stronger PODlation

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 10.35.89-alt1
- Autobuild version bump to 10.35.89

* Wed Mar 06 2013 Fr. Br. George <george@altlinux.ru> 10.35.88-alt1
- Autobuild version bump to 10.35.88
- Fix build by linking with ancient libpng

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 10.35.82-alt1
- New version 10.35.82

* Tue Jul 12 2011 Vladimir Lettiev <crux@altlinux.ru> 10.35.81-alt1
- New version 10.35.81
- Fixed build with libjbig >= 2.0

* Mon Feb 21 2011 Vladimir Lettiev <crux@altlinux.ru> 10.35.80-alt1
- New version 10.35.80

* Tue Jan 25 2011 Vladimir Lettiev <crux@altlinux.ru> 10.35.79-alt1
- New version 10.35.79

* Sun Dec 12 2010 Vladimir Lettiev <crux@altlinux.ru> 10.35.78-alt1
- New version 10.35.78

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 10.35.77-alt2
- Fixed build: added perl-podlators to buildrequires

* Sun Sep 19 2010 Vladimir Lettiev <crux@altlinux.ru> 10.35.77-alt1
- New version 10.35.77

* Fri Jul 30 2010 Vladimir Lettiev <crux@altlinux.ru> 10.35.76-alt1
- New version 10.35.76

* Sun Mar 28 2010 Vladimir Lettiev <crux@altlinux.ru> 10.35.74-alt1
- New version 10.35.74

* Fri Feb 12 2010 Vladimir Lettiev <crux@altlinux.ru> 10.35.73-alt1
- 10.35.32 -> 10.35.73
  + fixed stack-based buffer overflow (CVE-2009-4274)
- build fixes
  + netpbm-10.35-alt-fix-overflow-destination-buffer.patch
  + netpbm-10.35-alt-fix-userguide-name.patch
- patches merged upstream
  + netpbm-10.33-alt-ppmquantall-syntax.patch
  + netpbm-10.35-rh-pbmtog3-segv.patch
  + netpbm-10.35-rh-pbmtomacp.patch
- sync RedHat patches (10.35.58)
  + netpbm-10.34-rh-security-overflows.patch updated
  + netpbm-10.35-rh-pnmtofiascoleaks.patch (new)
  + netpbm-10.35-rh-docfix.patch (new)
  + netpbm-10.35-rh-glibc.patch (new)
  + netpbm-10.17-rh-time.patch (new)
  + netpbm-10.35-rh-ximtoppmsegfault.patch (new)
  + netpbm-10.35-rh-rgbtxt.patch (new)
  + netpbm-10.35-rh-pnmmontagefix.patch (new)
  + netpbm-10.35-rh-64bitfix.patch (new)
  + netpbm-9.24-rh-strip.patch (new)
  + netpbm-10.35-rh-svgtopam.patch (new)
  + netpbm-10.33-rh-multilib.patch (new)

* Sat Nov 10 2007 Alexey Tourbin <at@altlinux.ru> 10.35.32-alt1
- 10.35.30 -> 10.35.32

* Mon Aug 20 2007 Alexey Tourbin <at@altlinux.ru> 10.35.30-alt1
- 10.33 -> 10.35.30 (from netpbm.svn.sourceforge.net repo)
  + fixes buffer overflow in pamtofits (CVE-2006-3145)
- sync RedHat patches (Jindrich Novy, 10.35-14)
  + pamscale won't waste all system resources by usage of uninitialized
    variables for output image resolution (RH#199871)
  + pbmtog3 won't segfault on 64bit arches (RH#220739)
  + bmptopnm won't crash with "BMPlencolormap: internal error" (RH#224554)
  + fix pbmtomacp buffer overflow (RH#226969)
- jpeg2k converters: build with system jasper library
- libnetpbm: added dependency on xorg-x11-rgb, due to /usr/share/X11/rgb.txt
- netpbm: install /usr/bin/netpbm-config
- netpbm-doc: new package (HTML user guide)

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 10.33-alt1.0
- Automated rebuild.

* Sun May 14 2006 Alexey Tourbin <at@altlinux.ru> 10.33-alt1
- 10.29 -> 10.33
- sync FC netpbm-10.33-2 (Jindrich Novy)
- fixed various minor issues
- spec demacroization (Michael Shigorin)

* Fri Oct 07 2005 Alexey Tourbin <at@altlinux.ru> 10.29-alt2
- rh-pnmtopng-segv.patch: fix segfault in pnmtopng

* Tue Oct 04 2005 Alexey Tourbin <at@altlinux.ru> 10.29-alt1
- 10.27 -> 10.29
- updated patches, synced with Fedora's 10.29-1
- alt-ppmtompeg-tmp.patch merged upstream
- alt-libpm-tmp.patch partially merged upstream
- disabled nstring.o, enabled asprintf() from glibc
- built with -D_GNU_SOURCE, fixed conflicting names
- linked libnetpbm.so against -lm (rh #165980)
- updated docs

* Sat May 14 2005 Alexey Tourbin <at@altlinux.ru> 10.27-alt1
- 10.26.4 -> 10.27
- License: BSD-like, not GPL (see copyright_summary for details)
- fixed insecure temporary files handling in perl and shell scripts
- fixed insecure temporary file creation in ppmtompeg/parallel.c
- refactored pm_tmpfile() and pm_make_tmpfile() in libpm.c
- rh-overflows.patch: re-added checks for possible integer overflows;
  fixed a bug in rh-overflows.patch (filed RedHat bug #157757)
- imported more RedHat patches (in sync with 10.27-2)
- updated docs; improved manual pages

* Sun Mar 06 2005 Alexey Tourbin <at@altlinux.ru> 10.26.4-alt1
- 10.26 -> 10.26.4
- fixed directory layout for x86_64
- updated docs; improved generation of manual pages
- manweb not packaged

* Mon Jan 24 2005 Alexey Tourbin <at@altlinux.ru> 10.26-alt1
- 10.25 -> 10.26
  + alt-sh-syntax.patch merged upstream
  + alt-fix-usage.patch merged upstream
- updated docs

* Fri Oct 22 2004 Alexey Tourbin <at@altlinux.ru> 10.25-alt1
- 10.24 -> 10.25
- updated docs

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 10.24-alt1.1.1
- Rebuilt with libtiff.so.4.

* Tue Sep 07 2004 Alexey Tourbin <at@altlinux.ru> 10.24-alt1.1
- disabled SMP build

* Wed Aug 25 2004 Alexey Tourbin <at@altlinux.ru> 10.24-alt1
- 10.20 -> 10.24
- build with system-wide libjbig
- build real man pages from HTML pages (a copy of netpbm web site)
  by replacing buildtools/makepointerman script (requires html2pod)
- fixed jbigtopnm and pnmtojbig usage output
- dropped printconf stuff

* Thu Mar 25 2004 Alexey Tourbin <at@altlinux.ru> 10.20-alt1
- 9.24 -> 10.20, major revision
- old patches dropped; sh-syntax.patch: fixed missing `fi'
- reworked %%build and %%install; buildtools/ avoided whenever possible
- lib%name-devel-static not packaged by default; librle.a not packaged
- #define COMPILED_BY "%vendor"

* Thu Feb 12 2004 Alexey Tourbin <at@altlinux.ru> 9.24-alt4
- deb-tmp.patch: secure temporary files (CAN-2003-0924)

* Thu Oct 30 2003 Dmitry V. Levin <ldv@altlinux.org> 9.24-alt3
- Specfile cleanup.
- Removed %_bindir/pcdindex (never worked anyway).
- Reenabled standard dependencies calculation method.

* Thu Oct 30 2003 AEN <aen@altlinux.ru> 9.24-alt2
- patch #3 from RH

* Mon Feb 10 2003 AEN <aen@altlinux.ru> 9.24-alt1
- 9.24
- spec changed, thnx to MDK & RH
- security patch (#4)

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 9.10-alt4
- rebuilt with gcc-3.2

* Thu Oct 11 2001 AEN <aen@logic.ru> 9.10-alt3
- rebuilt with libpng.so.3

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 9.10-alt2
- Specfile cleanup (still requires more cleanup).
- Fixed pnmindex script syntax.

* Thu Aug 16 2001 AEN <aen@logic.ru> 9.10-alt1
- first build for Sisyphus
- static package

* Wed Aug 08 2001 Yves Duret <yduret@mandrakesoft.com> 9.10-4mdk
- added a builrequires to zlib-devel (Buchan Milne <bgmilne@cae.co.za>)
- corrected the 4 no-ldconfig-symlink errors (thx titi)

* Fri Jul 27 2001 Frederic Lepied <flepied@mandrakesoft.com> 9.10-3mdk
- added missing obsoletes on libgr1-progs

* Fri Jul 27 2001 Yves Duret <yduret@mandrakesoft.com> 9.10-2mdk
- added patch2 to fix bad include netpbm-shhopt.h
- added provides libgr

* Tue Jul 24 2001 Yves Duret <yduret@mandrakesoft.com> 9.10-1mdk
- first MandrakeSoft package (stolen from d3bi4n and PLD)
    Obsoletes libgr libgr-progs libgr-devel
