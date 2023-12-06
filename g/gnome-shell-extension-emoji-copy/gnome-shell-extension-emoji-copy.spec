%def_enable snapshot

%define _name emoji-copy
%define old_name emoji-selector
%define git_ver 1.1.0
# from metadata.json
%define ego_ver 14
%define beta %nil
%define uuid emoji-copy@felipeftn
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ego_ver
Release: alt1

Summary: Emoji Selector for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://github.com/felipeftn/emoji-copy.git

%if_disabled snapshot
Source: %url/-/archive/v%git_ver%beta/%_name-%git_ver%beta.tar.gz
%else
Vcs: https://github.com/felipeftn/emoji-copy.git
Source: %_name-%git_ver%beta.tar
%endif
# reverse this
Patch10: %_name-1.1.0-up-transgenders.patch
Patch11: %_name-1.1.0-1-up-transgenders.patch

BuildArch: noarch

Obsoletes: gnome-shell-extension-%old_name
Conflicts: gnome-shell-extension-%old_name
Provides: gnome-shell-extension-%old_name = %EVR

Requires: gnome-shell >= 45 font(notocoloremoji)

%description
This GNOME shell extension provides a searchable popup menu displaying
most emojis. Clicking on an emoji copies it to your clipboard.

%prep
%setup -n %_name-%git_ver%beta
%patch10 -p1 -R
%patch11 -p1

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
* Wed Dec 06 2023 Yuri N. Sedunov <aris@altlinux.org> 14-alt1
- 14
- switched build to EGO release numbering

* Fri Dec 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Nov 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

