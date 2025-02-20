%def_enable snapshot
%define _libexecdir %prefix/libexec

%define ver_major 0.45
%define xdg_name mobi.phosh.Phrog
%define rdn_name mobi.phosh.phrog

%def_disable check

%def_disable bootstrap

Name: phrog
Version: %ver_major.0
Release: alt0.5

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

%define phosh_ver %ver_major

Requires: greetd accountsservice
Requires: dconf osk-wayland font(lato)
Requires: /usr/bin/phoc /usr/bin/gnome-session

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

%build
%rust_build

%install
%rust_install
install -pD -m 644 data/%rdn_name.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
install -pD -m 644 data/%name.session -t %buildroot%_datadir/gnome-session/sessions/
install -pD -m 644 data/%xdg_name.desktop -t %buildroot%_desktopdir
install -pD -m 644 dist/fedora/greetd-config.toml -t %buildroot%_sysconfdir/%name/
install -pD -m 644 dist/fedora/%name.service -t %buildroot%_unitdir/
install -pD -m 644 data/systemd-session.conf -T %buildroot%_userunitdir/gnome-session@phrog.target.d/session.conf
install -Dpm 0755 data/%name-greetd-session -t %buildroot%_libexecdir/
install -d %buildroot%_datadir/%name/autostart
install -d %buildroot%_sysconfdir/%name/autostart

%find_lang %name

%check
dbus-run-session xvfb-run -a phoc -E "cargo test --release --frozen"

%files -f %name.lang
%dir %_sysconfdir/%name
%_sysconfdir/%name/greetd-config.toml
%_bindir/%name
%_libexecdir/%name-greetd-session
%_unitdir/%name.service
%dir %_userunitdir/gnome-session@phrog.target.d
%_userunitdir/gnome-session@phrog.target.d/session.conf
%_desktopdir/%xdg_name.desktop
%_datadir/gnome-session/sessions/%name.session
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%doc README*

%changelog
* Thu Feb 20 2025 Yuri N. Sedunov <aris@altlinux.org> 0.45.0-alt0.5
- 0.45.0

* Thu Nov 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt0.5
- updated to 0.42.0-5-ge9682f6

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt0.1
- first build for Sisyphus

