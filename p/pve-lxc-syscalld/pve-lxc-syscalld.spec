%global _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: pve-lxc-syscalld
Summary: PVE LXC syscall daemon
Version: 1.2.2.1
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Vcs: git://git.proxmox.com/git/pve-lxc-syscalld.git 
Source: %name-%version.tar
Patch: pve-lxc-syscalld-aarch64-u8.patch

ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust libsystemd-devel
BuildRequires: /proc

%description
A daemon which handles a selected subset of syscalls for unprivileged
containers.

%prep
%setup
%ifarch aarch64
%patch -p0 -b .u8
%endif
sed -i 's|roxmox ||' etc/pve-lxc-syscalld.service.in

%build
export BUILD_MODE=release
%make_build

%install
%makeinstall_std
install -dm755 %buildroot%_unitdir
install -m644 etc/%name.service %buildroot%_unitdir/

%files
%_unitdir/%name.service
%_libexecdir/%name/%name

%changelog
* Tue Oct 04 2022 Alexey Shabalin <shaba@altlinux.org> 1.2.2.1-alt1
- 1.2.2-1

* Wed Sep 29 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0-1

* Thu Dec 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- initial release

