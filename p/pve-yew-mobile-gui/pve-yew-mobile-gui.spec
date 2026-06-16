%define _unpackaged_files_terminate_build 1

Name: pve-yew-mobile-gui
Summary: Mobile Web UI to for the Proxmox Virtual Environment
Version: 0.7.0
Release: alt1
License: AGPL-3.0-or-later
Group: System/Servers
Url: https://git.proxmox.com/

Requires: pve-yew-mobile-i18n fonts-font-awesome

ExclusiveArch: x86_64 aarch64 loongarch64

Source0: %name-%version.tar
Source1: pwt-assets.tar
Patch: %name-%version.patch

BuildRequires: rpm-build-rust
BuildRequires: rust-wasm32-unknown-unknown-target
BuildRequires: esbuild fonts-font-awesome
BuildRequires: proxmox-wasm-builder grass-sass

%description
Mobile Web UI to for the Proxmox Virtual Environment.
This package provides the mobile web UI of the Proxmox Virtual Environment.


%prep
%setup -a1
%patch -p1

%build
export BUILD_MODE=release
%make

%install
export BUILD_MODE=release
%makeinstall_std

%files
%doc debian/copyright
%_datadir/%name

%changelog
* Wed Jun 10 2026 Sergey Konev <darisishe@altlinux.org> 0.7.0-alt1
- 0.7.0

* Tue Jan 20 2026 Sergey Konev <darisishe@altlinux.org> 0.6.4-alt1
- 0.6.4

* Tue Sep 30 2025 Sergey Konev <darisishe@altlinux.org> 0.6.2-alt1
- Initial build
