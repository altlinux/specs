%def_disable snapshot

%define ver_major 64
%define beta %nil
%define uuid appindicatorsupport@rgcjonas.gmail.com
%define xdg_name org.gnome.shell.extensions.appindicator
%define gettext_domain AppIndicatorExtension

%def_disable check

Name: gnome-shell-extension-appindicator
Version: %ver_major
Release: alt1

Summary: AppIndicator, KStatusNotifierItem and legacy Tray icons extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://github.com/ubuntu/gnome-shell-extension-appindicator

Vcs: https://github.com/ubuntu/gnome-shell-extension-appindicator.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

Requires: gnome-shell >= 45
Requires: typelib(Gtk) = 4.0
Requires: typelib(AyatanaAppIndicator3)

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson /usr/bin/glib-compile-schemas jq eslint
%{?_enable_check:BuildRequires: %_bindir/gjs typelib(Gtk) = 4.0}

%description
This extension integrates AppIndicators and KStatusNotifierItems
into GNOME Shell, including support for legacy tray icons.

%prep
%setup -n %name-%version%beta

%build
%meson -Dlocal_install=disabled
%meson_build

%install
%meson_install
%find_lang %gettext_domain

%check
%__meson_test

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc AUTHORS.md README.md

%changelog
* Sat Mar 21 2026 Yuri N. Sedunov <aris@altlinux.org> 64-alt1
- 64

* Fri Feb 13 2026 Yuri N. Sedunov <aris@altlinux.org> 63-alt1
- 63 (GNOME 50 supported)

* Thu Sep 18 2025 Yuri N. Sedunov <aris@altlinux.org> 61-alt1
- 61 (GNOME 49 supported)

* Wed May 07 2025 Yuri N. Sedunov <aris@altlinux.org> 60-alt1
- 60

* Mon Mar 17 2025 Yuri N. Sedunov <aris@altlinux.org> 59-alt2
- applied fix for GNOME 48.

* Tue Aug 06 2024 Yuri N. Sedunov <aris@altlinux.org> 59-alt1
- 59

* Fri Apr 19 2024 Yuri N. Sedunov <aris@altlinux.org> 58-alt1
- 58

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 57-alt2
- updated to v57-5-g03a7412 (gnome-46 support)

* Fri Aug 18 2023 Yuri N. Sedunov <aris@altlinux.org> 57-alt1
- 57

* Sat Mar 25 2023 Yuri N. Sedunov <aris@altlinux.org> 53-alt1
- first build for Sisyphus

