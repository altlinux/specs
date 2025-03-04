%define _name alt-panelmode
%define xdg_name org.altlinux.%_name

Name: alt-panelmoded
Version: 0.6.1
Release: alt1

Summary: Used for panelmode on Alt operating systems with GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/Armatik/alt-panelmoded
Vcs: https://gitlab.gnome.org/Armatik/alt-panelmoded
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gee-0.8)

Requires: dconf
Requires: gnome-shell-extensions
Requires: gnome-shell-extension-dash-to-panel
Requires: gnome-shell-extension-arcmenu
Requires: gnome-shell-extension-gtk4-desktop-icons-ng
Requires: gnome-shell-extension-appindicator
Requires: gnome-shell-extension-clipboard-indicator

%description
Used for panelmode on operating systems of the Alt family
with GNOME desktop enviroment.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml

%changelog
* Mon Mar 4 2025 Alexey Volkov <qualimock@altlinux.org> 0.6.1-alt1
- new version 0.6.1

* Sun Feb 23 2025 Alexey Volkov <qualimock@altlinux.org> 0.5.2-alt1
- new version 0.5.2

* Mon Feb 17 2025 Alexey Volkov <qualimock@altlinux.org> 0.5.1-alt1
- new version 0.5.1

* Wed Feb 12 2025 Alexey Volkov <qualimock@altlinux.org> 0.4.3-alt1
- new version 0.4.3

* Mon Feb 10 2025 Alexey Volkov <qualimock@altlinux.org> 0.4.2-alt1
- new version 0.4.2

* Wed Feb 5 2025 Alexey Volkov <qualimock@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Thu Dec 12 2024 Oleg Shchavelev <oleg@altlinux.org> 0.3.3-alt2
- Fix name license

* Thu Dec 12 2024 Oleg Shchavelev <oleg@altlinux.org> 0.3.3-alt1
- Initial build
