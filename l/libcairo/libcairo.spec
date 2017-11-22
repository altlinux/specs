%def_without docs

Name: libcairo
Version: 1.14.10
Release: alt1
Epoch: 1
Summary: Multi-platform 2D graphics library
License: LGPL
Group: System/Libraries
URL: http://cairographics.org/

Source: cairo-%version.tar
Patch: cairo-%version-%release.patch

BuildRequires: fontconfig-devel ghostscript-classic glib2-devel gtk-doc libGL-devel libXrender-devel
BuildRequires: libfreetype-devel libpixman-devel libpng-devel librsvg-devel libudev-devel zlib-devel
BuildRequires: libEGL-devel libGLES-devel libXext-devel

%description
Cairo is a vector graphics library with cross-device output support

%package devel
Summary: Headers for developing programs that will use cairo
Group: Development/C
Requires: %name = %epoch:%version-%release

%description devel
Cairo is a vector graphics library with cross-device output support.
This package contains the headers that programmers will need to develop
applications which will use cairo library.

%package gobject
Summary: GObject bindings for cairo
Group: System/Libraries
Requires: %name = %epoch:%version-%release

%description gobject
This package contains functionality to make cairo graphics library
integrate well with the GObject object system used by GNOME.

%package gobject-devel
Summary: Development files for cairo-gobject
Group: Development/C
Requires: %name-gobject = %epoch:%version-%release
Requires: %name-devel = %epoch:%version-%release

%description gobject-devel
This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo Gobject library.

%package tools
Summary: Development tools for cairo
Group: Development/C

%description tools
This package contains tools for working with the cairo graphics library.
 * cairo-trace: Record cairo library calls for later playback

%prep
%setup -q -n cairo-%version
%patch -p1

> boilerplate/Makefile.am.features
> src/Makefile.am.features
> ChangeLog

%build
%autoreconf
%configure \
	--enable-xlib \
	--disable-xlib-xcb \
	--enable-xcb \
%ifarch %arm
	--disable-gl \
	--enable-glesv2 \
%else
	--enable-gl \
	--disable-glesv2 \
%endif
	--enable-egl \
	--disable-drm \
	--enable-ps \
	--enable-pdf \
	--enable-svg \
	--enable-tee \
	--disable-xml \
%if_with docs
	--enable-gtk-doc \
%endif
	--disable-static \
	--localstatedir=%_var
%make_build
%if_with docs
%make doc
%endif

%install
%make DESTDIR=%buildroot install

#%check
#%make -k test

%files
%doc AUTHORS NEWS README
%_libdir/%name.so.*
%_libdir/%name-script-interpreter.so.*
%_bindir/cairo-sphinx

