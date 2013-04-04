%define ver_major 3.8

Name: gnome-clocks
Version: %ver_major.0
Release: alt1

Summary: Clock application designed for GNOME 3
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/GnomeClocks

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: intltool
BuildRequires: libgio-devel libgtk+3-devel libnotify-devel
BuildRequires: libcanberra-gtk3-devel libgweather-devel libgnome-desktop3-devel
BuildRequires: vala-tools gobject-introspection-devel libgtk+3-gir-devel

%description
Clock application designed for GNOME 3

%prep
%setup

%build
%autoreconf
%configure \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%name.desktop
%_datadir/icons/*/*/apps/%name.png
%_datadir/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%doc README NEWS

%changelog
* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Feb 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- first build for Sisyphus

