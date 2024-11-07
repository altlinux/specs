%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.42
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
Requires: /usr/bin/phoc

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
install -pD -m 644 resources/%rdn_name.gschema.xml \
    %buildroot%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%find_lang %name

%check
dbus-run-session xvfb-run -a phoc -E "cargo test --release --frozen"

%files -f %name.lang
%_bindir/%name
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%doc README*

%changelog
* Thu Nov 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt0.5
- updated to 0.42.0-5-ge9682f6

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt0.1
- first build for Sisyphus



