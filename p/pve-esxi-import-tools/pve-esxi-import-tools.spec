%define _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: pve-esxi-import-tools
Summary: Tools to allow importing VMs from ESXi hosts
Version: 0.7.0
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://git.proxmox.com/?p=pve-esxi-import-tools.git
Vcs: git://git.proxmox.com/git/pve-esxi-import-tools.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 riscv64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: python3-module-mypy
BuildRequires: libfuse3-devel
BuildRequires: pkgconf
BuildRequires: pkgconfig(openssl)
BuildRequires: /proc

%description
Tools to allow importing VMs from ESXi hosts.
Provides a FUSE file system to access files on ESXi hosts and a python utility
to query the list of VMs and datastores.

%prep
# Vendoring:
# rm -rf Cargo.lock vendor/*
# cargo vendor
# find vendor -name *.a -delete
# git add -f vendor Cargo.lock ...
%setup
sed -i 's!include /usr/share/dpkg/default.mk!#include /usr/share/dpkg/default.mk!' Makefile
sed -i 's!CARGO_BUILD_ARGS += --release!CARGO_BUILD_ARGS += --release --offline!' Makefile
sed -i 's!install: $(BINARY) $(SCRIPT) .lint-incremental!install: $(BINARY) $(SCRIPT)!' Makefile

%build
export REPOID=alt
export BUILD_MODE=release
%rust_build

%install
%makeinstall_std

%files
%doc debian/copyright
%_libexecdir/%name

%changelog
* Wed Apr 17 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.7.0-alt1
- 0.7.0

* Fri Mar 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 0.6.0-alt1
- Initial build for ALT.

