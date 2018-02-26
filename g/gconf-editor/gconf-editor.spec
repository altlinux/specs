%define ver_major 3.0

Name: gconf-editor
Version: %ver_major.1
Release: alt1

Summary: An editor for the GConf configuration system.
License: GPLv2+
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define GConf_ver 2.32.1-alt2
%define gtk_ver 3.0.5

Requires(post,preun): GConf >= %GConf_ver

BuildPreReq: rpm-build-gnome >= 0.5
# From configure.in
BuildPreReq: intltool >= 0.35.0 librarian gnome-doc-utils
BuildPreReq: libGConf-devel >= %GConf_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: libgio-devel

%description
An editor for the GConf configuration system.
Directly edit your entire configuration database.

%prep
%setup -q

%build
%configure --disable-scrollkeeper \
    --disable-schemas-install

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %name
fi

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/*/*
%_man1dir/*
%_datadir/%name
%config %gconf_schemasdir/*
%doc AUTHORS ChangeLog README

%changelog
* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.91.1-alt1
- 2.91.91.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Fri Aug 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Thu Mar 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- updated buildreqs

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- new tango style icons.

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- updated buildreqs

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs
- removed obsolete %%post{,un} scripts

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0.1-alt1
- new version (2.24.0.1)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gconf-editor

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version (2.20.0)
- add Packager

* Thu Aug 09 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)
- use more macros, spec cleanup

* Sat Sep 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- updated depenedencies
- removed scrollkeeper workaround in the specfile.

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version (2.13.90)

* Sat Sep 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92.

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Thu Sep 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Fri Apr 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sat Sep 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Aug 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt2
- menu file fixed.

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- new version.

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt2
- rebuild with new pango, gtk+ with Xft2 support.

* Sun Sep 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt1
- 0.3.1
- gcc-3.2 used
- buildreqs updated

* Fri Jun 07 2002 Igor Androsov <blake@altlinux.ru> 0.2-alt1
- Create Spec for AltLinux Team
- Inital build
