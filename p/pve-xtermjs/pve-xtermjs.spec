%global _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: pve-xtermjs
Summary: HTML/TypeScript based fully-featured terminal for Proxmox projects
Version: 6.0.0.1
Release: alt1
License: AGPL-3.0+
Group: Networking/WWW
Url: https://git.proxmox.com/

Vcs: git://git.proxmox.com/git/pve-xtermjs.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 loongarch64
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust pkgconfig(openssl) libuuid-devel
BuildRequires: /proc

Requires: proxmox-termproxy

%description
HTML/TypeScript based fully-featured terminal for Proxmox projects.
Provides the xterm.js frontend for the terminal feature in Proxmox projects'
web UI's, like for host administration or Proxmox VE containers shells.

%package -n proxmox-termproxy
Summary: Wrapper proxy for executing programs in the system terminal
Version: 2.1.0
Group: Networking/WWW

%description -n proxmox-termproxy
This package provides an wrapper for running commands in a system terminal,
redirecting input via a special protocol and returning the PTY output 1:1.
It's used for the backend of the xterm.js based host and virtual guest
consoles in Proxmox projects like Proxmox VE or Proxmox Backup Server.

%prep
%setup

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
%_datadir/%name

%files -n proxmox-termproxy
%_libexecdir/proxmox/proxmox-termproxy
%_bindir/termproxy

%changelog
* Tue Jun 09 2026 Sergey Konev <darisishe@altlinux.org> 6.0.0.1-alt1
- Update:
  + pve-xtermjs 6.0.0.1
  + proxmox-termproxy 2.1.0

* Thu Jan 22 2026 Sergey Konev <darisishe@altlinux.org> 5.5.0.3-alt1
- Update:
  + pve-xtermjs 5.5.0.3
  + proxmox-termproxy 2.0.3
- Package 'proxmox-termproxy' separately

* Tue Apr 15 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 5.5.0.2-alt1
- 5.5.0-2 

* Wed Dec 18 2024 Sergey Konev <darisishe@altlinux.org> 5.3.0.3-alt3
- Merged upstream fixes

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

