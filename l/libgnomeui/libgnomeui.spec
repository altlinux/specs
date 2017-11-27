%def_enable snapshot

%define ver_major 2.24
%def_disable static
%def_enable gtk_doc

# For some reason, the above construct doesn't work is some places of the spec.
#define _disable_static --disable-static
%define _unpackaged_files_terminate_build 1

Name: libgnomeui
Version: %ver_major.5
Release: alt2

Summary: GNOME base GUI library
License: LGPL
Group: System/Libraries
Url: ftp://ftp.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
%else
Source: %name-%version.tar
%endif
Patch: libgnomeui-2.24.5-alt-gtk-doc.patch

# From configure.in
%define libxml_ver 2.4.20
%define libgnome_ver 2.13.7
%define libgnomecanvas_ver 2.0.0
%define libbonoboui_ver 2.13.1
%define GConf_ver 1.1.11
%define pango_ver 1.1.2
%define glib_ver 2.16.0
%define gio_ver 2.16.0
%define gtk_ver 2.12.0
%define gnome_vfs_ver 2.7.3
%define glade_ver 2.0.0
%define gnome_keyring_ver 0.4


Obsoletes: %name-utils
Provides: %name-utils = %version-%release

BuildPreReq: rpm-build-gnome
# From configure.in
BuildPreReq: libxml2-devel >= %libxml_ver
BuildPreReq: libgnome-devel >= %libgnome_ver
BuildPreReq: libgnomecanvas-devel >= %libgnomecanvas_ver
BuildPreReq: libbonoboui-devel >= %libbonoboui_ver
BuildPreReq: libGConf2-devel >= %GConf_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: gnome-vfs2-devel >= %gnome_vfs_ver
BuildPreReq: libgnome-keyring-devel >= %gnome_keyring_ver
BuildPreReq: intltool >= 0.35
BuildPreReq: gnome-common
BuildPreReq: libX11-devel libXt-devel libSM-devel libICE-devel
BuildPreReq: libjpeg-devel
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: libpopt-devel
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: libglade-devel >= %glade_ver
BuildRequires: gcc-c++ imake perl-XML-Parser xorg-cf-files

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME. (The
libgnome package includes the library features that don't use the X
Window System.)

%package devel
Summary: Libraries and headers for libgnome
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui-devel package
includes the libraries and include files that you will need to
use libgnomeui.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui package
includes GUI-related libraries that are needed to run GNOME.

This package provides development documentation for %name.

%if_enabled static
%package devel-static
Summary: Static libraries for libgnome
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnomeui-devel package
includes the libraries and include files that you will need to
use libgnomeui.

You should install the libgnomeui-devel-static package if you would like
to compile GNOME applications. You do not need to install libgnomeui-devel
if you just want to use the GNOME desktop environment.
%endif

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup
%patch

%build
%autoreconf
export DATADIRNAME=share
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make

%install
%makeinstall_std

bzip2 -9f ChangeLog

%find_lang %name-2.0

%files -f %name-2.0.lang
%_libdir/*.so.*
%_libdir/libglade/2.0/*.so
%_datadir/pixmaps/*
%doc AUTHORS ChangeLog.bz2 NEWS

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/*
%endif

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/libglade/*/*.a
%endif

%exclude %_libdir/libglade/*/*.la

%changelog
* Mon Nov 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.24.5-alt2
- updated to LIBGNOMEUI_2_24_5-13-g30334c2
- fixed doc build

* Mon Jan 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.5-alt1
- 2.24.5

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt2
- rebuild for update dependencies

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- removed obsolete %%post{,un}_ldconfig
- don't rebuild documentation

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0
- build devel-doc as noarch

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt2
- new version (2.22.1)

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.01-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.01-alt1
- new version (2.22.01)

* Wed Mar 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- updated BuildPreReq

* Fri Sep 21 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.1 -> 2.20.0

* Wed May 23 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- updated dependencies, cleaned up the spec, removed %%__ macros
- removed old --disable-static workaround.

* Thu Mar 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt2
- removed ChangeLog dup (Bug #11078)
- _unpackaged_files_terminate_build from now on.

* Wed Dec 20 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt1
- new version 2.16.1 (with rpmrb script)

* Mon Sep 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)

* Tue Aug 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- added libSM-devel to devel package requires.

* Thu Aug 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt2
- updated dependencies

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version (2.15.90)

* Mon Apr 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt2
- bumped up the version of required libbonoboui.
- fixed the location of gnome_segv2

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sat Mar 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Tue Feb 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.3-alt1
- new version
- spec cleanup
- Temporary ugly workaround instead of '%%def_disable static' due to obscure problems with rpmbuild.

* Tue Feb 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.12.0-alt1.2
- Buildreq

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.12.0-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.3-alt1
- 2.11.3

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.1-alt1
- 2.9.1
- documentation moved to devel-doc subpackage.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Sep 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Sun May 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1
- 2.6.1.1

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Sun Mar 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.92-alt1
- 2.5.92

* Wed Mar 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Thu Mar 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90.1-alt1
- 2.5.90.1

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.1-alt3
- do not package .la files.
- do not build devel-static subpackage by default.

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.1-alt2
- rebuild to reject dependence on libalsa.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.1-alt1
- 2.4.0.1

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt1
- 2.3.3.1

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Jan 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt2
- move gnome_segv2 to main package.

* Thu Jan 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Jan 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.2.90

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Mon Sep 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Fri Jun 14 2002 Igor Androsov <blake@altlinux.ru> 2.0.1-alt1
- Initail build for AltLinux
- (aris):
    + SMP-compatible build
    + ldconfig in post{,un}
    + files section fixed
    + other small fixes and cleanups.

* Wed May 15 2002 Igor Androsov <blace@mail.ru> 1.117.0-blk0.1
- New version from CVS
- Many changes for AltLinux
- Moved static libs to devel-static

* Mon Feb 25 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.112.0-1
- new version

* Mon Feb 18 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.111.1-1
- new version
- disabled gtk-doc
- disabled binary stripping
- split into more packages

* Mon Jan 28 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.109.0-4
- fixed dependancies

* Tue Jan 22 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.109.0-3
- replace libtoolize with /bin/echo
- new %files section
- replace tabs with spaces

* Sun Jan 20 2002 Roy-Magne Mo <rmo@sunnmore.net> 1.109.0-2
- touching file in $PWD instead of /usr/src/redhat
- removed glade and pixmap from glob

* Sat Jan 19 2002 Chris Chabot <chabotc@reviewboard.com>
- Import into gnome 2.0 alpha
- Changed versions accordingly
- Dirty hack to prevent warning on libgnomeui/pixmaps/copyright.txt
- Minor Cleanups

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- 1.108.0.90 snap, remove gconf stuff moved to libgnome

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- 1.106.0.90 snap, glib 1.3.11
- add explicit-versioned requires on dependency libs
- do gconftool stuff, put schemas in file list
- use makeinstall instead of destdir to avoid broken makefiles

* Mon Oct 29 2001 Havoc Pennington <hp@redhat.com>
- grumble, we require libglade 2 not libglade 1

* Mon Oct 29 2001 Havoc Pennington <hp@redhat.com>
- add libglade module to file list
- add libglade dependency

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- new snap, rebuild for glib 1.3.10

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- new tarball, rebuild for new glib, remove db1 dependency

* Mon Sep 24 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- Initial build.

