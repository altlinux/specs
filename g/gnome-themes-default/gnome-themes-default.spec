%define _name gnome-themes
%define ver_major 2.32

Name: %_name-default
Version: %ver_major.1
Release: alt1

Summary: A set of default themes for GNOME 2 desktop
License: LGPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.bz2

%undefine _configure_target
BuildArch: noarch

%define icon_theme icon-theme
%define old_icon_theme gnome-icon-theme
%define icon_theme_namechange_ver 2.16.1.1-alt4

%define theme_prefix gnome-theme
%define old_theme_prefix gtk2-themes
%define namechange_ver 2.16.1.1
%define gtk_theme_prefix gtk2-theme

%define metacity_theme_prefix metacity-theme
%define old_metacity_theme_prefix metacity-themes

Requires: %icon_theme-crux = %version-%release
Requires: %icon_theme-mist = %version-%release
Requires: %{icon_theme}s-accessibility = %version-%release
Requires: %{theme_prefix}s-accessibility = %version-%release
Requires: %theme_prefix-crux = %version-%release
Requires: %theme_prefix-glider = %version-%release
Requires: %theme_prefix-mist = %version-%release
Requires: %theme_prefix-clearlooks = %version-%release
Requires: %theme_prefix-glossy = %version-%release
Requires: %gtk_theme_prefix-simple = %version-%release

# From configure.in
%define gtk_engines_ver 2.17.1
%define icon_theme_ver 2.24.0

BuildPreReq: intltool >= 0.35.0
BuildPreReq: libgtk+2-devel
# libgtk-engines-devel only appeared in 2.8.0-alt3, actually; it was named
# gtk-engines-default-devel, but to force apt to choose the new package, we
# use the new name.
BuildPreReq: libgtk-engines-devel >= %gtk_engines_ver
BuildPreReq: icon-naming-utils >= 0.8.0

BuildRequires: gnome-common perl-XML-Parser

%description
This package provides a set of default themes for GNOME 2 desktop.

%package common
Summary: Common files for GNOME default themes
Group: Graphical desktop/GNOME
BuildArch: noarch
Obsoletes: %old_theme_prefix-common < %namechange_ver
Provides: %old_theme_prefix-common = %version-%release
Obsoletes: gnome-themes-common < 2.16.1.1-alt3

%description common
This package contains common files needed to use GNOME default themes.

%package -n %{gtk_theme_prefix}s-accessibility
Summary: Accessibility themes for GTK+2
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release
Requires: libgtk-engine-hc >= %gtk_engines_ver

%description -n %{gtk_theme_prefix}s-accessibility
This package provides accessibility themes for GTK+2.

%package -n %{theme_prefix}s-accessibility
Summary: Accessibility themes for GNOME 2
Group: Graphical desktop/GNOME
Obsoletes: %old_theme_prefix-accessibility < %namechange_ver
Provides: %old_theme_prefix-accessibility = %version-%release

Requires: %name-common = %version-%release
Requires: %{gtk_theme_prefix}s-accessibility = %version-%release

%description -n %{theme_prefix}s-accessibility
This package provides accessibility themes for GNOME 2.

%package -n %theme_prefix-crux
Summary: A theme for GNOME 2
Group: Graphical desktop/GNOME
Obsoletes: %old_theme_prefix-Crux < %namechange_ver
Provides: %old_theme_prefix-Crux = %version-%release

Requires: %name-common = %version-%release
Requires: %gtk_theme_prefix-crux
Requires: %old_icon_theme-crux
Requires: metacity-theme-crux >= 2.28

%description -n %theme_prefix-crux
This package contains Crux - a GNOME 2 theme developed by Eazel, Inc.

%package -n %theme_prefix-mist
Summary: A theme for Metacity and GNOME 2
Group: Graphical desktop/GNOME
Obsoletes: %old_theme_prefix-Mist < %namechange_ver
Provides: %old_theme_prefix-Mist = %version-%release

Provides: %metacity_theme_prefix-mist = %version-%release
Provides: metacity-theme = %version-%release

Requires: %name-common = %version-%release
Requires: %gtk_theme_prefix-mist
Requires: %old_icon_theme-mist >= %icon_theme_ver
Requires: %metacity_theme_prefix-mist

