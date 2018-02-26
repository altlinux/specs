%define ver_major 3.2

Name: gnome-nettool
Version: %ver_major.0
Release: alt1

Summary: GNOME interface for various networking tools
License: %gpl2only
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Obsoletes: gnome-netinfo
Provides: gnome-netinfo = %version-%release

Requires: net-tools
Requires: iputils
Requires: traceroute

BuildPreReq: rpm-build-gnome >= 0.6 gnome-common
BuildPreReq: rpm-build-licenses
BuildPreReq: desktop-file-utils >= 0.8

# From configure.in
BuildPreReq: intltool >= 0.40.1
BuildPreReq: libgtk+3-devel >= 2.99.2
BuildPreReq: libgio-devel libgtop-devel
BuildRequires: gnome-doc-utils gnome-doc-utils-xslt xsltproc

%description
GNOME Nettool is a set of front-ends to various networking command-line
tools, like ping, netstat, ifconfig, whois, traceroute, finger.

%prep
%setup -q

# don't run gtk_update_icon_cache
subst '/install-data-hook: update-icon-cache/d' pixmaps/icons/Makefile.in

%build
%configure \
	--disable-scrollkeeper

#	--disable-schemas-compile

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name
%config %_datadir/glib-2.0/schemas/*.xml

#icons
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%doc README NEWS TODO ChangeLog

%changelog
* Fri Apr 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Jan 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Jan 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun Aug 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Wed Nov 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- updated russian translation from upstream git

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed May 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Mar 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- removed obsolete %%post{,un} scripts
- updated buildreqs

* Fri Oct 03 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- new version

* Tue Jun 10 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- new version
- use {update,clean}_scrollkeeper and {update,clean}_desktopdb in %%post{un}
- modified %%files section
- use macroses from rpmbuild-gnome rpmbuild-licenses
- add Packager tag

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.16.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-nettool

* Wed Feb 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.0-alt1
- new version (2.16.0)
- updated dependencies

* Mon May 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt2
- fixed invalid GConf1 dependency.

* Thu May 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Wed Mar 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.91-alt1
- new version (2.13.91)
- removed Debian menu support
- revised dependencies.

* Wed Oct 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.4.1-alt1
- new version

* Sat Oct 01 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.4.0-alt1
- new version
- Removed excess buildreqs.

* Fri Mar 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.99.0-alt0.6
- fixed %%build.

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.99.0-alt0.5
- First build for Sisyphus.

