Name: libXfont
Version: 1.5.4
Release: alt1%ubt
Summary: X.Org libXfont runtime library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: bzlib-devel libfontenc-devel libfreetype-devel xorg-fontsproto-devel xmlto
BuildRequires: xorg-xproto-devel xorg-xtrans-devel xorg-util-macros zlib-devel xorg-sgml-doctools

%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font file
formats, and rasterizing them.   It is used by the X servers, the
X Font Server (xfs), and some font utilities (bdftopcf for instance),
but should not be used by normal X11 clients.  X11 clients access fonts
via either the new API's in libXft, or the legacy API's in libX11.

%package devel
Summary: X.Org libXfont development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the libXfont development library and header files

%def_enable ipv6

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-bzip2 \
	%{subst_enable ipv6} \
	--disable-devel-docs \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d

%files
%dir %_sysconfdir/X11/fontpath.d
%_libdir/*.so.*

%files devel
%_includedir/X11/fonts
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Dec 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.4-alt1%ubt
- fixes:
 + CVE-2017-16611 Open files with O_NOFOLLOW

* Fri Oct 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.5.3-alt1
- 1.5.3

* Mon Mar 23 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Fri Sep 05 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Fri May 16 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.4.8-alt1
- 1.4.8

* Wed Jan 08 2014 Valery Inozemtsev <shrek@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Tue Jul 30 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Tue Mar 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Thu Aug 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Thu Jun 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt4
- enabled ipv6

* Wed Apr 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt3
- updated build dependencies

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt2
- devel: fixed pkg-config requires

* Fri Oct 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Wed Jun 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Wed Feb 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sat Dec 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Fri Dec 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3-alt4
- added support for bzip2 bitmap font compression

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Sep 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3-alt2
- disabled fontcache

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Sun Jun 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt2
- fixed encodingsdir

* Thu Mar 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Thu Jan 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt2
- fix for CVE-2008-0006 - PCF Font parser buffer overflow

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Fri Aug 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt2
- added %_sysconfdir/X11/fontpath.d

* Tue Aug 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sun Jul 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt2
- added libXfont-1.2.8-alt-ft_isdigit.patch: fixed build

* Sun Jun 24 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Wed Apr 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt2
- fixed CVE-2007-1351, CVE-2007-1352

* Tue Jan 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Thu Jan 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.6-alt2
- libXfont-1.2.6-git-scalable-renderer.patch adds "return BadFont;"
  stubs to prevent the crash.

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.6-alt1
- 1.2.6
- drop libXfont-1.1.0-alt-includes.patch

* Fri Dec 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Sep 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2:
    Fixes for integer overflows in CID encoded fonts parsing
    reported by iDefense CVE-ID 2006-3739, 2006-3740

* Sat Aug 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt3
- CVE-2006-3467

* Thu Jul 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- added libXfont-1.2.0-git-buffer_overflow.patch

* Sat Jul 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Jun 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt3
- fix warning about FreeTypeRasteriseGlyph() return error on glyph
  that has zero height

* Wed May 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2.1
- updated noftinternals patch

* Wed May 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt2
- added noftinternals patch

* Sun Apr 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt4
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt3
- fixed requires for %name-devel

* Fri Jan 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt2
- install fcqueue.h, fontcache.h for build FontCache extensions

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

