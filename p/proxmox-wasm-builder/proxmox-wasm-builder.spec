%global _unpackaged_files_terminate_build 1

Name:    proxmox-wasm-builder
Version: 0.2.0
Release: alt1
Summary: Proxmox rust to WASM build tool
License: AGPL-3.0+
Group:   Development/Tools
Url:     https://www.proxmox.com/en/proxmox-wasm-buidlder
Vcs:     git://git.proxmox.com/git/proxmox-wasm-builder.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust clang-devel

Requires: binaryen

%description
Tool to build rust programs to WASM for the web

%prep
%setup -q

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Thu Mar 27 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 0.2.0-alt1
- Initial build
