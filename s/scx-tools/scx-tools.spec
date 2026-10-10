Name:    scx-tools
Version: 1.1.3
Release: alt1

Summary: Sched_ext Tools
License: GPL-2.0-only
Group:   System/Kernel and hardware
URL:     https://github.com/sched-ext/scx-loader

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
Requires: dbus
Requires: polkit

%description
Tools for managing sched_ext schedulers.

scx_loader is a system daemon and D-Bus based loader of sched_ext schedulers.
scxctl is a command-line client for switching schedulers, modes and arguments.
scxtui is an interactive terminal user interface for managing schedulers,
inspecting the loader state and viewing recent scheduler logs.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install scx_loader scxctl scxtui
target/release/xtask install --destdir=%buildroot

%files
%doc LICENSE README.md
%_bindir/scx_loader
%_bindir/scxctl
%_bindir/scxtui
%_datadir/dbus-1/system.d/org.scx.Loader.conf
%_datadir/dbus-1/interfaces/org.scx.Loader.xml
%_datadir/polkit-1/actions/org.scx.Loader.policy
%dir %_datadir/scx_loader
%_datadir/scx_loader/config.toml
%_datadir/dbus-1/system-services/org.scx.Loader.service
%_unitdir/scx_loader.service

%changelog
* Sat Oct 10 2026 Sergey Palcheh <minergenon@altlinux.org> 1.1.3-alt1
- new version 1.1.3

* Tue Aug 25 2026 Sergey Palcheh <minergenon@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