%description -n %theme_prefix-mist
Author named this after the song he was listening to when he named it
(Opeth's "In Mist She Was Standing").
This package provides a window decoration for Metacity and a preset for
GNOME 2 theme switcher.

%package -n %gtk_theme_prefix-glider
Summary: A theme for GTK+2
Group: Graphical desktop/GNOME
Requires: libgtk-engine-glide >= %gtk_engines_ver

%description -n %gtk_theme_prefix-glider
This package provides Glider theme for GTK+2.

%package -n %gtk_theme_prefix-ClearlooksClassic
Summary: A theme for GTK+2
Group: Graphical desktop/GNOME
Requires: %gtk_theme_prefix-clearlooks >= %gtk_engines_ver

%description -n %gtk_theme_prefix-ClearlooksClassic
This package provides classic Clearlooks theme for GTK+2.

%package -n %theme_prefix-glider
Summary: A theme for GNOME 2, and Metacity
Group: Graphical desktop/GNOME
Obsoletes: %old_theme_prefix-Glider < %namechange_ver
Provides: %old_theme_prefix-Glider = %version-%release
Obsoletes: %old_metacity_theme_prefix-glider < %namechange_ver
Provides: %old_metacity_theme_prefix-glider = %version-%release

Provides: %metacity_theme_prefix-glider = %version-%release
Provides: metacity-theme = %version-%release

Requires: %name-common = %version-%release
Requires: %gtk_theme_prefix-glider = %version-%release
Requires: gnome-%icon_theme >= %icon_theme_ver
Requires: %metacity_theme_prefix-glider

%description -n %theme_prefix-glider
This package provides Glider themes: a window decoration for Metacity, and a preset for GNOME 2 theme switcher.

%package -n %theme_prefix-clearlooks
Summary: A theme for GNOME and Metacity
Group: Graphical desktop/GNOME
Obsoletes: %old_theme_prefix-Clearlooks < %namechange_ver
Provides: %old_theme_prefix-Clearlooks = %version-%release
Obsoletes: %old_metacity_theme_prefix-clearlooks < %namechange_ver
Provides: %old_metacity_theme_prefix-clearlooks = %version-%release

Provides: %metacity_theme_prefix-clearlooks = %version-%release
Provides: %metacity_theme_prefix-ClearlooksClassic = %version-%release
Provides: metacity-theme = %version-%release

Requires: %name-common = %version-%release
Requires: gnome-%icon_theme >= %icon_theme_ver
Requires: %gtk_theme_prefix-clearlooks >= %gtk_engines_ver
Requires: %gtk_theme_prefix-ClearlooksClassic = %version-%release
Requires: %metacity_theme_prefix-clearlooks

%description -n %theme_prefix-clearlooks
Clearlooks is the official default theme of GNOME 2.12-2.16.
This package provides a window decoration for Metacity and a preset for
GNOME 2 theme switcher.

%package -n %gtk_theme_prefix-glossy
Summary: A Clearlooks-based theme for GTK+ applications
Group: Graphical desktop/GNOME
Requires: libgtk-engine-clearlooks >= %gtk_engines_ver

%description -n %gtk_theme_prefix-glossy
This package contains Glossy theme for GTK+ applications. Note: if you want to
have Glossy window decoration or GNOME theme, you should install
%theme_prefix-glossy package.

%package -n %theme_prefix-glossy
Summary: A Clearlooks-based theme for GNOME
Group: Graphical desktop/GNOME
Requires: metacity
Provides: %metacity_theme_prefix-glossy = %version-%release
Provides: metacity-theme = %version-%release
Requires: libgnome
Requires: %gtk_theme_prefix-glossy >= %gtk_engines_ver
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %theme_prefix-glossy
This package provides Glossy theme (a preset for GNOME 2 theme switcher).

%package -n %gtk_theme_prefix-simple
Summary: A theme for GTK+2
Group: Graphical desktop/GNOME
Obsoletes: %old_theme_prefix-Simple < %namechange_ver
Provides: %old_theme_prefix-Simple = %version-%release
Requires: libgtk-engine-glide >= %gtk_engines_ver

%description -n %gtk_theme_prefix-simple
This package provides a Simple theme for GTK+2.

%package -n %{icon_theme}s-accessibility
Summary: Accessibility icon themes for fd.o compliant graphical environments
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release

%description -n %{icon_theme}s-accessibility
This package provides a set of icon themes designed for accessibility.

%package -n %icon_theme-crux
Summary: A Crux icon theme
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release
Obsoletes: %old_icon_theme-crux < %icon_theme_namechange_ver
Provides: %old_icon_theme-crux = %version-%release

%description -n %icon_theme-crux
This package provides a Crux icon theme.

%package -n %icon_theme-mist
Summary: A Mist icon theme
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release
Obsoletes: %old_icon_theme-mist < %icon_theme_namechange_ver
Provides: %old_icon_theme-mist = %version-%release

%description -n %icon_theme-mist
This package provides a Mist icon theme.

%prep
%setup -q -n %_name-%version

%__subst 's,\$2/\(\$ORIG_FILE\),\1,' common/mkiconlinks.sh

%build
%configure \
	--enable-all-themes \
	--disable-placeholders \
	--enable-icon-mapping \
	--disable-test-themes

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_iconsdir -name "index.theme" -print0|\
xargs -r0 %__subst 's|\(Inherits=.*$\)|\1,hicolor,default.kde|' --

%find_lang %_name

%files

%files common -f %_name.lang
%doc README ChangeLog AUTHORS

%files -n %{gtk_theme_prefix}s-accessibility
%dir %_datadir/themes/HighContrast*
%dir %_datadir/themes/HighContrast*/gtk-2.0
%_datadir/themes/HighContrast*/gtk-2.0/gtkrc
%dir %_datadir/themes/HighContrast*/pixmaps
%_datadir/themes/HighContrast*/pixmaps/*.png
%_datadir/themes/HighContrast*/pixmaps/*.xpm
%dir %_datadir/themes/LowContrast*
%dir %_datadir/themes/LowContrast*/gtk-2.0
%_datadir/themes/LowContrast*/gtk-2.0/gtkrc
%dir %_datadir/themes/LowContrast*/pixmaps
%_datadir/themes/LowContrast*/pixmaps/*.png
%_datadir/themes/LowContrast*/pixmaps/*.xpm
%dir %_datadir/themes/LargePrint*
%dir %_datadir/themes/LargePrint*/gtk-2.0
%_datadir/themes/LargePrint*/gtk-2.0/gtkrc
%dir %_datadir/themes/Inverted/gtk-2.0
%_datadir/themes/Inverted/gtk-2.0/gtkrc

%exclude %_datadir/themes/LowContrast/index.theme

%files -n %{theme_prefix}s-accessibility
%_datadir/themes/HighContrast*/index.theme
#%_datadir/themes/HighContrast*/index.theme.disabled
%_datadir/themes/LowContrast/index.theme
%_datadir/themes/LowContrast*/index.theme
%_datadir/themes/LargePrint*/index.theme
%_datadir/themes/Inverted/metacity-1/metacity-theme-1.xml

%files -n %gtk_theme_prefix-ClearlooksClassic
%dir %_datadir/themes/ClearlooksClassic/gtk-2.0
%_datadir/themes/ClearlooksClassic/gtk-2.0/gtkrc

%files -n %gtk_theme_prefix-glider
%dir %_datadir/themes/Glider
%dir %_datadir/themes/Glider/gtk-2.0
%_datadir/themes/Glider/gtk-2.0/gtkrc

%files -n %theme_prefix-glider
%dir %_datadir/themes/Glider/metacity-1
%_datadir/themes/Glider/metacity-1/metacity-theme-1.xml
%_datadir/themes/Glider/index.theme

%files -n %theme_prefix-crux
%_datadir/themes/Crux/index.theme

%files -n %theme_prefix-mist
%dir %_datadir/themes/Mist/metacity-1
%_datadir/themes/Mist/metacity-1/metacity-theme-1.xml
%_datadir/themes/Mist/index.theme

%files -n %theme_prefix-clearlooks
%dir %_datadir/themes/Clearlooks/metacity-1
%_datadir/themes/Clearlooks/metacity-1/metacity-theme-1.xml
%_datadir/themes/Clearlooks/index.theme
# Clearlooks Classic
%dir %_datadir/themes/ClearlooksClassic/metacity-1
%_datadir/themes/ClearlooksClassic/metacity-1/metacity-theme-1.xml

%files -n %gtk_theme_prefix-glossy
%dir %_datadir/themes/Glossy
%dir %_datadir/themes/Glossy/gtk-2.0
%_datadir/themes/Glossy/gtk-2.0/gtkrc

%files -n %theme_prefix-glossy
%dir %_datadir/themes/Glossy/metacity-1
%_datadir/themes/Glossy/metacity-1/metacity-theme-1.xml
%_datadir/themes/Glossy/index.theme

%files -n %gtk_theme_prefix-simple
%dir %_datadir/themes/Simple
%dir %_datadir/themes/Simple/gtk-2.0
%_datadir/themes/Simple/gtk-2.0/gtkrc

%files -n %{icon_theme}s-accessibility
%dir %_iconsdir/HighContrast*
%dir %_iconsdir/HighContrast*/*x*
%dir %_iconsdir/HighContrast*/*x*/*
%_iconsdir/HighContrast*/*x*/*/*.png
%_iconsdir/HighContrast*/*x*/*/*.icon

%dir %_iconsdir/HighContrast-SVG/scalable
%dir %_iconsdir/HighContrast-SVG/scalable/*
%_iconsdir/HighContrast-SVG/scalable/*/*.svg
%dir %_iconsdir/LargePrint
%_iconsdir/LargePrint/index.theme

%files -n %icon_theme-crux
%dir %_iconsdir/Crux
%dir %_iconsdir/Crux/*x*
%dir %_iconsdir/Crux/*x*/*
%_iconsdir/Crux/*x*/*/*.png
%dir %_iconsdir/Crux/scalable
%dir %_iconsdir/Crux/scalable/*
%_iconsdir/Crux/scalable/*/*.svg

%files -n %icon_theme-mist
%dir %_iconsdir/Mist
%dir %_iconsdir/Mist/*x*
%dir %_iconsdir/Mist/*x*/*
%_iconsdir/Mist/*x*/*/*.png
#%_iconsdir/Mist/*x*/*/*.svg
#%dir %_iconsdir/Mist/scalable
#%dir %_iconsdir/Mist/scalable/*
#%_iconsdir/Mist/scalable/*/*.svg
%_iconsdir/Mist/index.theme

%changelog
* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Thu Apr 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Fri Feb 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5

* Thu Jan 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt2
- fixed dependencies for clearlooks* themes
- build all packages as noarch

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3
- packaged Inverted and ClearlooksClassic themes

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Sat Mar 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- fix section %%files

* Wed Dec 05 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- new version (2.20.2)

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager

* Fri Jun 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- updated dependencies
- introduced Glossy theme (maybe a new GNOME default, hah?).

* Tue Oct 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1.1-alt4
- further changes to comply with GTK+/GNOME themes packaging policy:
  + changed icon themes prefix from gnome-icon-theme- to icon-theme-;
  + mentioned directories in the file list that were missing;
  + split GTK+ and GNOME parts of the package with Glider theme;
  + added Provides: metacity-theme to packages that have Metacity themes.
  + split the package with accessibility themes into three: gtk2-themes-,
    icon-themes-, and gnome-themes-;

* Tue Oct 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1.1-alt3
- yet another obsoletes clause.

* Mon Oct 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1.1-alt2
- fixed broken back compatibility on metacity-theme/metacity-themes

* Wed Oct 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1.1-alt1
- new version (2.16.1.1)
- cleaning up the mess between GTK engines, GTK themes, and GNOME themes.
- lowered the case in the packages' names, to maintain uniformity with
  metacity-themes and gtk2-themes.
- now really package Simple theme.
- made filelists more verbose
- revised summaries and descriptions of subpackages.
- the package is noarch now.

* Mon Sep 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- Clarius theme was renamed back to Clearlooks.
- resurrected Simple theme.

* Thu Aug 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91.1-alt1
- new version (2.15.91.1)
- added a subpackage for Clarius, the default theme of GNOME 2.16
- added a subpackage for Mist icon theme; no more Flat-Blue icon theme.

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt2
- upped required version of gtk-engines
- Glider theme now requires Glide engine

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.90-alt1
- new version 2.15.90.
- a great cleanup in upstream; good-bye to Grand Canyon, Sandy, Sandwish, Simple, Smokey, Traditional, Ocean Dream themes.

* Sun Jun 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Mon Mar 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Mon Feb 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version

* Fri Nov 18 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Added a subpackage for the new Clearlooks theme.
- Fixed Provides/Requires for some subpackages.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.94-alt1
- 2.9.94

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92

* Tue Jan 25 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90

* Tue Dec 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Sat Dec 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92
- new gtk-engines-smooth, gtk2-themes-Glider subpackages.

* Tue Jun 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Jun 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0
- Inherits=gnome,hicolor,default.kde for icon themes.

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.92-alt1
- 2.5.92

* Wed Mar 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Thu Sep 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sat May 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2.1-alt1
- 2.3.2.1

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2-alt1
- 2.2

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0-alt1
- 1.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1
- 0.6

* Mon Dec 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt1
- 0.5

* Wed Nov 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- 0.4

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3-alt1
- 0.3

* Tue Oct 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2-alt1
- 0.2

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1-alt1
- First build for Sisyphus.
