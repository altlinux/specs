%global uuid ar.xjuan.Cambalache
%define _unpackaged_files_terminate_build 1

%add_python3_req_skip cambalache
%add_python3_req_skip merengue
%add_python3_req_skip merengue.mrg_gtk
%add_python3_req_skip mrg_command

Name: cambalache
Version: 1.0
Release: alt1

Summary: Cambalache is a RAD tool for Gtk 4 and 3 with a clear MVC design and data model first philosophy
# Cambalache is licensed under the LGPLv2 license.
# Tools (in the tools/ directory) are licensed under the GPLv2 license.
# Tools are not installed, so neither will be the GPLv2 license.
License: LGPLv2 AND GPLv2
Group: Development/GNOME and GTK+
Url: https://gitlab.gnome.org/jpu/cambalache

AutoReq: yes nogir

Source0: %name-%version.tar
Patch1: fix_modulesdir.patch

BuildRequires(pre):  rpm-build-python3 rpm-build-gir
BuildRequires:  meson

BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(casilda-1.0)

BuildRequires: python3-module-lxml
BuildRequires: libwebkit2gtk4.1-devel
BuildRequires: libwebkitgtk6.0-devel
BuildRequires: libgtksourceview5-devel
BuildRequires: libgtk4-gir-devel
BuildRequires: libgtk+3-gir-devel
BuildRequires: libadwaita-gir-devel
BuildRequires: libhandy1-gir-devel
BuildRequires: libwebkit2gtk4.1-gir-devel
BuildRequires: libwebkitgtk6.0-gir-devel
BuildRequires: libgtksourceview5-gir-devel

Requires: icon-theme-hicolor
Requires: python3-module-lxml
Requires: python3-module-pygobject3 >= 3.52.0
Requires: libcasilda-gir >= 1.2.1
Requires: libgtk+3-gir >= 3.24.0
Requires: libgtk4-gir >= 4.21.0
Requires: libwebkit2gtk4.1-gir >= 2.48.0
Requires: libwebkitgtk6.0-gir >= 2.48.0
Requires: libgtksourceview5-gir >= 5.16.0
Requires: libhandy1-gir >= 1.8.0
Requires: libadwaita-gir >= 1.7.0
# These typelibs are located in non-standard locations 
# and are shipped together with the cambalache package: 
# libdir/cambalache and libdir/cmb_catalog_gen
%add_typelib_req_skiplist typelib(CambalachePrivate)
%add_typelib_req_skiplist typelib(CmbCatalogUtils)

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
%python3_sitelibdir/%name/
%python3_sitelibdir/cmb_catalog_gen/
%_datadir/metainfo/%uuid.metainfo.xml
%_datadir/applications/%{uuid}.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%uuid.gschema.xml
%_datadir/icons/hicolor/*/apps/*.svg
%_datadir/icons/hicolor/scalable/mimetypes/*.svg
%_datadir/mime/packages/%uuid.mime.xml
%_girdir/*.gir
%_libdir/%name/
%_libdir/cmb_catalog_gen/

%changelog
* Thu Apr 09 2026 Maria Alexeeva <alxvmr@altlinux.org> 1.0-alt1
- Update to 1.0 version.
- Change dependency casilda to libcasilda.

* Wed Apr 09 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.94.1-alt1
- First build
