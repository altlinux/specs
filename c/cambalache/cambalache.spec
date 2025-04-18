%global uuid ar.xjuan.Cambalache

%add_python3_req_skip cambalache
%add_python3_req_skip merengue
%add_python3_req_skip merengue.mrg_gtk

Name: cambalache
Version: 0.94.1
Release: alt1

Summary: Cambalache is a RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy
# Cambalache is licensed under the LGPLv2 license.
# Tools (in the tools/ directory) are licensed under the GPLv2 license.
# Tools are not installed, so neither will be the GPLv2 license.
License: LGPLv2 AND GPLv2
Group: Development/GNOME and GTK+
Url: https://gitlab.gnome.org/jpu/cambalache

Source0: %name-%version.tar
Patch1: fix_modulesdir.patch

BuildRequires(pre):  rpm-build-python3
BuildRequires:  meson
BuildRequires:  libgtk4-devel
BuildRequires:  libgtk+3-devel

BuildRequires: python3-module-lxml
BuildRequires: python3-module-pygobject3-devel
BuildRequires: libwebkit2gtk4.1-devel
BuildRequires: libwebkitgtk6.0-devel
BuildRequires: libhandy1-devel
BuildRequires: libadwaita-devel
BuildRequires: libgtksourceview5-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libgtk4-gir-devel
BuildRequires: libwebkit2gtk4.1-gir-devel
BuildRequires: libwebkitgtk6.0-gir-devel
BuildRequires: libgtksourceview5-gir-devel
BuildRequires: libhandy1-gir-devel
BuildRequires: libadwaita-gir-devel
BuildRequires: casilda-devel

Requires: icon-theme-hicolor
Requires: python3-module-lxml
Requires: python3-module-pygobject3
Requires: libgtk+3-gir
Requires: libgtk4-gir
Requires: libwebkit2gtk4.1-gir
Requires: libwebkitgtk6.0-gir
Requires: libgtksourceview5-gir
Requires: libhandy1-gir
Requires: libadwaita-gir
Requires: casilda

%description
Cambalache is a new RAD tool for Gtk 4 and 3 with a clear MVC design and data
model first philosophy. This translates to a wide feature coverage with
minimal/none developer intervention for basic support.

To support multiple Gtk versions it renders the workspace out of process using
the Gdk broadway backend.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%_bindir/%name
%_bindir/cmb-catalog-gen
%_libdir/girepository-1.0/*
%_libdir/*.so
%python3_sitelibdir/%name/
%python3_sitelibdir/cmb_catalog_gen/
%_datadir/metainfo/%uuid.metainfo.xml
%_datadir/applications/%{uuid}.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%uuid.gschema.xml
%_datadir/icons/hicolor/*/apps/*.svg
%_datadir/icons/hicolor/scalable/mimetypes/*.svg
%_datadir/mime/packages/%uuid.mime.xml
%_girdir/

%changelog
* Wed Apr 09 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.94.1-alt1
- First build
