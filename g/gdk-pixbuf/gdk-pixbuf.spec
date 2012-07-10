Name: gdk-pixbuf
Version: 0.22.0
Release: alt10.1

Summary: An image loading and rendering library for Gdk
Group: System/Libraries
License: LGPL
Url: http://www.gnome.org/

Source: ftp://ftp.gnome.org/pub/GNOME/sources/unstable/%name/%name-%version.tar.bz2

Patch0: ltmain.sh-inst_prefix.patch

Patch1: %name-0.11.0-mdk-demolink.patch
Patch2: %name-0.22.0-mdk-libdir.patch
Patch3: %name-0.22.0-mdk-xbmcrash.patch

Patch4: %name-0.22.0-rh-bmp-colormap.patch
Patch5: %name-0.22.0-rh-bmploop.patch
Patch6: %name-0.22.0-rh-ico-width.patch
Patch7: %name-0.22.0-rh-m4.patch
Patch8: %name-0.22.0-rh-bmpcrash.patch
Patch9: %name-0.22.0-rh-noexecstack.patch

Patch10: %name-0.22.0-rh-alt-bound.patch
Patch11: %name-0.22.0-alt-linkage.patch
Patch12: %name-0.22.0-alt-libs.patch
Patch13: %name-0.22.0-alt-DSO.patch

Provides: %name-loaders = %version-%release
Obsoletes: %name-loaders < %version-%release

# Automatically added by buildreq on Fri Oct 17 2008
BuildRequires: glib-devel gnome-libs-devel gtk+-devel
BuildRequires: libjpeg-devel libpng-devel libtiff-devel zlib-devel
BuildRequires: libXt-devel xorg-cf-files

%package gnomecanvas
Summary: An image loading and rendering library for Gdk
Group: System/Libraries
Requires: %name = %version-%release

%package xlib
Summary: An image loading and rendering library for Gdk
Group: System/Libraries
Requires: %name = %version-%release

%package devel
Summary: Development tools for GdkPixBuf applications
Group: Development/GNOME and GTK+
Requires: %name-gnomecanvas = %version-%release
Requires: %name-xlib = %version-%release

%description
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

%description gnomecanvas
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

This package provides GTK version of %name.

%description xlib
The GdkPixBuf library provides a number of features:
+ Image loading facilities.
+ Rendering of a GdkPixBuf into various formats:
  drawables (windows, pixmaps), GdkRGB buffers.

This package provides Xlib version of %name.

%description devel
The include files and documentation needed for developing GdkPixBuf
applications. GdkPixBuf is an image loading and rendering library
for Gdk.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p2
find -type f -name \*.orig -delete -print

%build
%set_libtool_version 1.4
%set_automake_version 1.4
%set_autoconf_version 2.13
%undefine __libtoolize
libtoolize -c -f
#patch -p0 <%PATCH0
aclocal
# new gettext introduce new m4 macros which depend on fresh autoconf
# and automake; hopefully glib doesn't use gettext and its m4 macros.
%__subst -p 's,^AC_PREREQ(\[\?2\.5[0-9]\]\?),AC_PREREQ(2.13),' *.m4
autoheader
automake
autoconf
%configure --disable-static --with-libwrap --disable-gtk-doc

make

