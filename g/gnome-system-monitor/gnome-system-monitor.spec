%define _unpackaged_files_terminate_build 1

%define ver_major 44
%define beta %nil
%def_enable systemd
%def_disable wnck

%define _libexecdir %_prefix/libexec

Name: gnome-system-monitor
Version: %ver_major.0
Release: alt1%beta

Summary: Simple process monitor
License: GPL-2.0
Group: Monitoring
Url: https://wiki.gnome.org/Apps/SystemMonitor

Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz

%define glib_ver 2.56.0
%define gtk_ver 3.22
%define glibmm_ver 2.28.0
%define libgtkmm3_ver 3.3.18
%define libwnck_ver 3.0.0
%define libgtop_ver 2.38.0
%define libxml_ver 2.0
%define rsvg_ver 2.35
%define handy_ver 1.5.0

Requires: polkit

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson gcc-c++ libappstream-glib-devel
BuildRequires: yelp-tools desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libglibmm-devel >= %glibmm_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgtkmm3-devel >= %libgtkmm3_ver
BuildRequires: libgtop-devel >= %libgtop_ver
BuildRequires: libxml2-devel >= %libxml_ver
BuildRequires: librsvg-devel >= %rsvg_ver
BuildRequires: libpolkit-devel
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
%{?_enable_wnck:BuildRequires: libwnck3-devel >= %libwnck_ver}
%{?_enable_systemd:BuildRequires: pkgconfig(systemd)}

%description
Gnome-system-monitor is a simple process and system monitor.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_systemd:-Dsystemd=true} \
    %{?_enable_wnck:-Dwnck=true}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%dir %_libexecdir/%name
%_libexecdir/%name/gsm-kill
%_libexecdir/%name/gsm-renice
%_libexecdir/%name/gsm-taskset
%_desktopdir/*
%_datadir/%name/
%_datadir/polkit-1/actions/org.gnome.%name.policy
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.%name.enums.xml
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/%name.appdata.xml


%changelog
* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0.1-alt1
- 3.18.0.1

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Jun 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt2
- rebuilt against libgtop-2.0.so.10

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

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
