# NB: we track "superstable" upstream releases, see Url:

Name: netpbm
Version: 10.35.82
Release: alt1

Summary: Tools for manipulating graphics files in netpbm supported formats
License: BSD-like
Group: Graphics

Packager: Vladimir Lettiev <crux@altlinux.ru>

URL: http://netpbm.sourceforge.net

# https://netpbm.svn.sourceforge.net/svnroot/netpbm/stable
Source0: netpbm-%version.tar
# https://netpbm.svn.sourceforge.net/svnroot/netpbm/userguide
Source1: netpbm-userguide.tar

# fix various build and install issues
Patch0: netpbm-10.34-alt-libpm-tmp.patch
Patch1: netpbm-10.34-alt-no-nstring.patch
Patch2: netpbm-10.35-alt-cameratopam-memmem.patch
Patch3: netpbm-10.35-alt-fix-overflow-destination-buffer.patch
Patch4: netpbm-10.35-alt-fix-userguide-name.patch

# security patches
Patch5: netpbm-10.34-rh-security-overflows.patch
Patch6: netpbm-10.29-rh-CAN-2005-2471.patch

# libjbig >= 2.0
Patch10: netpbm-10.35-alt-libjbig2.patch

# use mktemp(1) in shell scripts
Patch20: netpbm-10.29-alt-anytopnm-tmp.patch
Patch21: netpbm-10.29-alt-ppmquantall-tmp.patch
Patch22: netpbm-10.29-alt-pnmmargin-tmp.patch
Patch23: netpbm-10.29-alt-pamstretchgen-tmp.patch
Patch24: netpbm-10.29-alt-pnmindex-tmp.patch

# use File::Temp in perl scripts
Patch30: netpbm-10.29-alt-pnmquant-tmp.patch
Patch31: netpbm-10.29-alt-ppmshadow-tmp.patch
Patch32: netpbm-10.33-alt-ppmrainbow-tmp.patch
Patch33: netpbm-10.27-alt-ppmfade-tmp.patch

# more RedHat patches
Patch50: netpbm-10.32-rh-giftopnm-verbose-message.patch
Patch51: netpbm-10.35-rh-alt-bmptopnm.patch
Patch52: netpbm-10.30-rh-gcc4.patch
Patch53: netpbm-10.35-rh-ppmtompeg.patch
Patch54: netpbm-10.35-rh-xwdtopnm-x86_64.patch
Patch55: netpbm-10.34-rh-pamscale.patch
Patch56: netpbm-10.35-rh-pnmtofiascoleaks.patch
Patch57: netpbm-10.35-rh-docfix.patch
Patch58: netpbm-10.35-rh-glibc.patch
Patch59: netpbm-10.17-rh-time.patch
Patch60: netpbm-10.35-rh-ximtoppmsegfault.patch
Patch61: netpbm-10.35-rh-rgbtxt.patch
Patch62: netpbm-10.35-rh-pnmmontagefix.patch
Patch63: netpbm-10.35-rh-64bitfix.patch
Patch64: netpbm-9.24-rh-strip.patch
Patch65: netpbm-10.35-rh-svgtopam.patch
Patch66: netpbm-10.33-rh-multilib.patch

Requires: lib%name = %version-%release

# for manual pages
BuildPreReq: %_bindir/html2pod

# Automatically added by buildreq on Sat Nov 10 2007
BuildRequires: flex libjasper-devel libjbig-devel >= 2.0 libjpeg-devel libpng-devel libtiff-devel libxml2-devel perl-podlators

%package doc
Summary: Tools for manipulating graphics files in netpbm supported formats
Group: Documentation

%package -n lib%name
Summary: A library for handling different graphics file formats
Group: System/Libraries
Requires: xorg-x11-rgb

%package -n lib%name-devel
Summary: A library for handling different graphics file formats
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: A library for handling different graphics file formats
Group: Development/C
Requires: lib%name-devel = %version-%release

%description
The netpbm package contains programs for handling various graphics file
formats, including .pbm (portable bitmaps), .pgm (portable graymaps),
.pnm (portable anymaps), .ppm (portable pixmaps) and others.

%description doc
The netpbm package contains programs for handling various graphics file
formats, including .pbm (portable bitmaps), .pgm (portable graymaps),
.pnm (portable anymaps), .ppm (portable pixmaps) and others.

%description -n lib%name
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
%setup -q -a1

# build
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p1

# security
%patch5 -p1
%patch6 -p1

# libjbig >= 2.0
%patch10 -p2

# mktemp
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

# File::Temp
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1

# RedHat
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1

# rename shhopt.h to pbmshhopt.h to avoid namespace conflicts
mv lib/util/{,pbm}shhopt.h
find -type f \( -name '*.[chl]' -o -iname '*makefile*' \) -print0 |
	xargs -r0 grep -FZl shhopt.h -- |
	xargs -r0 subst -p 's/\<shhopt\.h/pbm&/g' --

# rename conflicting functions and variables
sed -i 's/\<getline\>/ppm_&/g' converter/ppm/xpmtoppm.c

# use system jbig library
rm -v converter/other/jbig/{jbig.c,jbig_tab.c,jbig.h}

