%define ver_major 3.4
%def_enable systemd

Name: gnome-system-monitor
Version: %ver_major.1
Release: alt1

Summary: Simple process monitor
License: GPLv2+
Group: Monitoring
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.in
%define glib_ver 2.28.0
%define gtk_ver 3.0.5
%define glibmm_ver 2.28.0
%define libgtkmm3_ver 3.0.0
%define libwnck_ver 3.0.0
%define libgtop_ver 2.28.2
%define libxml_ver 2.0
%define rsvg_ver 2.35
%define gnome_icon_theme_ver 3.0.0
%define systemd_ver 38

PreReq: librarian

BuildPreReq: rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libglibmm-devel >= %glibmm_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgtkmm3-devel >= %libgtkmm3_ver
BuildPreReq: libwnck3-devel >= %libwnck_ver
BuildPreReq: libgtop-devel >= %libgtop_ver
BuildPreReq: gnome-icon-theme >= %gnome_icon_theme_ver
BuildPreReq: libxml2-devel >= %libxml_ver
BuildPreReq: librsvg-devel >= %rsvg_ver
BuildPreReq: gnome-doc-utils gnome-common
BuildRequires: docbook-dtds gnome-doc-utils-xslt librarian
BuildRequires: gcc-c++
%{?_enable_systemd:BuildRequires: systemd-devel}

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -q

%build
%configure \
    --disable-scrollkeeper \
    --disable-schemas-compile \
    %{subst_enable systemd}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_pixmapsdir/%name/
%_desktopdir/*
%_datadir/%name/
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.gnome-system-monitor.enums.xml

%changelog
* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Mar 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91-alt1
- 3.3.91

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.0-alt1
- 2.99.0

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Sat May 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Jan 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.4-alt1
- 2.24.4

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3
- removed obsolete %%post{,un} scripts

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Sun Sep 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.4-alt1
- new version

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-system-monitor

* Mon Apr 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager

* Thu Jul 19 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- updated dependencies, more use of macros in the spec
- updated files list; removed scrollkeeper files exclusion

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)

* Mon Aug 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version (2.15.92)
- spec cleanup
- gksu support has been dropped

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sat Apr 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Sun Feb 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version
- updated dependencies, cleaned up the spec
- got rid of Debian menu stuff
- no more gnomesu support
- gksu support temporarily disabled, until libgksu comes.

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Fri Oct 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Sat Sep 03 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92.

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Sun Jun 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0
- fix ##2076, 3818

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Aug 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Fri Jun 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- new version.

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt2
- rebuild with new pango, gtk+

* Sat Sep 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt1
- First build for Sisyphus.
