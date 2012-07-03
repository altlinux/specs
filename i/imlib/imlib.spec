Name: imlib
Version: 1.9.15
Release: alt4

Summary: An image loading and rendering library for X11R6
License: LGPL
Group: System/Libraries

Url: http://freshmeat.net/projects/imlib
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/imlib/1.9/imlib-%version.tar.bz2
Source1: imlib-pofiles.tar.bz2
Source2: http://cvs.pld-linux.org/cgi-bin/cvsweb/packages/imlib/imlib-config.desktop
Patch1: imlib-1.9.14-mdk-rh-m4.patch
Patch2: imlib-1.9.14-alt-imlib_config-i18n.patch
Patch3: imlib-1.9.14-alt-path.patch
Patch4: imlib-1.9.15-alt-configure.patch
Patch5: imlib-1.9.14-alt-linkage.patch
Patch6: imlib-1.9.14-peak-fixes.patch
Patch7: imlib-1.9.14-alt-gdk_imlib-modules-debug.patch
Patch8: imlib-1.9.15-debian-shm.patch
Patch9: imlib-1.9.15-asneeded.patch
Patch10: imlib-1.9.15-alt-DSO.patch
Packager: Dmitry V. Levin <ldv@altlinux.org>

Provides: lib%name = %version-%release
Obsoletes: Imlib, lib%name

%def_disable static

# Automatically added by buildreq on Sat Jun 06 2009
BuildRequires: gtk+-devel libSM-devel libXext-devel libgif-devel libjpeg-devel libpng-devel libtiff-devel

%package cfgeditor
Summary: A configuration editor for the Imlib library
Group: System/Libraries
Requires: %name = %version-%release

%package devel
Summary: Includes and other files to develop imlib applications
Group: Development/GNOME and GTK+
Requires: %name = %version-%release, %name-cfgeditor = %version-%release
Requires: gtk+-devel libSM-devel libXext-devel libjpeg-devel libpng-devel libtiff-devel libungif-devel
Provides: lib%name-devel = %version-%release
Obsoletes: lib%name-devel

%package devel-static
Summary: Static library files to develop imlib applications
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release, libpng3-devel-static
Provides: lib%name-devel-static = %version-%release
Obsoletes: lib%name-devel-static

%description
Imlib is a display depth independent image loading and rendering library.
Imlib is designed to simplify and speed up the process of loading images
and obtaining X Window System drawables.  Imlib provides many simple
manipulation routines which can be used for common operations.

%description cfgeditor
The imlib-cfgeditor package contains the %{name}_config program, which
you can use to configure the Imlib image loading and rendering library.
Imlib_config can be used to control how Imlib uses color and handles
gamma corrections, etc.

%description devel
The header files, static libraries and documentation needed for developing
Imlib applications.  Imlib is an image loading and rendering library
for X11R6.

%description devel-static
The static libraries needed to link Imlib applications statically
with Imlib.  Imlib is an image loading and rendering library for X11R6.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%{?_enable_debug:%patch7 -p1}
%patch8 -p1
%patch9 -p0
%patch10 -p2

%build
%autoreconf
%add_optflags -DENABLE_NLS
export \
	ac_cv_lib_dnet_dnet_ntoa=no \
	ac_cv_path_CJPEG_PROG=%_bindir/cjpeg \
	ac_cv_path_DJPEG_PROG=%_bindir/djpeg \
	ac_cv_path_CONVERT_PROG=%_bindir/convert \
	ac_cv_path_GIFTOPNM_PROG=%_bindir/giftopnm \
	#
%configure %{subst_enable static}
#SMP-incompatible build
%make
# Compile locales by hand.
pushd po
	for f in *.po; do
		msgfmt -v -o "${f%%.po}.mo" "$f"
	done
popd

%install
%makeinstall

# Install locales by hand.
pushd po
	for f in *.mo; do
		install -pD -m644 "$f" "%buildroot%_datadir/locale/${f%%.mo}/LC_MESSAGES/imlib.mo"
	done
popd

install -pD -m644 %SOURCE2 %buildroot%_desktopdir/imlib-config.desktop

