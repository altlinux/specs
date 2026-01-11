%def_disable snapshot

%define __name ClipMaster
%define _name clipmaster
%define ver_major 1.3
%define beta %nil
%define uuid %_name@gnome.extension
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: ClipMaster is a clipboard manager for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/sfnemis/ClipMaster

Vcs: https://github.com/sfnemis/ClipMaster.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%__name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1
Requires: wl-clipboard
# for x11
#Requires: xclip

BuildRequires: /usr/bin/glib-compile-schemas

%description
A powerful GNOME Shell clipboard manager with history, encryption, image
support, favorites, and 12 themes. Follows system dark/light mode.

%prep
%setup -n %__name-%version%beta

%build
/usr/bin/glib-compile-schemas --strict %uuid/schemas

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions
cp -r %uuid %buildroot%_datadir/gnome-shell/extensions/

%files
%_datadir/gnome-shell/extensions/%uuid/
%doc README.md

%changelog
* Sun Jan 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- first build for Sisyphus

