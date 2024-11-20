%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id io.github.lainsce.Notejot

Name: notejot
Version: 3.5.1
Release: alt1

Summary: Jot your ideas
License: GPL-3.0-or-later
Group: Office

Url: https://github.com/lainsce/notejot
Vcs: https://github.com/lainsce/notejot
Source: %name-%version.tar

Patch: notejot-3.5.1-alt-vala-equality-operation-fix.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gee-0.8)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
A stupidly-simple notes application for any type of short term notes or ideas.

* Color your notes in 8 different colors
* Classify them in notebooks
* Format text to your liking
* Pin your most important ones

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_datadir/locale/*/*/%app_id.mo
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%doc README.md

%changelog
* Sun Oct 27 2024 Semen Fomchenkov <armatik@altlinux.org> 3.5.1-alt1
- Init build for Sisyphus.
