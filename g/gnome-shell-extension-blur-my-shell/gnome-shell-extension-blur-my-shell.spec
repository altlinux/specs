%def_disable snapshot

%define _name blur-my-shell
%define ver_major 66
%define beta %nil
%define uuid %_name@aunetx
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %uuid

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: GNOME Shell Extension - Blur my Shell
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/aunetx/blur-my-shell

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Vcs: https://github.com/aunetx/blur-my-shell.git
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 46
Requires: typelib(Adw) = 1

BuildRequires: /usr/bin/glib-compile-schemas

%description
A GNOME Shell extension that adds a blur look to different parts of the
GNOME Shell, including the top panel, dash and overview.

%prep
%setup -n %_name-%version%beta

%build
#%make VERSION=%version

%install
# install main extension files
install -d -m 0755 %buildroot%_datadir/gnome-shell/extensions
cp -p -r src %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -p -r resources/ui %buildroot%_datadir/gnome-shell/extensions/%uuid/ui
cp -p -r resources/icons %buildroot%_datadir/icons
install -D -p -m 0644 metadata.json %buildroot%_datadir/gnome-shell/extensions/%uuid/metadata.json

# install the schema file
install -D -p -m 0644 \
    schemas/%xdg_name.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml

# install locale files
pushd po
for po in *.po; do
    install -d -m 0755 %buildroot%_datadir/locale/${po%.po}/LC_MESSAGES
    msgfmt -o %buildroot%_datadir/locale/${po%.po}/LC_MESSAGES/%gettext_domain.mo $po
done
popd

%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/scalable/actions/*.svg
%doc README.md

%changelog
* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 66-alt1
- 66

* Tue Aug 20 2024 Yuri N. Sedunov <aris@altlinux.org> 65-alt1
- 65

* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 64-alt1
- 64

* Mon May 27 2024 Yuri N. Sedunov <aris@altlinux.org> 62-alt1
- 62

* Tue Apr 23 2024 Yuri N. Sedunov <aris@altlinux.org> 61-alt1
- 61

* Thu Apr 11 2024 Yuri N. Sedunov <aris@altlinux.org> 60-alt1
- 60

* Tue Mar 26 2024 Yuri N. Sedunov <aris@altlinux.org> 59-alt1
- 59

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 57-alt1
- 57

* Wed Mar 06 2024 Yuri N. Sedunov <aris@altlinux.org> 56-alt1
- 56

* Mon Feb 19 2024 Yuri N. Sedunov <aris@altlinux.org> 55-alt1
- 55

* Thu Nov 09 2023 Yuri N. Sedunov <aris@altlinux.org> 54-alt1
- 54

* Sat Nov 04 2023 Yuri N. Sedunov <aris@altlinux.org> 53-alt1
- 53

* Wed Oct 18 2023 Yuri N. Sedunov <aris@altlinux.org> 52-alt1
- 52

* Wed Sep 27 2023 Yuri N. Sedunov <aris@altlinux.org> 51-alt1
- 51

* Tue Sep 19 2023 Yuri N. Sedunov <aris@altlinux.org> 50-alt1
- 50 (ported to GNOME-45)

* Mon Jun 26 2023 Yuri N. Sedunov <aris@altlinux.org> 47-alt1
- 47

* Sat May 06 2023 Yuri N. Sedunov <aris@altlinux.org> 46-alt1
- 46

* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt1
- first build for Sisyphus