%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -p -m644 README AUTHORS ChangeLog doc/*.{gif,html} \
	%buildroot%docdir/
bzip2 -9 %buildroot%docdir/ChangeLog

%find_lang imlib

%files
%_libdir/*.so.*
%_libdir/libimlib-*.so
%config(noreplace) %_sysconfdir/*
%dir %docdir
%docdir/[AR]*

%files cfgeditor -f imlib.lang
%_bindir/*_config
%_man1dir/*_config.*
%_desktopdir/imlib-config.desktop

%files devel
%_bindir/*-config
%_man1dir/*-config.*
%_libdir/libImlib.so
%_libdir/libgdk_imlib.so
%_includedir/*
%_libdir/pkgconfig/*.pc
%_datadir/aclocal/*
%dir %docdir
%docdir/C*
%docdir/*.gif
%docdir/*.html

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt4
- Fixed build

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.15-alt3
- Rebuilt for soname set-versions

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 1.9.15-alt2.3
- NMU:
  + replaced debian menufile with freedesktop one (PLD)
  + updated an Url:, sort of
  + spec cleanup
  + buildreq

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 1.9.15-alt2.2
- NMU: applied Gentoo as-needed patch to fix FTBFS

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 1.9.15-alt2.1
- NMU: applied Debian patch to fix incorrect rendering
  when the MIT-SHM extension doesn't support shared pixmaps
  (e.g. using EXA with current versions of Xorg).
  + see debian bug #448360
  + manifests in e.g. kdegraphics-quickshow
  + closes: #17515

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.9.15-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig and %%update_menus/%%clean_menus calls.

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.9.15-alt1
- Updated to 1.9.15.
- Updated build and install dependencies.

* Sun Jan 09 2005 Dmitry V. Levin <ldv@altlinux.org> 1.9.14-alt5
- Applied patch from Pavel Kankovsky, to fix several
  heap overflow and integer overflow flaws.

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.9.14-alt4.1
- Rebuilt with libtiff.so.4.

* Thu Sep 02 2004 Dmitry V. Levin <ldv@altlinux.org> 1.9.14-alt4
- Fixed more potential heap corruption bugs.

* Mon Aug 30 2004 Dmitry V. Levin <ldv@altlinux.org> 1.9.14-alt3
- Relaxed error handling in heap corruption fixes, to load
  as much of broken bmp image as possible.

* Fri Aug 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1.9.14-alt2
- Relaxed linkage fix made in previous package release,
  to support broken packages.

* Thu Aug 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.9.14-alt1
- Updated to 1.9.14.
- Rediffed patches.
- Fixed few potential heap corruption bugs.
- Relocated documentation.
- Packaged pkgconfig files.
- Fixed library linkage.
- Cleaned up imlib-config and pkgconfig library output.

* Wed Aug 25 2004 Dmitry V. Levin <ldv@altlinux.org> 1.9.13-alt7
- Fixed BMP loader integer overflow bug, see
  http://bugzilla.gnome.org/show_bug.cgi?id=151034 for details.
- Fixed underquoted m4 definitions.

* Mon Jan 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1.9.13-alt6
- Do not build static library by default.

* Sat Jan 03 2004 Vitaly Lipatov <lav@altlinux.ru> 1.9.13-alt5
- rebuild without *.la files

* Wed Oct 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1.9.13-alt4
- Backported file descriptor leak and extra waitpid fixes from 1.9.14 (rh).
- Fixed configure.
- Rebuilt to fix config files in devel subpackage.
- Updated buildrequires (#0001381).

* Wed Apr 10 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.9.13-alt3
- Do the same for -devel and -devel-static subpackages.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.9.13-alt2
- Set explicit versioned requires on libpng3,
  to enforce libpng upgrade.

* Thu Mar 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.9.13-alt1
- 1.19.3
- bug #97 closed

* Wed Oct 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.9.11-alt2
- Fixed imlib_config i18n patch.
- Rebuilt with libpng.so.3, updated dependencies.

* Wed Sep 05 2001 AEN <aen@logic.ru> 1.9.11-alt1
- patches adopted to new version

* Sat May 19 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.9.10-alt2
- Moved *.la back to devel, stupid me.
- Added menu stuff from 1.9.10-5mdk

* Tue May 15 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.9.10-alt1
- Version 1.9.10
- Added devel-static subpackage
- Cleaned up BuildReqs

* Sun Jan 07 2001 Dmitry V. Levin <ldv@fandra.org> 1.9.8.1-ipl9mdk
- Specfile cleanup.
- Updated i18n patch.

* Tue Dec 19 2000 AEN <aen@logic.ru>
- old lib policy :-)
- adopted for RE

* Tue Nov 28 2000 dam's <damien@mandrakesoft.com> 1.9.8.1-7mdk
- imlib-profiles sourced
- new lib policy

* Sat Sep 30 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.9.8.1-6mdk
- added gtk+-devel BuildRequires.

* Mon Sep 11 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.9.8.1-5mdk
- rebuilt to have the correct provides.

* Mon Sep 11 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.9.8.1-4mdk
- Added new languages (Slovak, Czech, Hungarian, Esperanto, Bulgarian,
  Vietnamese and Russian)

* Fri Sep  8 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.9.8.1-3mdk
- Correct build dependency (Thanks Pedro Rosa)
- Use find_lang macro

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.9.8.1-2mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.9.8.1-1mdk
- release 1.9.8.1
- BM, macroszification
- clean spec

* Tue May 02 2000 Warly <warly@mandrakesoft.com> 1.9.8-10mdk
- rebuild to have good provides

* Sat Apr 29 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.9.8-9mdk
- Added new langs: Lithuanian, Esperanto, Finnish, Slovakian, Norwegian,
  Bulgarian, Galician, Danish and Croatian

* Wed Mar 22 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.9.8-8mdk
- new Groups: naming
- rebuild with new gtk+/glib libs
- added German, Bulgarian, Dutch and Chinese interfaces

* Fri Feb 25 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 7mdk
- several new and improved translations

* Mon Jan 24 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Portuguese interface

* Tue Jan 18 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added da, ca languages

* Fri Nov 05 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added hu, id, it, pl, ro, uk translations

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Sane SMP build

* Sun Oct 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.9.8

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 1.9.7

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix bug with palettes reported by Rudi Pittman
(famewolf@georgia.army.net).

* Mon Jul 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Building release (3mdk).

* Thu Jul 08 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- imlib_config has i18n support; simply it isn't used (I don't knwo why);
  I just enabled it back and included the spanish translation file

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch to upgrade the imlib.m4 to the proper version.
- we strip binary with our macros.
- 1.9.5 version.

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.

* Tue Apr 06 1999 Michael Fulbright <drmike@redhat.com>
- quiet imlib when initializing

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- added development requirements for imlib-devel

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.9.4, moved %_sysconfdir to %_sysconfdir

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 1.9.3

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- build against gtk+ 1.1.14

* Mon Jan 25 1999 Michael Fulbright <drmike@redhat.com>
- fixed file list to include lib_imlib*.so in main pkg, not devel pkg

* Wed Jan 20 1999 Michael Fulbright <drmike@redhat.com>
- moved to version 1.9.2

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- moved to version 1.9.1, main feature - dyn loading of image
  support libs - saves memory and speeds startup of apps.

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- moved imlib-config moved to devel package
- new version of gtk+ forced us to rebuild imlib

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- up to 1.8.2 in prep for GNOME freeze

* Wed Sep 23 1998 Carsten Haitzler <raster@redhat.com>
- up to 1.8.1

* Tue Sep 22 1998 Cristian Gafton <gafton@redhat.com>
- yet another build for today (%%defattr and %%attr in the files lists)
- devel docs are back on the spec file

* Tue Sep 22 1998 Carsten Haitzler <raster@redhat.com>
- Added minor patch for ps saving code.

* Mon Sep 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 1.8

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- take out imlib_config from devel package

* Wed Sep 9 1998 Michael Fulbright <msf@redhat.com>
- upgraded to 1.7
- changed name so it will persist if user later install devel imlib
- added subpackage for imlib_config

* Fri Apr 3 1998 Michael K. Johnson <johnsonm@redhat.com>
- fixed typo

* Fri Mar 13 1998 Marc Ewing <marc@redhat.com>
- Added -k, Obsoletes
- Integrate into CVS source tree
