%def_enable snapshot

%define _name emoji-copy
%define old_name emoji-selector
%define ver_major 1.0
%define beta %nil
%define uuid emoji-copy@felipeftn
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major.1
Release: alt1

Summary: Emoji Selector for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/felipeftn/emoji-copy.git

%if_disabled snapshot
Source: %url/-/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Vcs: https://github.com/felipeftn/emoji-copy.git
Source: %_name-%version%beta.tar
%endif
# reverse this
Patch: %_name-1.0.1-up-transgenders.patch

BuildArch: noarch

Obsoletes: gnome-shell-extension-%old_name
Conflicts: gnome-shell-extension-%old_name
Provides: gnome-shell-extension-%old_name = %EVR

Requires: gnome-shell >= 45 font(notocoloremoji)

%description
This GNOME shell extension provides a searchable popup menu displaying
most emojis. Clicking on an emoji copies it to your clipboard.

%prep
%setup -n %_name-%version%beta
%patch -p1 -R

%build
./update-and-compile-translations.sh

%install
mkdir -p %buildroot%_datadir/{gnome-shell/extensions/%uuid,glib-2.0/schemas,icons/hicolor/symbolic/apps/}
pushd %uuid
cp -ar *.js* data/ %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a schemas/*.gschema.xml %buildroot%_datadir/glib-2.0/schemas/
cp -ar locale %buildroot%_datadir/ && rm -f %buildroot/%_datadir/locale/{*.pot*,*/*/*.po*}
cp -a icons/*.svg %buildroot%_iconsdir/hicolor/symbolic/apps/
popd

%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/*.gschema.xml
%_iconsdir/hicolor/symbolic/apps/*.svg
%doc README.md

%changelog
* Fri Dec 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Nov 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

