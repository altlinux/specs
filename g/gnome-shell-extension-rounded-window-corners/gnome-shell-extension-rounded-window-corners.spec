%def_enable snapshot

%define _name rounded-window-corners
%define ver_major 12
%define beta %nil
%define uuid %_name@fxgn
%define gettext_domain %_name@fxgn
%define xdg_name org.gnome.shell.extensions.%_name-reborn

%def_disable bootstrap

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt2

Summary: Rounded Window Corners Reborn extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/flexagoon/rounded-window-corners

Vcs: https://github.com/flexagoon/rounded-window-corners.git

BuildArch: noarch

BuildRequires: just npm /usr/bin/tsc /usr/bin/glib-compile-schemas

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif
Source1: %_name-%version-npm.tar

Requires: gnome-shell >= 50
Requires: typelib(Adw) = 1

%description
GNOME extension to add rounded corners to all windows.

%prep
%setup -n %_name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
npm install && npm audit fix --force &&
tar -cf %_name-%version-npm.tar node_modules && \
mv %_name-%version-npm.tar %_sourcedir/}

%build
just build
glib-compile-schemas _build/schemas

%install
mkdir -p %buildroot%_datadir/{locale,glib-2.0/schemas,gnome-shell/extensions}
cp -r _build %buildroot%_datadir/gnome-shell/extensions/%uuid
mv %buildroot%_datadir/gnome-shell/extensions/%uuid/locale %buildroot%_datadir/
%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
#%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc README.md

%changelog
* Thu May 14 2026 Yuri N. Sedunov <aris@altlinux.org> 12-alt2
- updated to 12-31-g9bc10e2 (GNOME 50 supported)

* Sat Jan 10 2026 Yuri N. Sedunov <aris@altlinux.org> 12-alt1
- first build for Sisyphus (12-15-g06e7874)

