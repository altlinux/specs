%def_disable snapshot
%define _name nautilus
%define _libexecdir %_prefix/libexec
%define ver_major 42
%define beta %nil
%define api_ver 3.0
%define xdg_name org.gnome.Nautilus

%def_disable packagekit
%def_disable introspection
%def_disable selinux
%def_disable docs
%def_disable check

Name: lib%_name-extension-compat
Version: %ver_major.5
Release: alt1%beta

Summary: Nautilus extension library
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Nautilus

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version.tar
%endif
Patch: nautilus-42.5-alt-libnautilus-extension-only.patch

%define icon_theme_ver 2.10.0
%define desktop_file_utils_ver 0.8
%define glib_ver 2.70
%define desktop_ver 3.3.3
%define pango_ver 1.28.3
%define gtk_ver 3.22.27
%define libxml2_ver 2.7.8
%define gexiv2_ver 0.14
%define gir_ver 0.10.2
%define tracker_ver 2.99.2
%define autoar_ver 0.4
%define portal_ver 0.5
%define handy_ver 1.5.0
%define selinux_ver 2.0

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson desktop-file-utils >= %desktop_file_utils_ver
BuildRequires: libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libgexiv2-devel >= %gexiv2_ver
BuildRequires: libgnome-autoar-devel >= %autoar_ver
BuildRequires: libX11-devel
BuildRequires: libseccomp-devel
BuildRequires: pkgconfig(gstreamer-tag-1.0) pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: libportal-gtk3-devel >= %portal_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
%{?_enable_docs:BuildRequires: docbook-utils gtk-doc}
BuildRequires: pkgconfig(tracker-sparql-3.0) tracker3-sandbox
%{?_enable_introspection:
BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel >= %selinux_ver}
%{?_enable_check:
BuildRequires(pre): rpm-build-python3
BuildRequires: xvfb-run dbus-tools-gui /proc}

%description
This package contains libnautilus-extension from Nautilus < 43.

%package devel
Summary: Libraries and include files for developing Nautilus components
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description devel
This package provides the necessary development libraries and include
files to allow you to build packages against old libnautilus-extension
library.

%prep
%setup -n %_name-%version%beta
%patch
sed -i 's|\(#\!/usr/bin/env python\)|\13|' test/interactive/*.py

%build
%meson \
    %{?_enable_docs:-Ddocs=true} \
    %{?_disable_packagekit:-Dpackagekit=false} \
    %{?_disable_introspection:-Dintrospection=false} \
    -Dextensions=false \
    -Dtests=none \
    %{?_enable_selinux:-Dselinux=true}
%meson_build

%install
%meson_install

%files
%_libdir/libnautilus-extension.so.*

#%files devel
#%_includedir/*
#%_libdir/*.so
#%_pkgconfigdir/*

%changelog
* Fri Sep 23 2022 Yuri N. Sedunov <aris@altlinux.org> 42.5-alt1
- first build for Sisyphus

