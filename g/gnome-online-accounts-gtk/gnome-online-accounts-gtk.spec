%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: gnome-online-accounts-gtk
Version: 3.50.8
Release: alt1

Summary: A GTK Frontend for GNOME Online Accounts
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/xapp-project/gnome-online-accounts-gtk

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(goa-1.0)

Requires: gnome-online-accounts

%description
GUI Utility for logging into online accounts for the
purpose of syncing mail, contacts and remote filesystems.

%prep
%setup
sed -i "s|Categories=.*|Categories=Network;FileTransfer;InstantMessaging;News;|" data/gnome-online-accounts-gtk.desktop.in.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc COPYING README.md
%_bindir/gnome-online-accounts-gtk
%_desktopdir/gnome-online-accounts-gtk.desktop
%_iconsdir/hicolor/scalable/apps/gnome-online-accounts-gtk.svg

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 3.50.8-alt1
- Initial build for Sisyphus
