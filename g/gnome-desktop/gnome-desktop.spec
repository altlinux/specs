%define ver_major 2.32
%define api_ver 2.0
%define gnome_distributor "%vendor"
%define gnome_date "%(date "+%%B %%e %%Y"), Moscow"
%def_disable static

Name: gnome-desktop
Version: %ver_major.1
Release: alt4.1

Summary: The gnome desktop programs for the GNOME desktop environment
License: %gpl2plus, %fdl
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
Source1: gnome-about.png

Requires: lib%name = %version-%release
Requires: icon-theme-hicolor
# use pnp.ids from hwdatabase package
Requires: hwdatabase >= 0.3.31-alt1

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+2-devel >= 2.22.0
BuildPreReq: glib2-devel >= 2.19.1
BuildPreReq: libgio-devel >= 2.15.4
BuildPreReq: libGConf-devel >= 2.0.0
BuildPreReq: libstartup-notification-devel >= 0.5
BuildPreReq: gnome-doc-utils librarian-devel
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildRequires: python-devel python-modules-compiler
BuildRequires: libSM-devel libXrandr-devel
BuildRequires: hwdatabase >= 0.3.31-alt1

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software. The
%name package includes the basic programs and libraries that are needed
to install GNOME.

GNOME Desktop provides the core icons and libraries for the gnome
desktop.

%package -n lib%name
Summary: GNOME desktop core libraries
Group: Graphical desktop/GNOME
License: %lgpl2plus

%description -n lib%name
Gnome 2 desktop libraries.

%package -n lib%name-devel
Summary: GNOME desktop develop libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release
License: %lgpl2plus, %fdl

%description -n lib%name-devel
Gnome 2 desktop libraries and header files for creating GNOME panels.

%package -n lib%name-devel-doc
Summary: GNOME desktop development documentation
Group: Development/GNOME and GTK+
Conflicts: lib%name-devel < %version
License: %lgpl2plus, %fdl
BuildArch: noarch

%description -n lib%name-devel-doc
Development documentation for Gnome desktop library.

%if_enabled static
%package -n lib%name-devel-static
Summary: GNOME desktop develop libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release
License: %lgpl2plus

%description -n lib%name-devel-static
Gnome 2 desktop static libraries for creating GNOME panels.
%endif

%prep
%setup -q

%build
%configure \
    %{subst_enable static} \
    --disable-rebuilds \
    --disable-scrollkeeper \
    --with-gnome-distributor=%gnome_distributor \
    --with-pnp-ids-path=%_datadir/misc

%make_build

%install
%make_install DESTDIR=%buildroot install

# already shipped in gnome-desktop3
rm -rf %buildroot%_datadir/omf
rm -rf %buildroot%_datadir/gnome/help

%find_lang --with-gnome --output=%name.lang %name-%api_ver

%files
%_bindir/*
%_desktopdir/*
%_datadir/gnome-about
%_pixmapsdir/*
%_man1dir/*
%doc AUTHORS NEWS README

%files -n lib%name -f %name.lang
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.32.1-alt4.1
- Rebuild with Python-2.7

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt4
- fix conflict with libgnome-desktop3

* Tue May 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt3
- requires hwdatabase with pnp.ids, not pci.ids

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- rebuild for debuginfo

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Aug 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.90-alt1
- 2.31.90

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92 (libgnome-desktop-2.so.17->.18)
- requires pciids

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Wed Jan 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Tue Dec 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Thu Dec 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Fri Dec 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Mon Oct 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Wed May 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Fri Feb 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts
- move documentation to lib%%name-devel-doc noarch subpackage

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)
- update randr code (patch2)
- handle slideshow start times in the future correctly
- fix some logic errors wrt to caching of slideshows that
  may cause nautilus crashes

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus
- remove gnome-vfs from BuildPreReq

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Wed Mar 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- updated BuildPreReq

* Sat Dec 29 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.2-alt2
- Use rpm-build-gnome and rpm-build-licenses.
- Specified proper Licenses for each subpackage.
- Updated dependencies.
- Removed runtime dependency on yelp (ALT Bug #13387).

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- new version (2.20.2)

* Thu Nov 22 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager
- add in gnome-about.desktop OnlyShowIn=GNOME

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)

* Fri Jun 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- fixed Bug 12040

* Wed Jun 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- checked dependencies, removed explicit dependencies on library packages from
  gnome-desktop subpackages.

* Sat Feb 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)
- dropped the dependency on gnome-user-docs

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- removed /usr/share/gnome items, as they went to gnome-filesystem package.

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version 2.15.92 (with rpmrb script)

* Sat Aug 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- updated dependencies
- spec cleanup

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version
- updated required Gtk+ version.

* Tue Apr 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- added gtk-doc files (for the moment, to lib%name-devel package).
- removed Debian menu support.
- cleaned up the spec.

* Tue Mar 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Mon Feb 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version
- Updated dependencies from configure.in and .pc files.

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Scrollkeeper dependency fixes.
- Removed excess buildreqs.

* Wed Apr 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92.

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90.1-alt1
- 2.9.90.1

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.1-alt1
- 2.6.0.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Wed Mar 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3
- /usr/share/application-registry owned by gnome-desktop package (close #3509).

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt2
- do not package .la files.
- do not build devel-static subpackage by default.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt1
- 2.4.1.1

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6.1-alt1
- 2.3.6.1

* Wed Jul 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt1
- 2.3.3.1

* Sun Jun 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Nov 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Fri Oct 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Sep 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt2
- yelp and gnome2-user-docs added to requires list.

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Thu Jun 20 2002 Igor Androsov <blake@altlinux.ru> 2.0.1-alt1
- Initial build for AltLinux
  (aris)
    + %name-devel{,-static} renamed to lib%name-devel{,-static}.
    + post{,un} sections fixed.
    + build process fixed (SMP compatible build).
- Fixes from Yuri Sedunov <aris@altlinux.ru>
    + sawfish2 added to requires list
    + replace command by macros
    + cleaup spec

* Tue Mar 05 2002 Chris Chabot <chabotc@reviewboard.com>
- Fixed remaining formating issues
- converted to .spec.in

* Sun Feb 15 2002 Chris Chabot <chabotc@reviewboard.com>
- initial spec file for gnome-desktop
