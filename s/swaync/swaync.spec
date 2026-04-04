Name: swaync
Version: 0.12.6
Release: alt1

Summary: A simple GTK notification daemon
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/ErikReider/SwayNotificationCenter

# Source-url: https://github.com/ErikReider/SwayNotificationCenter/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-xdg
BuildRequires: meson vala sassc scdoc blueprint-compiler
BuildRequires: vapi(granite)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: vapi(gtk4-layer-shell-0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(systemd)

%description
A simple notification daemon with a GTK gui for notifications and the control center.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc README.md

%_bindir/swaync
%_bindir/swaync-client

%_userunitdir/swaync.service
%_datadir/dbus-1/services/org.erikreider.swaync.service
%_datadir/dbus-1/services/org.erikreider.swaync.cc.service
%_datadir/glib-2.0/schemas/org.erikreider.swaync.gschema.xml

%_man1dir/swaync*
%_man5dir/swaync*

%dir %_xdgconfigdir/swaync
%config %_xdgconfigdir/swaync/*

%_datadir/bash-completion/completions/swaync*

%_datadir/zsh/site-functions/_swaync*

%_datadir/fish/vendor_completions.d/swaync*

%changelog
* Sat Apr 04 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.12.6-alt1
- new version 0.12.6

* Fri Feb 06 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.12.4-alt1
- new version 0.12.4 (with rpmrb script)

* Sat Dec 06 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.12.3-alt1
- new version 0.12.3 (with rpmrb script)

* Thu Aug 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.12.2-alt1
- new version 0.12.2 (with rpmrb script)

* Sat Jul 26 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.12.1-alt1
- new version 0.12.1 (with rpmrb script)

* Wed Apr 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Mon Jul 29 2024 Roman Alifanov <ximper@altlinux.org> 0.10.1-alt1
- initial build
