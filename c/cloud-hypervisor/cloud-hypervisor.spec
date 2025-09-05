%global _unpackaged_files_terminate_build 1

Name:    cloud-hypervisor
Version: 47.0
Release: alt1

Summary: Open source Virtual Machine Monitor that runs on top of the KVM hypervisor
License: Apache-2.0 and BSD-3-Clause
Group:   Emulators
Url:     https://github.com/cloud-hypervisor/cloud-hypervisor

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: bison
BuildRequires: flex
BuildRequires: qemu-tools
BuildRequires: perl-IPC-Cmd
BuildRequires: rust >= 1.77
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(ossp-uuid)
BuildRequires: /proc

ExclusiveArch: x86_64 aarch64

%description
The project focuses on running modern, Cloud Workloads, on specific, common,
hardware architectures. In this case Cloud Workloads refers to those that are
run by customers inside a Cloud Service Provider. This means modern operating
systems with most I/O handled by paravirtualised devices (e.g. virtio), no
requirement for legacy devices, and 64-bit CPUs.
Cloud Hypervisor is implemented in Rust and is based on the Rust VMM crates.

%package remote
Summary: Remote tool for accessing a cloud hypervisor instance
Group: Development/Tools

%description remote
Remote tool for accessing a cloud hypervisor instance.

%prep
%setup
%patch -p1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/firecracker-microvm/micro-http?branch=main"]
git = "https://github.com/firecracker-microvm/micro-http"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/microsoft/igvm?branch=main"]
git = "https://github.com/microsoft/igvm"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/rust-vmm/acpi_tables?branch=main"]
git = "https://github.com/rust-vmm/acpi_tables"
branch = "main"
replace-with = "vendored-sources"

[source."git+https://github.com/rust-vmm/vm-fdt?branch=main"]
git = "https://github.com/rust-vmm/vm-fdt"
branch = "main"
replace-with = "vendored-sources"
EOF

%build
%rust_build

%install
%rust_install
%rust_install ch-remote

%check
%rust_test -- --test unit_tests::

%post
#according to upstream docs
setcap -q cap_net_admin+ep %_bindir/%name 2>/dev/null ||:

%files
%doc *.md
%_bindir/%name

%files remote
%doc README.md
%_bindir/ch-remote
 
%changelog
* Tue Sep 02 2025 Nadezhda Fedorova <fedor@altlinux.org> 47.0-alt1
- Initial build for ALTLinux.
