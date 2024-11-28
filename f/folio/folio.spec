%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id com.toolstack.Folio

Name: folio
Version: 24.13
Release: alt1

Summary: A beautiful markdown note-taking app for GNOME
License: GPL-3.0
Group: Office

Url: https://github.com/toolstack/Folio
Vcs: https://github.com/toolstack/Folio
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: gir(GtkSource)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
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
%_datadir/gtksourceview-5/language-specs/markdownpp.lang
%_datadir/gtksourceview-5/styles/%{name}_markdown*.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/dbus-1/services/%app_id.SearchProvider.service
%_datadir/gnome-shell/search-providers/%app_id.SearchProvider-search-provider.ini
%doc README.md

%changelog
* Thu Nov 21 2024 Semen Fomchenkov <armatik@altlinux.org> 24.13-alt1
- Init build for Sisyphus.
