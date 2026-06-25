%define _unpackaged_files_terminate_build 1
%define app_id com.odnoyko.valot

Name: valot
Version: 0.9.3
Release: alt1

Summary: A modern time tracking application built with GTK4 and Adwaita.
License: MIT
Group: Office
Url: https://gitlab.com/Valo27/valot
Vcs: https://gitlab.com/Valo27/valot

Source: %name-%version.tar

Requires: libgjs
Requires: typelib(Adw) = 1
Requires: typelib(Gda) = 6.0
Requires: libgda6-providers

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gtk-doc
BuildRequires: libgjs-devel
BuildRequires: blueprint-compiler

%description
Valot is designed for developers, freelancers, and professionals.
It offers a modern interface that follows GNOME Human Interface Guidelines.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%app_id
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{app_id}*.svg
%_iconsdir/hicolor/scalable/plugins/plugin_unavaible_icon.svg
%_datadir/%name/
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/%app_id/screenshots/*.png
%doc README*

%changelog
* Wed Jun 24 2026 Pavel Mitrofanov <cobalt@altlinux.org> 0.9.3-alt1
- Update to newest version.

* Mon Oct 27 2025 Pavel Mitrofanov <cobalt@altlinux.org> 0.8.4-alt2
- Changed summary to comply with upstream.

* Thu Oct 16 2025 Pavel Mitrofanov <cobalt@altlinux.org> 0.8.4-alt1
- Initial commit.
