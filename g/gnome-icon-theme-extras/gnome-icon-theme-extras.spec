%define ver_major 3.4

Name: gnome-icon-theme-extras
Version: %ver_major.0
Release: alt1

Summary: Extra GNOME icons for specific devices and file types
License: Creative Commons Attribution-Share Alike 3.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define icon_naming_utils_ver 0.8.7

Requires: icon-naming-utils >= %icon_naming_utils_ver

# From configure.in
BuildPreReq: intltool >= 0.40.0
BuildPreReq: pkgconfig >= 0.19
BuildPreReq: icon-naming-utils >= %icon_naming_utils_ver
BuildRequires: perl-XML-Parser

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

* Thu Apr 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- first build for Sisyphus




