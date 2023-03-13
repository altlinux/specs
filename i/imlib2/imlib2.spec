Name: imlib2
Version: 1.11.0
Release: alt1

Summary: Image loading, saving, rendering, and manipulation library
License: Imlib2
Group: System/Libraries
Url: https://git.enlightenment.org/old/legacy-imlib2
# Source-url: https://sourceforge.net/projects/enlightenment/files/imlib2-src/%version/%name-%version.tar.xz
Source: %name-%version.tar

%def_disable static
%def_enable mmx

# Automatically added by buildreq on Sun Sep 16 2012
# optimized out: gnu-config libX11-devel pkg-config xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel libXext-devel libfreetype-devel libgif-devel libjpeg-devel libpng-devel libwebp-devel libtiff-devel libid3tag-devel
BuildRequires: libheif-devel librsvg-devel liblzma-devel libopenjpeg2.0-devel libspectre-devel

%description
Imlib 2 is a library that does image file loading and saving as well as
rendering, manipulation, arbitrary polygon support, etc.  It does ALL of
these operations FAST.  Imlib2 also tries to be highly intelligent about
doing them, so writing naive programs can be done easily, without
sacrificing speed.  This is a complete rewrite over the Imlib 1.x
series.  The architecture is more modular, simple, and flexible.

%package devel
Summary: Imlib2 development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files for Imlib2.

%package devel-static
Summary: Imlib static libraries
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Imlib2 static libraries.

%package utils
Summary: Imlib2 image manipulation and testing utilities.
Group: Graphics
Requires: %name = %version-%release

%description utils
Imlib2 is an advanced replacement library for libraries like libXpm
that provides many more features with much greater flexibility and
speed than standard libraries, including font rasterization, rotation,
RGBA space rendering and blending, dynamic binary filters, scripting,
and more.

This package provides some test programs and utilities from Imlib2
distribution.

%prep
%setup
#sed -i 's/echo \$libdirs -lImlib2 @my_libs@/echo -lImlib2/' imlib2-config.in
sed -i '1a#include <stdbool.h>' \
  src/modules/loaders/loader_gif.c

%build
export LIBS+="-L/%_lib -lm"
%autoreconf
%configure \
	%{subst_enable static} \
%ifarch x86_64
	--enable-amd64 \
%endif
%ifarch %ix86
	%{subst_enable mmx} \
%endif
	--enable-visibility-hiding

%make_build

%install
%makeinstall_std

# remove non-packaged files
find %buildroot%_libdir/ -name '*.la' -delete

%files
%_libdir/*.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/filters/
%dir %_libdir/%name/loaders/
%_libdir/%name/filters/*.so
%_libdir/%name/loaders/*.so

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
# %%doc doc/{*gif,*.html}

%files utils
%_bindir/*
%_datadir/%name/

%if_enabled static
%files devel-static
%_libdir/lib*.a
%_libdir/%name/*/*.a
%endif

%changelog
* Sun Mar 12 2023 Leontiy Volodin <lvol@altlinux.org> 1.11.0-alt1
- New version (1.11.0).

* Tue Dec 20 2022 Leontiy Volodin <lvol@altlinux.org> 1.10.0-alt1
- New version (1.10.0).
- Updated url tag.

* Wed Sep 07 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.1-alt1
- New version (1.9.1).

* Mon Apr 25 2022 Leontiy Volodin <lvol@altlinux.org> 1.9.0-alt1
- New version (1.9.0).

* Mon Mar 21 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.1-alt1
- New version (1.8.1).

* Mon Feb 14 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.0-alt1
- New version (1.8.0).
- Fixed underlinked libraries.

* Fri Dec 10 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.5-alt1
- New version (1.7.5) with rpmgs script.

* Tue Sep 21 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.4-alt1
- New version (1.7.4) with rpmgs script.

* Mon Aug 16 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.3-alt1
- New version (1.7.3) with rpmgs script.

* Wed Jul 28 2021 Leontiy Volodin <lvol@altlinux.org> 1.7.2-alt1
- New version (1.7.2) with rpmgs script.

* Mon Dec 14 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.1-alt1
- New version (1.7.1) with rpmgs script.

* Mon Aug 03 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.0-alt1
- New version (1.7.0) with rpmgs script.

* Tue Dec 17 2019 Leontiy Volodin <lvol@altlinux.org> 1.6.1-alt1
- New version (1.6.1) with rpmgs script.

* Wed Dec 11 2019 Leontiy Volodin <lvol@altlinux.org> 1.6.0-alt1
- New version (1.6.0) with rpmgs script.
- Added BR for native mp3 support.

* Tue Feb 19 2019 Leontiy Volodin <lvol@altlinux.org> 1.5.1-alt1
- Updated to 1.5.1 (ALT #36086).

* Mon Apr 15 2013 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt2
- Fixed "imlib2-config --libs" output.

* Sun Sep 16 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- Updated to 1.4.5.

* Wed Mar 09 2011 Michael Shigorin <mike@altlinux.org> 1.4.4-alt2.qa2
- rebuilt for debuginfo
- minor spec cleanup

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Thu Jul 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt2
- fix filters and loaders packing (ALT bug #23707)

* Thu Jul 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script) (ALT bug #23698)

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for imlib2
  * postun_ldconfig for imlib2
  * postclean-05-filetriggers for spec file

* Fri Nov 21 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.4.0-alt3
- Fix CVE-2008-5187.

* Mon Jun 16 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.4.0-alt2
- Fix CVE-2008-2426.
- Fix CVE-2006-4806 CVE-2006-4807, CVE-2006-4808, CVE-2006-4809.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.4.0-alt1
- 1.4.0 release.

* Tue Jun 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.0-alt3
- Use MMX only on ix86 and x86_64 (by kas@).

* Wed Apr 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.0-alt2
- Fixed #11348.
- Minor spec cleanup (mostly cosmetics)
- Introduced myself as a Packager.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.3.0-alt1
- 1.3.0 release.
- Removed textrel kludge.
- Enabled mmx.
- Fixed BuildRequires.

* Mon Mar 27 2006 Michael Shigorin <mike@altlinux.org> 1.2.1-alt2.1
- NMU: fix build

* Sun Oct 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- NMU: add /usr/lib/imlib2 to files
- fix URL and Source
- update buildreq (remove freetype-devel)

* Thu Jun 30 2005 Anton D. Kachalov <mouse@altlinux.org> 1.2.1-alt1
- 1.2.1
- x86_64 support

* Sat Jan 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Jan 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.2-alt1
- 1.1.2
- fixed multiple integer overflows in xpm loader (CAN-2004-1026)
  (debian patch for imlib2-1.0.5 adopted for this version).

* Mon Aug 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt1
- 1.1.1
- all old patches in mainstream now.
- fixed BMP biClrUsed overflow (thanks Suse).
- new utils subpackage.

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt2
- do not package .la files.
- devel-static subpackage now is optional.

* Wed Nov 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt1
- new version.
- disable mmx by default.
- with enabled mmx support apply
  set_verify_elf_method textrel=relaxed due i can't fix asm code.

* Thu Oct 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt4
- fixed %%build.

* Wed Oct 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.6-alt3
- Fixed "-I/usr/include" compilation warnings.
- Rebuilt with "libintl-free" freetype-devel.
- Updated buildrequires.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt2
- Rebuild with gcc-3.2
- Loaders .la files go in the main package.

* Fri Apr 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt1
- 1.06 

* Tue Apr 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt2
- build process fixed (#839).  
_ buildrequires updated.

* Thu Apr 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt1
- Adopted for Sisyphus PLD Team imlib2-1.0.5-2 package. 
