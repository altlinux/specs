%define _unpackaged_files_terminate_build 1
%define nautilus_extdir %_datadir/nautilus-python/extensions

Name: folder-color
Version: 1.0
Release: alt1

Summary: Folder colors and emblems in Nautilus
License: GPL-3.0
Group: Graphical desktop/GNOME

Url: https://github.com/SpikedPaladin/FolderColor
Vcs: https://github.com/SpikedPaladin/FolderColor
Source: %name-%version.tar

Requires: nautilus-python

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

BuildArch: noarch

%description
An extension for Nautilus that allows you change folder colors and emblems.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%nautilus_extdir/folder-color.py
%doc README.md

%changelog
* Wed Mar 12 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0-alt1
- initial build
