%define APP_ID app.devsuite.Schemes
%def_enable check

Name: schemes
Version: 46.0
Release: alt1

Summary: Create syntax highlighting schemes
License: GPL-3.0-or-later
Group: Development/GNOME and GTK+

Url: https://gitlab.gnome.org/chergert/schemes
Vcs: https://gitlab.gnome.org/chergert/schemes
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(libpanel-1)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstream-util
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Schemes allow you to create syntax highlighting style-schemes
for GtkSourceView-based applications such as Builder
or Text Editor.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.appdata.xml

%changelog
* Wed Oct 16 2024 Oleg Shchavelev <oleg@altlinux.org> 46.0-alt1
- Initial build
