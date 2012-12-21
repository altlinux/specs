Name: libfreetype
Version: 2.4.11
Release: alt1

Summary: A free and portable font rendering engine
License: FTL or GPLv2+
Group: System/Libraries
Url: http://www.freetype.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: http://download.savannah.gnu.org/releases/freetype/freetype-%version.tar.bz2
Source2: http://download.savannah.gnu.org/releases/freetype/freetype-doc-%version.tar.bz2
Source1: http://download.savannah.gnu.org/releases/freetype/ft2demos-%version.tar.bz2

Patch5: freetype-2.4.10-osh.patch

Patch1: freetype-2.4.10-alt-compat-version-script.patch
Patch2: freetype-2.4.10-alt-freetype-config.patch
Patch3: freetype-2.4.10-alt-fttrigon.patch
Patch4: ft2demos-2.4.10-alt-drop-ftgrid.patch

Patch11: freetype-2.4.10-rh-enable-subpixel-rendering.patch
Patch12: freetype-2.4.10-rh-enable-valid.patch
Patch13: ft2demos-2.4.10-rh-more-demos.patch

Patch21: ft2demos-2.4.10-deb-fixes.patch

Provides: freetype2 = %version
Obsoletes: freetype2 < %version

%def_disable static

BuildRequires: libX11-devel zlib-devel

%description
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments.  FreeType is a library which can open
and manages font files as well as efficiently load, hint and render
individual glyphs.  FreeType is not a font server or a complete
text-rendering library.

%package devel
Summary: Header files and library for development with FreeType2
Group: Development/C
Requires: %name = %version-%release
Provides: freetype2-devel = %version
Obsoletes: freetype2-devel < %version

%description devel
This package contains the header files and development libraries needed
to develop programs that use the FreeType2 library.

%package devel-static
Summary: The FreeType2 static library
Group: Development/C
Requires: %name-devel = %version-%release
Provides: freetype2-devel-static = %version
Obsoletes: freetype2-devel-static < %version

%description devel-static
This package contains the FreeType2 static library.

%package demos
Summary: A collection of FreeType demonstration programs
Group: Development/C
Requires: %name = %version-%release
Provides: freetype2-demos = %version
Obsoletes: freetype2-demos < %version
Conflicts: freetype

%description demos
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments.  FreeType is a library which can open
and manages font files as well as efficiently load, hint and render
individual glyphs.  FreeType is not a font server or a complete
text-rendering library.

This package contains collection of FreeType demonstration programs.

%prep
%setup -n freetype-%version -a1 -b2
ln -s ft2demos-%version ft2demos

%patch5 -p1

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

%patch11 -p1
%patch12 -p1
%patch13 -p0

%patch21 -p0

%build
%add_optflags -fno-strict-aliasing
%configure %{subst_enable static}

# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' builds/unix/libtool

%make_build
%make_build -C ft2demos-%version TOP_DIR=..

%install
%makeinstall_std

for f in ft2demos-%version/bin/ft*; do
	builds/unix/libtool --mode=install install -m755 $f %buildroot%_bindir/
done

wordsize=$(echo -e '#include <bits/wordsize.h>\n__WORDSIZE' | cpp -P | sed '/^$/d')
[ "$wordsize" -ge 32 ]
mv %buildroot%_includedir/freetype2/freetype/config/ftconfig{,-$wordsize}.h
cat >%buildroot%_includedir/freetype2/freetype/config/ftconfig.h << EOF
#ifndef __FTCONFIG_H__MULTILIB
#define __FTCONFIG_H__MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include <freetype/config/ftconfig-32.h>
#elif __WORDSIZE == 64
# include <freetype/config/ftconfig-64.h>
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

