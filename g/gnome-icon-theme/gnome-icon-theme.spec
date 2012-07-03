%define ver_major 3.4
%define gtk_api_ver 2.0

Name: gnome-icon-theme
Version: %ver_major.0
Release: alt1

Summary: A set of icons for GNOME 2 desktop
License: LGPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Provides: icon-theme-gnome = %version-%release

%define icon_naming_utils_ver 0.8.7

Requires: icon-naming-utils >= %icon_naming_utils_ver

# From configure.in
BuildPreReq: intltool >= 0.40.0
BuildPreReq: pkgconfig >= 0.19
BuildPreReq: icon-naming-utils >= %icon_naming_utils_ver
BuildRequires: gtk-update-icon-cache perl-XML-Parser

%description
The standard set of icons for Gnome.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
ln -s gnome %buildroot%_iconsdir/default.gnome

%find_lang %name

%define conf_string gtk-icon-theme-name = \"gnome\"
%define gtkrc %_sysconfdir/gtk-%{gtk_api_ver}/gtkrc

%post
if [ -f %gtkrc ]; then
        grep -qs '^%conf_string$' %gtkrc ||
        echo '%conf_string' >> %gtkrc
fi

%postun
[ $1 = 0 ] || exit 0
if [ -f %gtkrc ]; then
	subst '/%conf_string/d' %gtkrc
fi ||:

%triggerin -- libgtk+2-common
if [ -f %gtkrc ]; then
        grep -qs '^%conf_string$' %gtkrc ||
        echo '%conf_string' >> %gtkrc
fi

%triggerpostun -- libgtk+2-common < 2.12.11-alt1
[ $2 != 0 ] || exit 0
if [ -f %gtkrc ]; then
        grep -qs '^%conf_string$' %gtkrc ||
        echo '%conf_string' >> %gtkrc
fi

%files -f %name.lang
%dir %_iconsdir/gnome
%_iconsdir/gnome/*
%_iconsdir/default.gnome
%_datadir/pkgconfig/*
%doc AUTHORS README TODO

%changelog
* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91-alt1
- 3.3.91

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1.2-alt1
- 3.2.1.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.0-alt1
- 2.31.0

* Wed May 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2.1-alt1
- 2.30.2.1

* Sat Apr 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Thu Mar 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.2-alt1
- 2.29.2

* Thu Mar 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt1
- 2.29.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Tue Jul 08 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt3
- set gtk-icon-theme-name = "gnome"
  in %%_sysconfdir/gtk-%%api_ver/gtkrc if this package installed

* Fri Jun 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt2
- %%_iconsdir/gnome and under owned by this package.

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Sat Mar 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)

* Sat Sep 22 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.0 -> 2.20.0

* Thu May 24 2007 Igor Zubkov <icesik@altlinux.org> 2.18.0-alt1
- 2.17.90 -> 2.18.0
- update Patch0

* Tue Jan 23 2007 Alexey Rusakov <ktirf@altlinux.org> 2.17.90-alt1
- new version (2.17.90)
- removed glib2-devel to fix building the package (it is not needed anyway;
  thanks to raorn@).
- updated the patch for index.theme file

* Wed Oct 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.17.1-alt1
- new version (again unstable branch, but we can afford this with icons)
- added Provides: icon-theme-gnome to make a look that we comply with
  GTK+/GNOME packaging policy.

* Mon Sep 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0.1-alt1
- new version (2.16.0.1)
- spec cleanup

* Thu Aug 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version 2.15.92 (with rpmrb script)

* Thu Aug 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version 2.15.90
- renewed the patch for index.theme of the default icon theme.

* Sat Mar 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.0-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Thu Mar 24 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1.1
- properly fixed "Inherits" tag.

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92.

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Tue Jan 25 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.90-alt1
- 2.7.90

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0
- Inherits=hicolor,default.kde

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.90-alt1
- 1.1.90

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Wed Feb 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt2
- no more move icons/gnome to icons/Gnome.

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Tue Jul 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue May 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Mon Mar 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Thu Jan 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt2
- OpenOffice and WINE mime icons, translation (slava)

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.91-alt1
- 0.91

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Mon Dec 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Sun Dec 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.3-alt2
- Move "Gnome" theme icons to the directory of the same name.

* Mon Nov 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Mon Nov 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.0-alt1
- First build for Sisyphus.