# use system jasper library
rm -rv converter/other/jpeg2000/libjasper/
sed -i '/^SUBDIRS = libjasper$/d' converter/other/jpeg2000/Makefile

%build
cat <<__EOF__ >lib/compile.h
#define COMPILE_TIME "$(LC_ALL=C date '+%%a %%b %%d %%Y')"
#define COMPILED_BY "%packager, %vendor"
__EOF__

cp -av Makefile.config{.in,}
cat <<__EOF__ >>Makefile.config
#
# ALT
#
CC = gcc
CFLAGS = %optflags -D_GNU_SOURCE
CFLAGS_SHLIB = %optflags_shared
SHLIB_CLIB = -lm
TIFFLIB = libtiff.so
JPEGLIB = libjpeg.so
PNGLIB = libpng.so
ZLIB = libz.so
JBIGLIB = %_libdir/libjbig.so
JASPERHDR_DIR = %_includedir/jasper
JASPERLIB = %_libdir/libjasper.so
STRIPFLAG =
pkgdir = %buildroot%_prefix
__EOF__

# SMP incompatible
make

%install
%make_install install.bin install.data install.hdr
mkdir -p %buildroot%_libdir %buildroot%_datadir
cp -av lib/lib%name.a lib/lib%name.so* %buildroot%_libdir
mv %buildroot%_prefix/misc %buildroot%_datadir/%name
rm -fv %buildroot%_bindir/manweb

# install netpbm-config
sed	-e '/^@/d'				\
	-e 's|@VERSION@|%version|'		\
	-e 's|@DATADIR@|%_datadir/%name|'	\
	-e 's|@LINKDIR@|%_libdir|'		\
	-e 's|@INCLUDEDIR@|%_includedir|'	\
	-e 's|@BINDIR@|%_bindir|'		\
		buildtools/config_template >%buildroot%_bindir/netpbm-config
egrep '@[A-Z]+@' %buildroot%_bindir/netpbm-config && exit 1
chmod +x %buildroot%_bindir/netpbm-config
test "$(%buildroot%_bindir/netpbm-config --datadir)" = %_datadir/%name

mkman()
{
	local section="$1" name="$2"
	local html="userguide/$name.html"
	if [ ! -f "$html" ]
	then
		echo "warning: HTML doc for $name not available" >&2
		return 0
	fi
	perl -ne 's/>GENERAL</>DESCRIPTION</g;				#\
		s{<a name=[^>]*>(.+?)</a>}{$1}gi;			#\
		s{<\?makeman\s+\.\S+\s*(.+?)\s*\?>}{<H1>$1</H1>}g;	#\
		s{<\?makeman\s+(.+?)\s*\?>}{<p>$1</p>}g && s/\\//g;	#\
		s{<[hH][12][^>]*>([A-Z ]+)</[hH][12]>}{<H1>$1</H1>}g;	#\
		$in = 1 if /^<[hH][12][^>]*>(NAME|SYNOPSIS)/;		#\
		last if /^<hr\b|table of contents/i and $in;		#\
		print "<p>" and next if /<p>This program is part of/i;	#\
		print if $in;' "$html" >"pod/$name.html"
	if [ ! -s "pod/$name.html" ]; then
		echo "warning: HTML doc for $name not convertable" >&2
		return 0
	fi
	html2pod "pod/$name.html" >"pod/$name.pod"
	grep -qs '^=head1 NAME' "pod/$name.pod"
	touch -r "$html" "pod/$name.pod"
	pod2man --name="$name" --center=Graphics --release="%name %version" \
		--section="$section" "pod/$name.pod" >"man/$name.$section"
}

mkdir -p pod man %buildroot{%_man1dir,%_man3dir,%_man5dir}
mkman 1 index; mv man/index.1 man/%name.1
subst 's/index 1/%name 1/g' man/%name.1
for f in %buildroot%_bindir/*; do mkman 1 "${f##*/}"; done
for f in libnetpbm libnetpbm_image libnetpbm_ug libpm \
	libpbm libpgm libpnm libppm; do mkman 3 "$f"; done
for f in pam pbm pgm pnm ppm; do mkman 5 "$f"; done
install -p -m644 man/*.1 %buildroot%_man1dir
install -p -m644 man/*.3 %buildroot%_man3dir
install -p -m644 man/*.5 %buildroot%_man5dir

%define pkgdocdir %_docdir/%name-%version
mkdir -p %buildroot%pkgdocdir
cp -a doc/{HISTORY,COPYRIGHT.PATENT,copyright_summary,Netpbm.programming} \
	README %buildroot%pkgdocdir
cp -a userguide %buildroot%pkgdocdir/html

%files -n lib%name
%_libdir/lib%name.so.?*
%dir %pkgdocdir
%pkgdocdir/copyright_summary
%pkgdocdir/COPYRIGHT.PATENT
%pkgdocdir/README

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/*.h
%_man3dir/*.*
%dir %pkgdocdir
%pkgdocdir/Netpbm.programming

%files
%_bindir/*
%_man1dir/*.*
%_man5dir/*.*
%_datadir/%name/
%dir %pkgdocdir
%pkgdocdir/HISTORY

%files doc
%dir %pkgdocdir
%pkgdocdir/html/

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
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
