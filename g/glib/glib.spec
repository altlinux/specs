Name: glib
Version: 1.2.10
Release: alt18

Summary: A library of handy utility functions
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.gtk.org/

# ftp://ftp.gtk.org/pub/gtk/v1.2/glib-%version.tar.bz2
Source: glib-%version.tar
Patch1: glib-1.2.8-alt-texinfo.patch
Patch2: glib-1.2.10-rh-isowarning.patch
Patch3: glib-1.2.10-rh-m4.patch
Patch4: glib-1.2.10-rh-gcc34.patch
Patch5: glib-1.2.10-alt-linkage.patch

%def_enable static
%set_automake_version 1.4
%set_autoconf_version 2.13
%set_libtool_version 1.5

%package devel
Summary: Development environment for the glib library
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Static libraries for development with glib
Group: Development/C
Requires: %name-devel = %version-%release

%description
Glib is a handy library of utility functions.  This C library is designed
to solve some portability problems and provide other useful functionality
which most programs require.

%description devel
Include files for the glib support library.  GLIB includes generally
useful data structures.

%description devel-static
Static libraries for development statically linked glib-based programs.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
find -type f -name \*.orig -delete

%build
%add_optflags -fno-strict-aliasing
libtoolize --copy --force
aclocal
# new gettext introduce new m4 macros which depend on fresh autoconf
# and automake; hopefully glib doesn't use gettext and its m4 macros.
%__subst -p 's,^AC_PREREQ(\[\?2\.5[0-9]\]\?),AC_PREREQ(2.13),' *.m4
autoheader
automake
autoconf
sed -i 's,/lib/,/%_lib/,g; s,/lib ,/%_lib ,g' ltconfig

%configure %{subst_enable static}
%make_build

%install
mkdir -p %buildroot/%_lib
%makeinstall

# Relocate shared libraries from %_libdir/ to /%_lib/.
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -pm644 AUTHORS NEWS README %buildroot%docdir/
bzip2 -9 %buildroot%docdir/NEWS

%files
/%_lib/*
%dir %docdir
%docdir/[ABD-Z]*

%files devel
%_bindir/*
%_libdir/*.so
%_libdir/glib
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/aclocal/*
%_mandir/man?/*
%_infodir/*.info*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt18
- Rebuilt for debuginfo.

* Sat Oct 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt17
- Rebuilt for soname set-versions.

* Sat Jun 05 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt16
- Fixed build with gettext >= 0.18.

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt15
- Removed obsolete %%install_info/%%uninstall_info calls.
- Fixed build in new build environment.

* Mon Dec 15 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt14
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Removed redundant dependencies.

* Tue Jan 15 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt13
- Fixed build in new build environment.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt12
- Disabled gcc optimization based on strict aliasing rules.

* Thu Feb 02 2006 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt11
- Rebuilt.

* Mon Jul 04 2005 Anton D. Kachalov <mouse@altlinux.org> 1.2.10-alt10.1
- Hack to fix ltconfig (really closes #4881)

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt10
- Rerun autotools scripts.

* Thu Aug 26 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt9
- Fixed library linkage.
- Added multilib support (#4881).

* Tue Dec 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt8
- Require libtool_1.5 >= 3:1.5-alt10 for build.

* Tue Nov 25 2003 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt7
- Do not package .la files.

* Thu Oct 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt6
- Rebuilt to fix config files in devel subpackage.

* Tue Sep 17 2002 AEN <aen@altlinux.ru> 1.2.10-alt5
- rebuild with gcc-3.2

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt4
- Fixed libglib.la

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt3
- Added #pragma GCC system_header to suppress warnings when in -pedantic mode (rh).
- Added pkgconfig files.
- Updated %post/%postun scripts.
- Fixed library symlinks generation.
- Relocated documentation.
- Updated devel-static requirements.
- Additional convention enforcement on patch file names.

* Fri May 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.10-alt2
- Moved shared libraries from %_libdir to /lib.
- Moved static libraries to devel-static subpackage.

* Wed Apr 4 2001 AEN <aen@logic.ru> 1.2.10-alt1
- 1.2.10

* Sat Mar 3 2001 AEN <aen@logic.ru> 1.2.9-ipl1mdk
- new version
- strjoinv patch (temporary?) removed

* Fri Nov 24 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.8-ipl2mdk
- FHSification.
- Fixed texinfo documentation.
- Patch g_strconcat(), g_strjoin() and g_strjoinv() so they are executed
  in O(n) instead of O(n*n) (from DindinX <odin@mandrakesoft.com>).
- Moved doc to devel subpackage.

* Thu Jun 22 2000 Dmitry V. Levin <ldv@fandra.org>
- 1.2.8

* Thu Feb 24 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Sun Feb 20 2000 AEN <aen@logic.ru>
- 1.2.7

* Thu Nov 4 1999 AEN <aen@logic.ru>
-- build for RE

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable SMP build/check
- 1.2.6

* Wed Sep 29 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.2.5.

* Thu Aug 26 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 1.2.4

* Wed Jul 14 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- changed %prefix/man/man1 to %prefix/man/man1/*
- added back descriptions from RH 5.2

* Wed May 12 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 1.2.3

* Tue Apr 27 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- 1.2.2
- bzip2 man pages

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.1

* Fri Feb 26 1999 Michael Fulbright <drmike@redhat.com>
- Version 1.2

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.0pre1

* Tue Feb 23 1999 Cristian Gafton <gafton@redhat.com>
- new description tags

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- removed libtoolize from %build

* Thu Feb 11 1999 Michael Fulbright <drmike@redhat.com>
- added libgthread to file list

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.15

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.14

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.13

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.12

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated in preparation for the GNOME freeze

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package
