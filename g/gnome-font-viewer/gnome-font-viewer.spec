%define ver_major 3.4

Name: gnome-font-viewer
Version: %ver_major.0
Release: alt1

Summary: The GNOME Font Viewer
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.30.0
%define gtk_ver 3.0.0

BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libfreetype-devel intltool gnome-doc-utils rpm-build-gnome

%description
GNOME Font Viewer is a simple application to preview fonts.

%prep
%setup

%build
%configure \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/gnome-thumbnail-font
%_datadir/applications/%name.desktop
%_datadir/thumbnailers/%name.thumbnailer
%doc NEWS

%changelog
* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

