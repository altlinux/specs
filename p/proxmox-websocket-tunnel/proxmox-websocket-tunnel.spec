%global _unpackaged_files_terminate_build 1

Name: proxmox-websocket-tunnel
Version: 0.1.0
Release: alt1
Summary: Proxmox websocket tunneling helper
License: AGPL-3.0+
Group: Networking/Other
URL: https://www.proxmox.com/
Vcs: git://git.proxmox.com/git/proxmox-websocket-tunnel.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel libacl-devel libssl-devel libzstd-devel
BuildRequires: /proc

%description
%summary.
This package contains a helper binary for tunnelling UNIX sockets over a
websocket connection.

%prep
%setup

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Wed Mar 09 2022 Alexey Shabalin <shaba@altlinux.org> 0.1.0-alt1
- Initial build.

