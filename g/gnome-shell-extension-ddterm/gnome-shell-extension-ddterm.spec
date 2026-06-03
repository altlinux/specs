%def_disable snapshot

%define _name ddterm
%define ver_major 63
%define beta %nil
# too many names since 63.0.1
%define uuid %_name@amezin.github.com
%define rdn_name com.github.amezin.%_name
%define xdg_name org.gnome.shell.extensions.%_name
%define gti_ver a4fd1ce4

%def_enable check

%def_disable bootstrap

Name: gnome-shell-extension-%_name
Version: %ver_major.1.0
Release: alt1%beta

%define gettext_domain %name

Summary: Drop Down Terminal Extension for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/ddterm/gnome-shell-extension-ddterm

Vcs: https://github.com/ddterm/gnome-shell-extension-ddterm.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif
# https://github.com/ddterm/gjs-typelib-installer.git
Source1: gjs-typelib-installer-%gti_ver.tar

%define meson_ver 1.8.0

Requires: gnome-shell >= 47
Requires: typelib(Adw) = 1 typelib(Vte) = 3.91
Requires: typelib(GnomeDesktop)

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson >= %meson_ver xvfb-run
BuildRequires: /usr/bin/gjs
BuildRequires: /usr/bin/gtk-builder-tool /usr/bin/gtk4-builder-tool
BuildRequires: /usr/bin/glib-compile-schemas /usr/bin/gapplication xsltproc
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli}

%description
%summary

%prep
%setup -n %name-%version%beta -a1
mv gjs-typelib-installer-%gti_ver subprojects/gjs-typelib-installer

%build
%meson
xvfb-run %meson_build

%install
%meson_install
%find_lang %gettext_domain

%check
xvfb-run %__meson_test

%files -f %gettext_domain.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README* CHANGELOG*

%changelog
* Wed Jun 03 2026 Yuri N. Sedunov <aris@altlinux.org> 63.1.0-alt1
- 63.1.0

* Tue May 12 2026 Yuri N. Sedunov <aris@altlinux.org> 63.0.1-alt1
- 63.0.1

* Mon Apr 27 2026 Yuri N. Sedunov <aris@altlinux.org> 63.0.0-alt1
- 63.0.0 (GNOME 50 supported)

* Wed Sep 24 2025 Yuri N. Sedunov <aris@altlinux.org> 62.0.0-alt1
- 62.0.0

* Wed May 07 2025 Yuri N. Sedunov <aris@altlinux.org> 61-alt1
- 61
- spec cleanup (ALT #54094)

* Tue Apr 29 2025 Yuri N. Sedunov <aris@altlinux.org> 60-alt1
- 60

* Mon Mar 17 2025 Yuri N. Sedunov <aris@altlinux.org> 59-alt1
- 59 (GNOME 48 supported)

* Sun Jan 19 2025 Yuri N. Sedunov <aris@altlinux.org> 58-alt1
- 58

* Sun Jan 12 2025 Yuri N. Sedunov <aris@altlinux.org> 57-alt1
- 57

* Tue Jan 07 2025 Yuri N. Sedunov <aris@altlinux.org> 56-alt1
- 56

* Thu Nov 28 2024 Yuri N. Sedunov <aris@altlinux.org> 55-alt0.9
- first build for Sisyphus


