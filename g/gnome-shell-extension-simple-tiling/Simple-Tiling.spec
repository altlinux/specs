%define oname simple-tiling@domoel

Name: gnome-shell-extension-simple-tiling
Version: 8.3
Release: alt1

Summary: A simple Tiling Window Manager for Gnome

License: MIT
Group: Graphical desktop/GNOME

Url: https://extensions.gnome.org/extension/8345/simple-tiling
Vcs: https://git.ztfr.eu/Dome/Simple-Tiling

BuildArch: noarch

Source: %name-%version.tar

Requires: gnome-shell >= 48.0

BuildRequires: /usr/bin/glib-compile-schemas zip unzip

%description
A lightweight, opinionated, and automatic tiling window manager for GNOME Shell.

%prep
%setup
subst 's|@unzip -q $(UUID)-modern-v$(VERSION).zip -d $(EXTDIR)/$(UUID)|@unzip -q $(UUID)-modern-v$(VERSION).zip -d $(EXTDIR)|' Makefile

#subst 's|"49"|"49", "50"|' metadata_modern.json.in

%build
make build-modern

%install
install -d %buildroot%_datadir/gnome-shell/extensions
make install-modern EXTDIR=%buildroot%_datadir/gnome-shell/extensions

%files
%_datadir/gnome-shell/extensions/%oname
%doc README.md

%changelog
* Sun Jun 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 8.3-alt1
- automatic build: 8.2 -> 8.3

* Thu Jun 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 8.2-alt1
- 7.6 -> 8.2
- fixed for GNOME 50

* Tue Mar 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 7.6-alt2
- fixed for GNOME 50

* Mon Dec 15 2025 Aleksandr Shamaraev <shad@altlinux.org> 7.6-alt1
- Initial build for ALT Linux.
