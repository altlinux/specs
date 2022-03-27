%def_enable snapshot
%define api_ver 0.1
%define gst_api_ver 1.0
%define rdn_name org.entangle_photo.Manager

Name: entangle
Version: 3.0
Release: alt4

Summary: Tethered Camera Control and Capture tool
Group: Graphics
License: GPLv3+
Url: http://entangle-photo.org/

%if_disabled snapshot
Source: http://entangle-photo.org/download/sources/%name-%version.tar.xz
%else
Vcs: https://gitlab.com/entangle/entangle
Source: %name-%version.tar
%endif

Requires: adwaita-icon-theme
Requires: libpeas-python3-loader

%add_python3_path %_libdir/%name/plugins

BuildRequires(pre): meson >= 0.49.0 rpm-build-gir rpm-build-python3
BuildRequires: /proc yelp-tools gtk-doc %_bindir/pod2man
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
%ifarch %e2k
export LD_LIBRARY_PATH=$(pwd)/%__builddir/src/backend:$(pwd)/%__builddir/src/frontend
%endif
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
%_desktopdir/%rdn_name.desktop
%_datadir/metainfo/%rdn_name.metainfo.xml
%_man1dir/%name.1*
%_datadir/glib-2.0/schemas/org.%name-photo.manager.gschema.xml
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
%_typelibdir/Entangle-%api_ver.typelib
%doc README*
%{?_disable_snapshot:%doc AUTHORS NEWS ChangeLog}

# devel, devel-doc
%_datadir/gtk-doc/html/%name/
%exclude %_libdir/libentangle_backend.so
%exclude %_libdir/libentangle_frontend.so
%_girdir/Entangle-%api_ver.gir

%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt4
- updated to v3.0-24-g54795d2 (fixed build with meson >= 0.61)

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt3
- fixed build for %%e2k (ilyakurdyukov@)

* Sat Apr 24 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt2
- updated to v3.0-8-g1debc4b
- updated BR

* Tue Jun 16 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- first build for Sisyphus

