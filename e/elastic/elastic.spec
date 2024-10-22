%define APP_ID app.drey.Elastic
%def_enable check

Name: elastic
Version: 0.1.6
Release: alt1

Summary: Design spring animations
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/elastic
Vcs: https://gitlab.gnome.org/World/elastic
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(template-glib-1.0)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

%description
Elastic allows to design and export spring physics-based animations to use
with libadwaita.

Features:

* Preview translation, rotation and scaling transformations.
* See the animation curve and duration on a graph.
* Drag a handle to see it return back with the spring physics.
* Export C, JavaScript, Python, Vala or Rust code.

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
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/icons/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Tue Oct 22 2024 Oleg Shchavelev <oleg@altlinux.org> 0.1.6-alt1
- Initial build
