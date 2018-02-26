%define ver_major 3.4

Name: gnome-icon-theme-symbolic
Version: %ver_major.0
Release: alt1

Summary: Additional set of icons for GNOME desktop
License: Creative Commons Attribution-Share Alike 3.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define icon_naming_utils_ver 0.8.7

Requires: icon-naming-utils >= %icon_naming_utils_ver

# From configure.in
BuildPreReq: intltool >= 0.40.0 perl-XML-Parser
BuildPreReq: pkgconfig >= 0.19
BuildPreReq: icon-naming-utils >= %icon_naming_utils_ver
BuildRequires: gtk-update-icon-cache git-core inkscape

%description
Purpose of this icon theme is to extend the base icon theme that follows
the Tango style guidelines for specific purposes. This would include OSD
messages, panel system/notification area, and possibly menu icons.

Icons follow the naming specification, but have a -symbolic suffix, so
only applications specifically looking up these symbolic icons will
render them. If a -symbolic icon is missing, the app will fall back to
the regular name.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_iconsdir/gnome/*
%doc AUTHORS README NEWS COPYING

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91.1-alt1
- 3.3.91.1

* Wed Jan 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

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

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- first build for Sisyphus





