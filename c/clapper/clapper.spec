%def_enable snapshot

%define ver_major 0.5
%define api_ver 1.0
%define rdn_name com.github.rafostar.Clapper

%def_enable check

Name: clapper
Version: %ver_major.2
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

%set_typelibdir %_libdir/%rdn_name

%define glib_ver 2.76
%define gtk_ver 4.10
%define gst_ver 1.20

Requires: /usr/bin/gjs
Requires: typelib(Adw) = 1 typelib(Soup) = 3.0
Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver
Requires: gstreamer-vaapi

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gcc-c++ /usr/bin/gjs
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
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
BuildRequires: gir(Gst) gir(GstAudio) gir(GstBase)
BuildRequires: gir(GstPbutils) gir(GstTag) gir(GstVideo)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
A GNOME media player built using GJS with GTK4 toolkit and powered by
GStreamer with OpenGL rendering.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
# some libraries linked against gstreamer module
ln -s gstreamer-1.0/libgst%name.so %buildroot%_libdir/libgst%name.so

%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%name
%_bindir/%rdn_name
%_libdir/libgst%{name}glcontexthandler.so.*
%_libdir/%name-%api_ver/
%_libdir/%rdn_name/
%_libdir/gstreamer-1.0/libgst%name.so
# symlink
%_libdir/libgst%name.so
%_desktopdir/%rdn_name.desktop
%_datadir/%rdn_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/mime/packages/%rdn_name.xml
%doc README*

%exclude %_libdir/libgst%{name}glcontexthandler.so
%exclude %_girdir/GstClapper-%api_ver.gir

%changelog
* Fri Oct 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- first build for Sisyphus (0.5.2-47-gb4aaea1)


