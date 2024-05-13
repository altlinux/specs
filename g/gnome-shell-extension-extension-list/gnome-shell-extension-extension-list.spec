%def_enable snapshot

%define _name extension-list
%define ver_major 46
%define beta %nil
%define uuid %_name@tu.berry
%define xdg_name org.gnome.shell.extensions.%_name

%define ego 3088/%_name
# EGO=3088/extension-list sh cli/get-version.sh
%define ego_ver 36

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major.1
Release: alt1%beta

%define gettext_domain %name

Summary: Simple GNOME Shell extension manager
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/tuberry/extension-list

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/%version%beta/%name-%version%beta.tar.gz
%else
Vcs: https://github.com/tuberry/extension-list.git
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= %ver_major
Requires: typelib(Adw) = 1 typelib(Soup) = 3.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson /usr/bin/glib-compile-schemas sassc

%description
Simple GNOME Shell extension manager in the top panel.

%prep
%setup -n %_name-%version%beta

%build
%meson \
    -Dtarget=system \
    -Dversion=%ego_ver
%nil
%meson_build

%install
%meson_install
%find_lang %gettext_domain

%check
%__meson_test

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Mon May 13 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 46-alt0.5.beta
- 46.beta

* Thu Sep 21 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Wed Sep 13 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt0.5.beta
- 45.beta

* Mon Mar 27 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- first build for Sisyphus


