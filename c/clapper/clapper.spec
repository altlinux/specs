%def_disable snapshot

%define ver_major 0.6
%define api_ver 0.0
%define rdn_name com.github.rafostar.Clapper

%def_enable check

Name: clapper
Version: %ver_major.0
Release: alt1

Summary: Clapper is a GNOME media player
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/Rafostar/clapper

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/Rafostar/clapper.git
Source: %name-%version.tar
%endif

%define glib_ver 2.76
%define gtk_ver 4.10
%define adw_ver 1.4.0
%define gst_ver 1.20

Requires: lib%name = %EVR
Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver
Requires: gst-libav
Requires: gstreamer-vaapi

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gcc-c++ vala-tools
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-gl-1.0)
BuildRequires: pkgconfig(gstreamer-gl-prototypes-1.0)
BuildRequires: pkgconfig(gstreamer-gl-wayland-1.0)
BuildRequires: pkgconfig(gstreamer-gl-egl-1.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: gobject-introspection-devel
BuildRequires: gir(Gtk) = 4.0
BuildRequires: gir(Gst) gir(GstAudio) gir(GstBase)
BuildRequires: gir(GstPbutils) gir(GstTag) gir(GstVideo)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
A GNOME media player built using GJS with GTK4 toolkit and powered by
GStreamer with OpenGL rendering.

%package -n lib%name
Summary: Clapper shared libraries
Group: System/Libraries

%description -n lib%name
This package provides Clapper shared libraries.

%package -n lib%name-devel
Summary: Clapper shared libraries
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides development files for Clapper libraries.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
# some libraries linked against gstreamer module
ln -s gstreamer-1.0/libgst%name.so %buildroot%_libdir/libgst%name.so

%find_lang --output=%name.lang %name-app %name-gtk

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name-%api_ver
%dir %_libdir/%name-%api_ver/gst
%dir %_libdir/%name-%api_ver/gst/plugin
%dir %_libdir/%name-%api_ver/gst/plugin/importers
%_libdir/%name-%api_ver/gst/plugin/importers/libgst%{name}glimporter.so
%_libdir/%name-%api_ver/gst/plugin/importers/libgst%{name}gluploader.so
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/mime/packages/%rdn_name.xml
%doc README*

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*
%_libdir/lib%name-gtk-%api_ver.so.*
%_libdir/libgst%{name}glcontexthandler.so.*
%_libdir/gstreamer-1.0/libgst%name.so
# symlink
%_libdir/libgst%name.so
%_typelibdir/Clapper-%api_ver.typelib
%_typelibdir/ClapperGtk-%api_ver.typelib

%files -n lib%name-devel
%dir %_includedir/%name-%api_ver/
%_includedir/%name-%api_ver/%name
%_includedir/%name-%api_ver/%name-gtk
%_libdir/lib%name-%api_ver.so
%_libdir/lib%name-gtk-%api_ver.so
%_libdir/libgst%{name}glcontexthandler.so
%_pkgconfigdir/%name-%api_ver.pc
%_pkgconfigdir/%name-gtk-%api_ver.pc
%_girdir/Clapper-%api_ver.gir
%_girdir/ClapperGtk-%api_ver.gir
%_vapidir/%name-%api_ver.*
%_vapidir/%name-gtk-%api_ver.*

%changelog
* Tue Apr 23 2024 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Fri Oct 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- first build for Sisyphus (0.5.2-47-gb4aaea1)


