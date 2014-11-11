%define ver_major 3.14

Name: gnome-themes-standard
Version: %ver_major.2
Release: alt1

Summary: A set of standard themes for GNOME desktop
License: LGPLv2.1+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Obsoletes: gtk2-themes-accessibility
Provides: gtk2-themes-accessibility = %version-%release
Obsoletes: icon-themes-accessibility
Provides: icon-themes-accessibility = %version-%release
Obsoletes: gnome-themes-accessibility
Provides: gnome-themes-accessibility = %version-%release

Requires: %name-data = %version-%release

%define theme_prefix gnome-theme
BuildPreReq: intltool >= 0.35.0
BuildRequires: libgtk+3-devel >= 3.13.4 libgtk+2-devel librsvg-devel

%description
This package provides a set of standard GTK+-(2/3) themes, engines,
metacity themes, backgrounds for GNOME 3 desktop.

%package data
Summary: Arch-independent data for %name
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-icon-theme >= 3.0.0
# for gtk2 themes
Requires: libgtk-engine-hc
Requires: gtk2-theme-clearlooks

%description data
This package provides an Arch-independent part of %name.

%package -n libgtk2-engine-adwaita
Summary: GTK+2 theme engine Adwaita
Group: Graphical desktop/GNOME

%description -n libgtk2-engine-adwaita
This package provides a GTK+2 theme engine Adwaita.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files
%files data -f %name.lang
%dir %_datadir/themes/Adwaita
%_datadir/themes/Adwaita/index.theme
%_datadir/themes/Adwaita/metacity-1/
%dir %_datadir/themes/Adwaita/gtk-2.0
%_datadir/themes/Adwaita/gtk-2.0/gtkrc
%_datadir/themes/Adwaita/gtk-2.0/Arrows/
%_datadir/themes/Adwaita/gtk-2.0/Buttons/
%_datadir/themes/Adwaita/gtk-2.0/Check-Radio/
%_datadir/themes/Adwaita/gtk-2.0/Entry/
%_datadir/themes/Adwaita/gtk-2.0/Expanders/
%_datadir/themes/Adwaita/gtk-2.0/Handles/
%_datadir/themes/Adwaita/gtk-2.0/Lines/
%_datadir/themes/Adwaita/gtk-2.0/Menu-Menubar/
%_datadir/themes/Adwaita/gtk-2.0/Others/
%_datadir/themes/Adwaita/gtk-2.0/ProgressBar/
%_datadir/themes/Adwaita/gtk-2.0/Range/
%_datadir/themes/Adwaita/gtk-2.0/Scrollbars/
%_datadir/themes/Adwaita/gtk-2.0/Shadows/
%_datadir/themes/Adwaita/gtk-2.0/Spin/
%_datadir/themes/Adwaita/gtk-2.0/Tabs/
%_datadir/themes/Adwaita/gtk-2.0/Toolbar/
%dir %_datadir/themes/Adwaita/gtk-3.0
%_datadir/themes/Adwaita/gtk-3.0/gtk.css

# Accessibility themes from ghome-temes(-default)
%_datadir/themes/HighContrast/gtk-2.0/gtkrc
%_datadir/themes/HighContrast/gtk-3.0/gtk.css
%_datadir/themes/HighContrast/gtk-3.0/gtk.gresource
%_datadir/themes/HighContrast/index.theme
%_datadir/themes/HighContrast/gtk-3.0/settings.ini
%_iconsdir/HighContrast/
# metacity theme
%_datadir/themes/HighContrast/metacity-1/metacity-theme-3.xml
%doc NEWS README

%files -n libgtk2-engine-adwaita
%_libdir/gtk-2.0/2.10.0/engines/libadwaita.so
%exclude %_libdir/gtk-2.0/2.10.0/engines/libadwaita.la

%changelog
* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sat Sep 07 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sun Jul 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.4

* Tue Jul 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Feb 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.5-alt1
- 3.6.5

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1
- new libgtk2-engine-adwaita subpackage

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.2-alt1
- 3.6.0.2

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Mar 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Wed Jan 19 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Fri Dec 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.91.4-alt1
- first build for Sisyphus

