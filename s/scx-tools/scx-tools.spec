%define sorce_name scx-loader

Name:    scx-tools
Version: 1.1.2
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
scx_loader: A DBUS Interface for Managing sched_ext Schedulers

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install scx_loader scxctl
target/release/xtask install --destdir=%buildroot

%files
%doc LICENSE README.md
%_bindir/scx_loader
%_bindir/scxctl
%_datadir/dbus-1/system.d/org.scx.Loader.conf
%_datadir/dbus-1/interfaces/org.scx.Loader.xml
%_datadir/polkit-1/actions/org.scx.Loader.policy
%dir %_datadir/scx_loader
%_datadir/scx_loader/config.toml
%_datadir/dbus-1/system-services/org.scx.Loader.service
%_unitdir/scx_loader.service

%changelog
* Tue Aug 25 2026 Sergey Palcheh <minergenon@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
