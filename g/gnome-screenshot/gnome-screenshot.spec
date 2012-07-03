%define ver_major 3.4

Name: gnome-screenshot
Version: %ver_major.1
Release: alt1

Summary: The GNOME Screenshot Tool
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.31.0

BuildPreReq: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel libcanberra-gtk3-devel libX11-devel libXext-devel
BuildRequires: rpm-build-gnome intltool

%description
GNOME Screenshot Tool makes screenshots from desktop.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/GConf/gsettings/%name.convert
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_man1dir/%name.1.*
%doc NEWS

%changelog
* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Feb 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- first build for Sisyphus

