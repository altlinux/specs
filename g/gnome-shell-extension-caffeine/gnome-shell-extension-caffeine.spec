%def_disable snapshot

%define _name caffeine
%define ver_major 54
%define beta %nil
%define uuid %_name@patapon.info
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain gnome-shell-extension-%_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: Enable/Disable auto suspend with quick setting toggle.
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://github.com/eonpatapon/gnome-shell-extension-caffeine

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Vcs: https://github.com/eonpatapon/gnome-shell-extension-caffeine.git
Source: %name-%version%beta.tar
%endif

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1

BuildRequires: /usr/bin/glib-compile-schemas eslint

%description
Enable/Disable auto suspend with quick setting toggle.

%prep
%setup -n %name-%version%beta

%build
./update-locale.sh
glib-compile-schemas --strict --targetdir=caffeine@patapon.info/schemas/ caffeine@patapon.info/schemas

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas,icons}
cp -ar %uuid/{*.js*,preferences,icons} %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a %uuid/schemas/%xdg_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas/
# install locale files
pushd %uuid/locale
for po in *.po; do
    install -d -m 0755 %buildroot%_datadir/locale/${po%.po}/LC_MESSAGES
    msgfmt -o %buildroot%_datadir/locale/${po%.po}/LC_MESSAGES/%gettext_domain.mo $po
done
popd

%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Sun Sep 22 2024 Yuri N. Sedunov <aris@altlinux.org> 54-alt1
- 54

* Tue Sep 17 2024 Yuri N. Sedunov <aris@altlinux.org> 53-alt2
- updated to v53-50-gbe10165 (shell-47 supported)

* Tue Mar 26 2024 Yuri N. Sedunov <aris@altlinux.org> 53-alt1
- 53

* Thu Sep 21 2023 Yuri N. Sedunov <aris@altlinux.org> 50-alt1.1
- packaged lost translations

* Thu Sep 21 2023 Yuri N. Sedunov <aris@altlinux.org> 50-alt1
- 50

* Thu May 04 2023 Yuri N. Sedunov <aris@altlinux.org> 48-alt1
- 48

* Thu Apr 20 2023 Yuri N. Sedunov <aris@altlinux.org> 47-alt1
- 47

* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 46-alt1
- first build for Sisyphus (v46-7-gd835bae)

