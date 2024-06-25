%global _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: pve-xtermjs
Summary: HTML/JS Shell client
Version: 5.3.0.3
Release: alt2
License: AGPL-3.0+
Group: Networking/WWW
Url: https://git.proxmox.com/

Vcs: git://git.proxmox.com/git/pve-xtermjs.git
Source: %name-%version.tar

#Support loongarch64 fix
Patch3500: pve-xtermjs-5.3.0.3-alt-loongarch64_nix_vendor_fix.patch

ExclusiveArch: x86_64 aarch64 loongarch64
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust pkgconfig(openssl) libuuid-devel
BuildRequires: /proc
BuildRequires: cargo-vendor-checksum

%description
This is an xterm.js client for PVE Host, Container and Qemu Serial Terminal

%prep
%setup
%patch3500 -p1

# Checksum update for patched files
cargo-vendor-checksum \
    --vendor %_builddir/%name-%version/termproxy/vendor -f \
	nix/src/sys/ioctl/linux.rs

%build
#export BUILD_MODE=release
#%%make_build
pushd termproxy
%rust_build
popd

#sed -i 's|Proxmox|PVE|' xterm.js/src/index.html.tpl.in
sed -e "s/@VERSION@/%version/" xterm.js/src/index.html.tpl.in > xterm.js/src/index.html.tpl
sed -e "s/@VERSION@/%version/" xterm.js/src/index.html.hbs.in > xterm.js/src/index.html.hbs
rm xterm.js/src/index.html.tpl.in xterm.js/src/index.html.hbs.in

%install
pushd termproxy
#%%rust_install proxmox-termproxy
install -dm755 %buildroot%_libexecdir/proxmox/
install -m755 target/release/proxmox-termproxy %buildroot%_libexecdir/proxmox/
install -dm755 %buildroot%_bindir
ln -s %_libexecdir/proxmox/proxmox-termproxy %buildroot%_bindir/termproxy
popd
mkdir -p %buildroot%_datadir/%name
cp xterm.js/src/* %buildroot%_datadir/%name/

%files
%doc xterm.js/debian/copyright
%_libexecdir/proxmox/proxmox-termproxy
%_bindir/termproxy
%_datadir/%name

%changelog
* Sat Jun 22 2024 Aleksei Kalinin <kaa@altlinux.org> 5.3.0.3-alt2
- NMU: Patched vendor nix for loongarch64 support

* Thu Feb 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.3.0.3-alt1
- 5.3.0-3

* Tue Oct 31 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.16.0.1-alt2
- Support LoongArch architecture

* Thu May 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.16.0.1-alt1
- add copyright file

* Mon Mar 20 2023 Alexey Shabalin <shaba@altlinux.org> 4.16.0-alt1
- 4.16.0-1

* Fri Nov 05 2021 Valery Inozemtsev <shrek@altlinux.ru> 4.12.0-alt1
- 4.12.0-1

* Fri Mar 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.10.1-alt1
- 3.10.1-2

* Fri Jul 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0-5

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- initial release