%define docdir %_docdir/%name-%version
%define develdocdir %_docdir/%name-devel-%version
mkdir -p %buildroot%docdir
mkdir -p %buildroot%develdocdir
cp -a docs/* %buildroot%develdocdir/
pushd %buildroot%develdocdir
	bzip2 -9 CHANGES raster.txt
	rm INSTALL* release
popd
mv %buildroot%develdocdir/{FTL.TXT,LICENSE.TXT,CHANGES.bz2} %buildroot%docdir/

%set_verify_elf_method strict

%files
%docdir
%_libdir/*.so.*

%files devel
%develdocdir
%_bindir/*-config
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_datadir/aclocal/*.m4

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files demos
%_bindir/ft*

%changelog
* Fri Dec 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.4.11-alt1
- 2.4.11

* Mon Oct 08 2012 Dmitry V. Levin <ldv@altlinux.org> 2.4.10-alt2
- Fixed freetype-config script to use pkg-config (closes: #27761).
- Fixed multilib issues.
- Fixed fttrigon.h
- Packaged more demos.
- Applied demos fixes from Debian.
- Dropped rh-bitmap-foundry.patch.
- Rediffed patches, cleaned up specfile.
- Disabled build and packaging of static library.

* Wed Jul 18 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Sun Apr 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.4.9-alt1
- 2.4.9

* Sat Dec 10 2011 Dmitry V. Levin <ldv@altlinux.org> 2.4.8-alt2
- Fixed RPATH issue (closes: #26693).

* Wed Nov 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Sun Oct 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.7-alt1
- 2.4.7

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Sun Jun 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt4
- disabled dependency on zlib-devel

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt3
- added ld script to mitigate symbol versioning issues

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2.4.4-alt2
- rebuilt for debuginfo
- disabled symbol versioning

* Wed Dec 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.4-alt1
- added some upstream patches

* Mon Oct 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.3-alt2
- added some upstream patches

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Thu Aug 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Sat Aug 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt2
- fixed CVE-2010-2805, CVE-2010-2806, CVE-2010-2807, CVE-2010-2808

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.3.12-alt1
- 2.3.12

* Sat Oct 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.11-alt2
- fixed pcf font names (closes: #21972)

* Sun Oct 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.11-alt1
- 2.3.11 (closes: #21909)

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.10-alt1
- 2.3.10

* Wed Apr 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.9-alt2
- fixed CVE-2009-0946

* Mon Mar 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.9-alt1
- 2.3.9

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3.8-alt1
- 2.3.8

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.7-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jul 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Wed Jun 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Feb 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.3.5-alt2.1
- don't use logical OR to concatenate error codes

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.5-alt2
- fixed version script

* Sat Jul 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Fri May 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.4-alt2
- fixed CVE-2007-2754

* Tue Apr 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Fri Apr 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.3-alt2
- added freetype-2.3.3-cvs-ftbitmap.patch: fix buffer-overwrite bug

* Thu Apr 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.3-alt1
- 2.3.3:
  + fixed CVE-2007-1351

* Wed Mar 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.2-alt2
- added freetype-2.3.2-cvs-bdflib.patch: fixed potential buffer overflow in dbflib

* Sat Mar 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Jan 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.1-alt1
- 2.3.1
- drop upstream patches

* Tue Jan 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt3
- returned freetype-2.2.1-memcpy-fix.patch
- added freetype-2.3.0-cvs-limit-check.patch,
	freetype-2.3.0-cvs-SHZ.patch

* Thu Jan 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt2
- enable subpixel rendering

* Wed Jan 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.3.0-alt1
- 2.3.0
- introduced FREETYPE_2.3.0 ABI for new functions in libfreetype.so.6

* Sat Jan 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt9
- fixed %%docdir
- install documentations
- drop 	freetype-2.2.1-suse-bugzilla-159166-reduce-embolden-distance.patch
- merge patches from RH:
  + freetype-2.2.1-enable-valid.patch
  + freetype-composite.patch
  + freetype-more-composite.patch

* Wed Dec 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt8
- fixed error code on rendering a space character (#10414)

* Tue Dec 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt7
- merge patches from RH:
  + freetype-2.2.1-ttcmap.patch
  + freetype-2.2.1-memcpy-fix.patch

* Fri Jul 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt6
- merge patches from SuSE

* Sat Jul 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt5
- removed freetype2-bitmap-foundry.patch

* Wed Jun 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt4
- updated freetype-2.2.1-cvs-memleak.patch

* Wed May 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt3
- fixed #9647, #9648

* Sun May 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt2
- added freetype-2.2.1-cvs-memleak.patch

* Thu May 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt1
- 2.2.1
- added freetype-2.2.1-cvs-perfloadgluph.patch

* Mon Apr 24 2006 Alexey Tourbin <at@altlinux.ru> 2.1.10-alt4
- NMU: introduced FREETYPE_2.1.10 ABI for new functions in libfreetype.so.6;
  also restricted the list of symbols exported by the library

* Sun Apr 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt3
- merge patches from SuSE

* Fri Mar 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt2
- renamed to libfreetype
- fixed #8923, #8869
- updated build dependencies

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.10-alt1.1
- Rebuilt for new pkg-config dependencies.

* Wed Nov 09 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt1
- merge patches from RedHat

* Mon Oct 03 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.10-alt0.1
- 2.1.10

* Wed Jun 22 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt4
- merge patches from SuSE

* Fri Mar 18 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt3
- enable static

* Wed Oct 27 2004 Dmitry V. Levin <ldv@altlinux.org> 2.1.9-alt2
- Fixed build dependencies.
- Packaged translations.
- Build ft2demos.
- Moved documentation for developers to -devel subpackage.

* Wed Oct 20 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.1.9-alt1
- Updated to 2.1.9.

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 2.1.4-alt3
- Fix crash with non-format-0 hdmx tables (RH).
- Do not build static library by default.
- Do not package .la files.
- Specfile cleanup.

* Tue Jun 03 2003 AEN <aen@altlinux.ru> 2.1.4-alt2
- some internal headers added for pfaedit

* Sat Apr 12 2003 AEN <aen@altlinux.ru> 2.1.4-alt1
- new version
- patches 1,2 obsoletes now

* Tue Mar 11 2003 AEN <aen@altlinux.ru> 2.1.3-alt2
- enable bytecode interpreter

* Fri Feb 28 2003 AEN <aen@altlinux.ru> 2.1.3-alt1
- new verson
- patches from RH

* Mon Sep 02 2002 AEN <aen@altlinux.ru> 2.1.2-alt2
- patches from Rawhide (2.1.2-9) for hinting quality added

* Wed Jun 26 2002 AEN <aen@logic.ru> 2.1.2-alt1
- new version

* Tue Jun 17 2002 AEN <aen@logic.ru> 2.1.1-alt1
- new version
- patch regenerated

* Thu Mar 28 2002 AEN <aen@logic.ru> 2.0.9-alt1
- new version

* Fri Jan 18 2002 AEN <aen@logic.ru> 2.0.6-alt1
- new version

* Mon Oct 29 2001 AEN <aen@logic.ru> 2.0.5-alt1
- new version

* Wed Jul 4 2001 AEN <aen@logic.ru> 2.0.4-alt1
- new version

* Thu Jun 21 2001 AEN <aen@logic.ru> 2.0.3-alt3
- ttf hinting enabled

* Mon Jun 18 2001 AEN <aen@logic.ru> 2.0.3-alt2
- requirements fixed (thnx to Aleksey Voinov)

* Thu May 31 2001 AEN <aen@logic.ru> 2.0.3-alt1
- 2.0.3

* Wed Apr 4 2001 AEN <aen@logic.ru> 2.0.2-ipl1mdk
- 2.0.2 final

* Mon Dec 18 2000 AEN <aen@logic.ru>
- new snapshot for building XFree86-4.0.2

* Mon Nov 28 2000 AEN <aen@logic.ru>
- build for RE

* Tue Nov 21 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-3mdk
- Include all modules in lib (no longer apply patch1)

* Tue Nov 21 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-2mdk
- Add config script to devel package
- correctly configure package

* Fri Nov 10 2000 Geoffrey Lee <snailtalk@manrakesoft.com> 2.0-1mdk
- really 2.0 release.

* Wed Nov  8 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0-0.8.1mdk
- First mandrake release

* Thu Oct  5 2000 Ramiro Estrugo <ramiro@eazel.com>
- Created this thing