%install
%makeinstall libexecdir=$RPM_BUILD_ROOT%_libdir/%name/loaders
install -pm755 %name/pixops/timescale $RPM_BUILD_ROOT%_bindir/
%__subst 's,/lib$,/%_lib,g' $RPM_BUILD_ROOT%_bindir/*-config

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%_libdir/libgdk_pixbuf.so.*
%_bindir/timescale
%dir %_libdir/%name
%dir %_libdir/%name/loaders
%_libdir/%name/loaders/*.so*

%files xlib
%_libdir/*xlib.so.*

%files gnomecanvas
%_libdir/*gnomecanvas*.so.*

%files devel
%_bindir/*-config
%_libdir/libgdk*.so
%_libdir/libgnome*.so
%dir %_includedir/%name-1.0
%_includedir/%name-1.0/%name
%_datadir/aclocal/*
%_libdir/*.sh
%doc %_datadir/gnome/html/*

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22.0-alt10.1
- Fixed build

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.22.0-alt10
- rebuilt for debuginfo
- merged gdk-pixbuf-loaders subpackage into gdk-pixbuf

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.22.0-alt9.6.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Jun 05 2010 Dmitry V. Levin <ldv@altlinux.org> 0.22.0-alt9.6
- Fixed build with gettext >= 0.18.

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.22.0-alt9.5.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for gdk-pixbuf
  * postun_ldconfig for gdk-pixbuf
  * post_ldconfig for gdk-pixbuf-gnomecanvas
  * postun_ldconfig for gdk-pixbuf-gnomecanvas
  * post_ldconfig for gdk-pixbuf-loaders
  * postun_ldconfig for gdk-pixbuf-loaders
  * post_ldconfig for gdk-pixbuf-xlib
  * postun_ldconfig for gdk-pixbuf-xlib
  * postclean-05-filetriggers for spec file

* Fri Oct 17 2008 Yury Aliaev <mutabor@altlinux.org> 0.22.0-alt9.5
- build dependencies fixed

* Wed May 14 2008 Yury Aliaev <mutabor@altlinux.org> 0.22.0-alt9.4
- build dependencies fixed

* Tue Feb 05 2008 Yury Aliaev <mutabor@altlinux.org> 0.22.0-alt9.3
- fix for new autotools

* Sun Nov 12 2006 Yury Aliaev <mutabor@altlinux.org> 0.22.0-alt9.2
- fixed build with --as-needed ld option
- fixed strange libtool issue (patch0 seems to be unneeded)

* Mon Jun 06 2005 Anton D. Kachalov <mouse@altlinux.org> 0.22.0-alt9.1
- Multilib support

* Fri Apr 08 2005 Dmitry V. Levin <ldv@altlinux.org> 0.22.0-alt9
- Fixed a double free in the bmp loader (RH).
- Marked libraries as non-execstack (RH).
- Disabled build of gtk docs.

* Sat Sep 18 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.22.0-alt8.1
- Rebuilt with libtiff.so.4.

* Fri Sep 17 2004 Dmitry V. Levin <ldv@altlinux.org> 0.22.0-alt8
- Fixed typo in rh-alt-bound patch introduced in 0.22.0-alt6.

* Mon Sep 06 2004 Dmitry V. Levin <ldv@altlinux.org> 0.22.0-alt7
- Cleaned up gdk-pixbuf-config library output.

* Fri Sep 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.22.0-alt6
- Merged few essential patches from RH package.
- Fixed build without %name-devel installed.
- Do not build and package static library by default.
- Fixed few potential overflows (CAN-2004-0782, CAN-2004-0783),
  patch from Matthias Clasen (RH).

* Mon Dec 22 2003 Nazar Yurpeak <phoenix@altlinux.org> 0.22.0-alt5
- fixed BuildPreReq

* Tue Dec 03 2003 Nazar Yurpeak <phoenix@altlinux.org> 0.22.0-alt4
- removed *.la

* Tue Oct 21 2003 Nazar Yurpeak <phoenix@altlinux.org> 0.22.0-alt3
- updated BuildRequires

* Wed Oct 08 2003 Nazar Yurpeak <phoenix@altlinux.org> 0.22.0-alt2
- bug #3079 fix
- updated BuildRequires

* Wed May 07 2003 Nazar Yurpeak <phoenix@altlinux.ru> 0.22.0-alt1
- new version

* Wed Feb  5 2003 Alexander V. Nikolaev <avn@altlinux.ru> 0.18.0-alt2
- Add missing depends for -devel
- Add packager tag

* Mon Oct 28 2002 AEN <aen@altlinux.ru> 0.18.0-alt1
- new version

* Tue May 14 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.17.0-alt1
- 0.17.0
- loaders in a dedicated directory
- rebuilt BuildRequires
- wiped out requires from gdk-pixbuf-devel: half were crazy,
  the other half obvious
- removed redundant HTML docs from the main package

* Mon Apr 08 2002 Sergey Vlasov <vsu@altlinux.ru> 0.16.0-alt2
- fixed XBM loader crash on invalid files

* Wed Jan 23 2002 AEN <aen@logic.ru> 0.16.0-alt1
- new version

* Mon Jan 21 2002 AEN <aen@logic.ru> 0.15.0-alt1
- new version

* Fri Dec 14 2001 AEN <aen@logic.ru> 0.14.0-alt1
- new release 

* Fri Nov 09 2001 AEN <aen@logic.ru> 0.13.0-alt2
- remove gnome-libs from devel Requires

* Fri Oct 26 2001 AEN <aen@logic.ru> 0.13.0-alt1
- new version

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.11.0-alt3
- Updated package requires.
- Rebuilt with libpng.so.3

* Tue May 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.11.0-alt2
- Moved static libraries to devel-static subpackage.

* Fri May 11 2001 AEN <aen@logic.ru> 0.11.0-alt1
- new version

* Wed Mar 14 2001 AEN <aen@logic.ru> 0.10.1-ipl1mdk
- new version

* Sun Jan 07 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.0-ipl4mdk
- Specfile cleanup.

* Mon Nov 28 2000 AEN <aen@logic.ru>
- build for RE

* Wed Sep 13 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.0-2mdk
- Split package in 3 flavors : Xlib, gtk, Gnome

* Fri Sep  8 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.0-1mdk
- Release 0.9.0
- more macroszification

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.8.0-2mdk
- automatically added BuildRequires

* Thu Jul 20 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8.0-1mdk
- release 0.8.0
- BM
- use make macro

* Tue Apr 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.0-1mdk
- release for gnome-core 1.1.9 from helix.
- stable version
- add doc files

* Thu Apr 13 2000 Daouda Lo <daouda@mandrakesoft.com> 0.6.0-6mdk
- having some problems to build 1.1.8 on top of gdk_pixbuf 0.7.0
- retro build.

* Thu Apr 13 2000 Daouda Lo <daouda@mandrakesoft.com> 0.7.0-1mdk
- release 0.7.0

* Wed Apr 12 2000 Daouda Lo <daouda@mandrakesoft.com> 0.6.0-5mdk
- The <LIBRARY>Conf.sh missing file cause gnome-core failed at building!
- SMP build/check

* Wed Apr 12 2000 Daouda Lo <daouda@mandrakesoft.com> 0.6.0-4mdk
- rebuild for near future gnome (used in Helix).
- build with %prefix is suitable
- many minor changes in file sections

* Wed Apr 05 2000 Francis Galiegue <fg@mandrakesoft.com> 0.6.0-3mdk

- Changed group for -devel
- Some spec file corrections

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 0.6.0-2mdk

- Rebuilt on kenobi

* Mon Mar 13 2000 Francis Galiegue <francis@mandrakesoft.com> 0.6.0-1mdk

- 0.6.0
- Changed group to match those of 7.1
- Spec file corrections
- Let spec-helper do its job

* Mon Jan 24 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- updated to 0.5.0

* Mon Nov 01 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- First mandrake package

