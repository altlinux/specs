%def_disable snapshot

%define _name blur-my-shell
%define ver_major 45
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

Requires: gnome-shell >= 44
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
* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt1
- first build for Sisyphus

