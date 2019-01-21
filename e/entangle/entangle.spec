%define api_ver 0.1
%define gst_api_ver 1.0

Name: entangle
Version: 2.0
Release: alt1

Summary: Tethered Camera Control and Capture tool
Group: Graphics
License: GPLv3+
Url: http://entangle-photo.org/

#VCS: https://gitlab.com/entangle/entangle
Source: http://entangle-photo.org/download/sources/%name-%version.tar.xz

Requires: adwaita-icon-theme
Requires: libpeas-python3-loader

%add_python3_path %_libdir/%name/plugins

BuildRequires(pre): meson >= 0.41.0 rpm-build-gir rpm-build-python3
BuildRequires: yelp-tools gtk-doc perl-podlators
BuildRequires: glib2-devel >= 2.38.0
BuildRequires: libgtk+3-devel >= 3.22.0
BuildRequires: libgphoto2-devel >= 2.5.0
BuildRequires: libgudev-devel >= 145
BuildRequires: liblcms2-devel >= 2.0
BuildRequires: libpeas-devel >= 1.2.0
BuildRequires: libgexiv2-devel >= 0.10
BuildRequires: libX11-devel libXext-devel
BuildRequires: libraw-devel >= 0.9.0
BuildRequires: gstreamer%gst_api_ver-devel
BuildRequires: gst-plugins%gst_api_ver-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk+3-gir-devel libpeas-gir-devel
BuildRequires: libgexiv2-gir-devel libgstreamer%gst_api_ver-gir-devel

%description
Entangle is an application which uses GTK and libgphoto2 to provide a
graphical interface for tethered photography with digital cameras.

It includes control over camera shooting and configuration settings
and 'hands off' shooting directly from the controlling computer.

%prep
%setup

%build
%meson -Denable-gtk-doc=true
%meson_build -j 1

%install
%meson_install
%find_lang  --with-gnome %name

%files -f %name.lang
%_libdir/lib%{name}_backend.so.*
%_libdir/lib%{name}_frontend.so.*
%dir %_libdir/%name
%_libdir/%name/plugins/
%_datadir/%name/
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1*
%_datadir/glib-2.0/schemas/org.%name-photo.manager.gschema.xml
%_iconsdir/hicolor/*/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_typelibdir/Entangle-%api_ver.typelib
%doc README AUTHORS NEWS ChangeLog

# devel, devel-doc
%_datadir/gtk-doc/html/%name/
%exclude %_libdir/libentangle_backend.so
%exclude %_libdir/libentangle_frontend.so
%_girdir/Entangle-%api_ver.gir

%changelog
* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- first build for Sisyphus

