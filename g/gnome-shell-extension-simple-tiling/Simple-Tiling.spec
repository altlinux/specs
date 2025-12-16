%define oname simple-tiling@domoel

Name: gnome-shell-extension-simple-tiling
Version: 7.6
Release: alt1

Summary: A simple Tiling Window Manager for Gnome

License: MIT
Group: Graphical desktop/GNOME

Url: https://extensions.gnome.org/extension/8345/simple-tiling
Vcs: https://github.com/Domoel/Simple-Tiling

BuildArch: noarch

Source: %name-%version.tar

Requires: gnome-shell >= 48.0

BuildRequires: /usr/bin/glib-compile-schemas zip unzip

%description
A lightweight, opinionated, and automatic tiling window manager for GNOME Shell.

%prep
%setup
subst 's|@unzip -q $(UUID)-modern-v$(VERSION).zip -d $(EXTDIR)/$(UUID)|@unzip -q $(UUID)-modern-v$(VERSION).zip -d $(EXTDIR)|' Makefile

%build
make build-modern

%install
install -d %buildroot%_datadir/gnome-shell/extensions
make install-modern EXTDIR=%buildroot%_datadir/gnome-shell/extensions

%files
%_datadir/gnome-shell/extensions/%oname
%doc README.md

%changelog
* Mon Dec 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 7.6-alt1
- Initial build for ALT Linux.
