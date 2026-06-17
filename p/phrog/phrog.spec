%def_disable snapshot
%define _libexecdir %prefix/libexec

%define ver_major 0.53
%define xdg_name mobi.phosh.Phrog
%define rdn_name mobi.phosh.phrog

%def_disable check

%def_disable bootstrap

Name: phrog
Version: %ver_major.0
Release: alt1

Summary: Mobile device greeter
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/samcday/phrog

Vcs: https://github.com/samcday/phrog.git

%if_disabled snapshot
Source: https://github.com/samcday/phrog/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define phosh_ver 0.45

Provides: greetd-greeter

Requires: greetd accountsservice
Requires: dconf font(lato)
Requires: /usr/bin/phoc /usr/bin/gnome-session
Requires: %_userunitdir/mobi.phosh.OSK.service

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(libphosh-%phosh_ver) >= %phosh_ver
%{?_enable_check:BuildRequires: xvfb-run dbus phosh accountsservice /usr/bin/Xwayland}

%description
A greeter that works on mobile devices and also other kinds of computers.
phrog uses Phosh to conduct a greetd conversation.
It is the spiritual successor of phog.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

#sed -i 's|user = "greetd"|user = "_greeter"|' dist/fedora/greetd-config.toml

%build
export GETTEXT_SYSTEM=1
%rust_build
%__cargo run --offline --package xtask -- dist-data greetd-config.toml --greetd-vt 1 --greetd-user _greeter

%install
export GETTEXT_SYSTEM=1
%rust_install
install -pD -m 644 data/%rdn_name.gschema.xml -t %buildroot%_datadir/glib-2.0/schemas/
install -pD -m 644 data/00_%xdg_name.gschema.override -t %buildroot%_datadir/glib-2.0/schemas/
install -pD -m 644 data/%name.session -t %buildroot%_datadir/gnome-session/sessions/
install -pD -m 644 data/%xdg_name.desktop -t %buildroot%_desktopdir
install -pD -m 644 target/dist-data/greetd-config.toml -t %buildroot%_sysconfdir/%name/
install -pD -m 644 dist/fedora/%name.service -t %buildroot%_unitdir/
install -pD -m 644 data/%xdg_name.service -t %buildroot%_userunitdir/
install -pD -m 644 data/%xdg_name.target -t %buildroot%_userunitdir/
install -pD -m 644 data/systemd-session.conf -T %buildroot%_userunitdir/gnome-session@phrog.target.d/session.conf
install -Dpm 0755 data/%name-greetd-session -t %buildroot%_libexecdir/
install -d %buildroot%_datadir/%name/autostart
install -d %buildroot%_sysconfdir/%name/autostart

%find_lang %name

%check
export GETTEXT_SYSTEM=1
dbus-run-session xvfb-run -a phoc -E "cargo test --release --frozen"

%files -f %name.lang
%dir %_sysconfdir/%name
%_sysconfdir/%name/greetd-config.toml
%_bindir/%name
%_libexecdir/%name-greetd-session
%_unitdir/%name.service
%_userunitdir/%xdg_name.service
%_userunitdir/%xdg_name.target
%dir %_userunitdir/gnome-session@phrog.target.d
%_userunitdir/gnome-session@phrog.target.d/session.conf
%_desktopdir/%xdg_name.desktop
%_datadir/gnome-session/sessions/%name.session
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/00_%xdg_name.gschema.override
%doc README*

%changelog
* Wed Jun 17 2026 Yuri N. Sedunov <aris@altlinux.org> 0.53.0-alt1
- 0.53.0

* Fri Nov 28 2025 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Thu Oct 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt0.6
- 0.46.0-16-g07ec9c2 (adapted to gnome-session-49)

* Mon Mar 24 2025 Yuri N. Sedunov <aris@altlinux.org> 0.46.0-alt0.5
- 0.46.0
- added greetd-greeter provides
- changed the user from greetd to _greeter

* Thu Feb 20 2025 Yuri N. Sedunov <aris@altlinux.org> 0.45.0-alt0.5
- 0.45.0

* Thu Nov 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt0.5
- updated to 0.42.0-5-ge9682f6

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt0.1
- first build for Sisyphus

