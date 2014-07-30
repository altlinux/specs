%define _name adwaita-icon-theme
%define ver_major 3.13

Name: icon-theme-adwaita
Version: %ver_major.4
Release: alt1

Summary: Adwaita icon theme
License: Creative Commons Attribution-Share Alike 3.0
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides: %_name = %version-%release
Conflicts: gnome-theme-standard < 3.13.0

Requires: icon-naming-utils
BuildRequires: intltool icon-naming-utils gtk-update-icon-cache

%description
Adwaita icon theme for GTK+.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %_name

%files -f %_name.lang
%_iconsdir/Adwaita/*
%_datadir/pkgconfig/%_name.pc
%doc AUTHORS README NEWS COPYING

%changelog
* Wed Jul 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.13.4-alt1
- first build for Sisyphus

