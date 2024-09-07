# see .gitmodules
%def_enable snapshot
%define ver_major 0.1

%def_disable bootstrap
%def_enable check

Name: dynisland
Version: %ver_major.3
Release: alt0.1

Summary: A dynamic and extensible GTK4 bar
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/cr3eperall/dynisland

Vcs: https://github.com/cr3eperall/dynisland.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

Requires: dbus

BuildRequires(pre): rpm-build-rust
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)

%description
A dynamic and extensible GTK4 bar for compositors implementing
wlr-layer-shell, written in Rust.

Dynisland is designed to look and feel like Apple's Dynamic Island.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name
%doc README*

%changelog
* Sat Sep 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt0.1
- 0.1.3

* Fri Aug 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt0.1
- preview for Sisyphus (0.1.2-2-gfb03410)


