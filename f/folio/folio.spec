%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id com.toolstack.Folio

Name: folio
Version: 25.01
Release: alt1

Summary: A beautiful markdown note-taking app for GNOME
License: GPL-3.0
Group: Office
Url: https://github.com/toolstack/Folio

Vcs: https://github.com/toolstack/Folio

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define gtksource_api_ver 5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtksourceview-%gtksource_api_ver)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: gir(GtkSource) = %gtksource_api_ver
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas
%endif

%description
Create notebooks and take notes in markdown

Some features include:

* Almost WYSIWYG markdown rendering
* Searchable through GNOME search
* Highlight and strikethrough text formatting
* App themeing based on notebook color
* Trash can
* Markdown document
* Optional line numbers
* Optional auto save
* Open links with Control-Click
* Link to other notes in Folio
* Automatically create links for bare URL's and e-mail addresses

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %app_id

%check
%meson_test

%files -f %app_id.lang
%_bindir/%app_id
%_bindir/%name-search-provider
%_desktopdir/%app_id.desktop
%_desktopdir/%app_id-editor.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.appdata.xml
%_datadir/gtksourceview-%gtksource_api_ver/language-specs/markdownpp.lang
%_datadir/gtksourceview-%gtksource_api_ver/styles/%{name}_markdown*.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/dbus-1/services/%app_id.SearchProvider.service
%_datadir/gnome-shell/search-providers/%app_id.SearchProvider-search-provider.ini
%doc README.md

%changelog
* Sat Feb 15 2025 Yuri N. Sedunov <aris@altlinux.org> 25.01-alt1
- updated to 25.01-3-ge6720c8

* Wed Feb 05 2025 Yuri N. Sedunov <aris@altlinux.org> 24.14-alt1.1
- explicitly BR "gir(GtkSource) = 5"

* Sun Nov 24 2024 Semen Fomchenkov <armatik@altlinux.org> 24.14-alt1
- 24.14

* Thu Nov 21 2024 Semen Fomchenkov <armatik@altlinux.org> 24.13-alt1
- Init build for Sisyphus.
