%define _unpackaged_files_terminate_build 1

Name: tiny-dfr
Version: 0.3.7
Release: alt1

Summary: Tiny Apple T2 and Silicon Mac Touch Bar daemon
License: MIT AND Apache-2.0
Group: System/Kernel and hardware

URL: https://github.com/AsahiLinux/tiny-dfr
VCS: https://github.com/AsahiLinux/tiny-dfr
Source: %name-%version.tar
Source1: %name-vendor.tar

BuildRequires(pre): rpm-build-systemd
BuildRequires: rust-cargo
BuildRequires: rpm-macros-rust
BuildRequires: libcairo-devel
BuildRequires: libcairo-gobject-devel
BuildRequires: glib2-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: librsvg-devel
BuildRequires: libudev-devel
BuildRequires: libinput-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig-devel

Requires: udev-rules

%description
The most basic dynamic function row daemon possible. Renders UI on the
Apple T2 and Silicon Mac Touch Bar using DRM and libinput.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install tiny-dfr
install -Dm644 share/tiny-dfr/config.toml %buildroot%_datadir/tiny-dfr/config.toml
install -Dm644 share/tiny-dfr/*.svg -t %buildroot%_datadir/tiny-dfr/
install -Dm644 etc/systemd/system/tiny-dfr.service %buildroot%_unitdir/tiny-dfr.service
install -Dm644 etc/udev/rules.d/99-touchbar-tiny-dfr.rules %buildroot%_udevrulesdir/99-touchbar-tiny-dfr.rules
install -Dm644 etc/udev/rules.d/99-touchbar-seat.rules %buildroot%_udevrulesdir/99-touchbar-seat.rules

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/tiny-dfr
%dir %_datadir/tiny-dfr
%_datadir/tiny-dfr/config.toml
%_datadir/tiny-dfr/*.svg
%_unitdir/tiny-dfr.service
%_udevrulesdir/99-touchbar-tiny-dfr.rules
%_udevrulesdir/99-touchbar-seat.rules

%changelog
* Fri Sep 04 2026 Anton Osipov <radiolamp@altlinux.org> 0.3.7-alt1
- Initial build.