%files devel
%_includedir/cairo
%exclude %_includedir/cairo/cairo-gobject.h
%_libdir/%name.so
%_libdir/%name-script-interpreter.so
%_pkgconfigdir/*.pc
%exclude %_pkgconfigdir/cairo-gobject.pc
%if_with docs
%_datadir/gtk-doc/html/cairo
%endif

%files gobject
%_libdir/%name-gobject.so.*

%files gobject-devel
%_includedir/cairo/cairo-gobject.h
%_libdir/%name-gobject.so
%_pkgconfigdir/cairo-gobject.pc

%files tools
%_bindir/cairo-trace
%_libdir/cairo

%changelog
* Wed Nov 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.14.10-alt1
- Updated to upstream version 1.14.10.
- Disabled docs generation.
- Fixed localstatedir location.

* Sun Nov 08 2015 Valery Inozemtsev <shrek@altlinux.ru> 1:1.14.4-alt1
- 1.14.4

* Wed Mar 11 2015 Valery Inozemtsev <shrek@altlinux.ru> 1:1.14.2-alt1
- 1.14.2

* Sun Oct 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 1:1.14.0-alt1
- 1.14.0

* Tue Aug 27 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.16-alt1
- 1.12.16

* Tue Apr 16 2013 Fr. Br. George <george@altlinux.ru> 1:1.12.14-alt1.1
- Fix make doc

* Mon Feb 11 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.14-alt1
- 1.12.14

* Fri Feb 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.12-alt1
- 1.12.12

* Thu Jan 17 2013 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.10-alt1
- 1.12.10

* Tue Nov 06 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.8-alt1
- 1.12.8

* Mon Oct 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.4-alt1
- 1.12.4

* Tue Sep 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.2-alt2
- egl: s/EGL_KHR_surfaceless_opengl/EGL_KHR_surfaceless_context/

* Tue May 01 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.2-alt1
- 1.12.2

* Sat Mar 24 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.12.0-alt1
- 1.12.0

* Wed Feb 15 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt9
- enabled egl backend

* Mon Jan 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt8
- enabled gl backend

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.10.2-alt7
- Reintroduced fixes for %name-devel dependencies that were removed
  erroneously in previous release.

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt6
- removed hacks of previous commits
- disabled gl, drm, xml backends (closes: #25609).

* Tue Mar 29 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.10.2-alt5
- Reintroduced fixes for %name-devel dependencies that were lost
  inadvertently in previous release.

* Mon Mar 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt4
- Updated to 1.10.2-14-gb4466bc.
- Enabled tee backend.

* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 1:1.10.2-alt3
- rebuilt for pkgconfig
- cairo-png.pc: disabled dependency on libpng-devel
- cairo-drm.pc: disabled dependency on libudev-devel
- cairo-{pdf,ps,xml}.pc: disabled dependency on zlib-devel

* Sat Feb 12 2011 Alexey Tourbin <at@altlinux.ru> 1:1.10.2-alt2
- rebuit for debuginfo
- disabled symbol versioning

* Wed Dec 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.2-alt1
- 1.10.2

* Sat Dec 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.0-alt5
- updated to 1.10 git.f832ff7

* Wed Nov 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.0-alt4
- updated to 1.10 git.91a6fe6

* Mon Oct 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.0-alt3
- don't require libbfd

* Tue Oct 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.0-alt2
- disabled xlib-xcb backend

* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.10.0-alt1
- 1.10.0

* Sun Aug 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.10-alt3
- real disabled glitz backend

* Sun Aug 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.10-alt2
- disabled glitz backend

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.10-alt1
- 1.8.10

* Mon Dec 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.8-alt4
- fixed build gtk doc
- moved "make test" to %%check section

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.8-alt3
- rebuild with libpng12 1.2.37-alt2

* Wed Jun 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.8-alt2
- fixed missing implicit move-to

* Wed Jun 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.8-alt1
- 1.8.8

* Mon Mar 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.6-alt3
- tests are started without a Xvfb

* Wed Jan 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.6-alt2
- lcd-filter: replaced archlinux patch to ubuntu patch

* Tue Dec 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.6-alt1
- 1.8.6

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.4-alt2
- cairo-xcb: avoid leaking memory

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.4-alt1
- 1.8.4

* Thu Nov 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.2-alt4
- disabled directfb backend

* Thu Nov 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.2-alt3
- applied http://aur.archlinux.org/packages/cairo-lcd/cairo-lcd/lcd-filter.patch (close #17796)

* Fri Oct 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.2-alt2
- [scaled-font] fix typo that prevented meta_surface lookup

* Thu Oct 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.2-alt1
- 1.8.2

* Fri Sep 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.8.0-alt1
- 1.8.0

* Thu Aug 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.7.4-alt3
- enabled xcb backend

* Sat Aug 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.7.4-alt2
- applied post-1.7.4 upstream changes

* Wed Aug 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.7.4-alt1
- 1.7.4

* Mon May 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.4-alt3
- update lcd filtering patch from ubuntu

* Thu Apr 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.4-alt2
- rename ABI interface LIBCAIRO_1.6 to CAIRO_1.6

* Wed Apr 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.6.4-alt1
- 1.6.4
- Applied LCD subpixel filtering patch (close #14361)

* Mon Jan 21 2008 Alexey Tourbin <at@altlinux.ru> 1:1.4.14-alt1
- 1.4.12-9-g1ea07fd -> 1.4.14

* Thu Dec 27 2007 Alexey Tourbin <at@altlinux.ru> 1:1.4.12-alt1
- 1.4.10 -> 1.4.12-9-g1ea07fd (fixes CVE-2007-5503)
- build with libglitz (requested by Alexey Gladkov)

* Sun Jul 22 2007 Alexey Tourbin <at@altlinux.ru> 1:1.4.10-alt1
- rebased from 1.2 to 1.4 branch
- changed src.rpm packaging to keep upstream tarball

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.6-alt1
- 1.2.4-ga5f068e -> 1.2.6 release

* Sat Sep 30 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.5-alt0.1
- this is the first build from git repository, which I cloned from
  git://git.cairographics.org/git/cairo; I started off with 1.2.4 release
  and applied all my changes to the source tree (this is master branch);
  then I merged in the changes from current 1.2 brnach (1.2.4-ga5f068e)
  and changed rpm package version according to the changes
- enabled test suite
- added CAIRO_DIRECTFB ABI for cairo_directfb_surface_create()

* Thu Sep 07 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.4-alt2
- enabled directfb backend

* Mon Aug 21 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.4-alt1
- 1.2.2 -> 1.2.4
- no longer provides/obsoletes libpixman

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.2-alt1
- 1.2.0 -> 1.2.2
- renamed CAIRO_1.2.0 ABI to CAIRO_1.2

* Wed Aug 02 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.0-alt3
- upstream fix for size-zero glyphs (#9830)

* Mon Jul 10 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.0-alt2
- fixed set_dpi.patch

* Sun Jul 02 2006 Alexey Tourbin <at@altlinux.ru> 1:1.2.0-alt1
- 1.0.4 -> 1.2.0
- restored cairo_ps_surface_set_dpi() and cairo_pdf_surface_set_dpi()
  as aliases to cairo_surface_set_fallback_resolution() to preserve
  binary compatibility with libcairomm etc.
- introduced CAIRO_1.2.0 ABI
- packaged gtk-doc files

* Mon Apr 24 2006 Alexey Tourbin <at@altlinux.ru> 1:1.0.4-alt2
- urgency=high (for 1:1.0.4-alt1): use --enable-pdf and --enable-ps
  again to preserve ABI; also provide cairo_glitz_surface_create() stub
- restricted the list of symbols exported by the library

* Mon Apr 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Mon Feb 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt0.1
- CVS snapshot 20060213

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt3.1
- Rebuilt for new pkg-config dependencies.

* Thu Jan 19 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt3
- Backported upstream fix for text relocations.

* Tue Jan 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- added verify_elf_method textrel=relaxed

* Tue Oct 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Aug 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Aug 10 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Sat Jul 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Fri May 13 2005 Kachalov Anton <mouse@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Feb 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Wed Aug 25 2004 Kachalov Anton <mouse@altlinux.ru> 0.1.23-alt2
- added missed requires to libglitz-devel

* Thu Jul 08 2004 Kachalov Anton <mouse@altlinux.ru> 0.1.23-alt1
- first build for Sisyphus

