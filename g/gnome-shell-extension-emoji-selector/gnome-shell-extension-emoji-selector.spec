%def_enable snapshot

%define _name emoji-selector
%define __name %_name-for-gnome
%define ver_major 23
%define beta %nil
%define uuid emoji-selector@maestroschan.fr
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: Emoji Selector for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0
# Original url: https://github.com/maoschanz/emoji-selector-for-gnome
Url: https://github.com/VortexAcherontic/emoji-selector-for-gnome

BuildArch: noarch

%if_disabled snapshot
Source: %url/-/archive/%version%beta/%__name-%version%beta.tar.gz
%else
Vcs: https://github.com/VortexAcherontic/emoji-selector-for-gnome.git
Source: %__name-%version%beta.tar
%endif

Requires: gnome-shell >= 44
Requires: typelib(Gtk) = 4.0

%description
This GNOME shell extension provides a searchable popup menu displaying
most emojis. Clicking on an emoji copies it to your clipboard.

%prep
%setup -n %__name-%version%beta

%build
./update-and-compile-translations.sh

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas,icons/hicolor/symbolic/apps/}
pushd %uuid
cp -ar *.js* *.ui data/ %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a schemas/%xdg_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas/
cp -ar locale %buildroot%_datadir/ && rm -f %buildroot/%_datadir/locale/{*.pot*,*/*/*.po*}
cp -a icons/*.svg %buildroot%_iconsdir/hicolor/symbolic/apps/
popd

%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/symbolic/apps/*.svg
%doc README.md

%changelog
* Fri Sep 1 2023 Yuri N. Sedunov <aris@altlinux.org> 23-alt1
- first build for Sisyphus (ac3dca3 (no tags))

