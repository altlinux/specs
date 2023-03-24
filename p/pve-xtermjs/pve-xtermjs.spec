%global _unpackaged_files_terminate_build 1

Name: pve-xtermjs
Summary: HTML/JS Shell client
Version: 4.16.0
Release: alt1
License: AGPL-3.0+
Group: Networking/WWW
Url: https://git.proxmox.com/

Vcs: git://git.proxmox.com/git/pve-xtermjs.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust pkgconfig(openssl) libuuid-devel
BuildRequires: /proc

%description
This is an xterm.js client for PVE Host, Container and Qemu Serial Terminal

%prep
%setup

%build
#export BUILD_MODE=release
#%%make_build
%rust_build

#sed -i 's|Proxmox|PVE|' src/www/index.html.tpl.in
sed -e "s/@VERSION@/%version/" src/www/index.html.tpl.in > src/www/index.html.tpl
sed -e "s/@VERSION@/%version/" src/www/index.html.hbs.in > src/www/index.html.hbs
rm src/www/index.html.tpl.in src/www/index.html.hbs.in

%install
%rust_install termproxy
mkdir -p %buildroot%_datadir/%name
cp src/www/* %buildroot%_datadir/%name/

%files
%_bindir/termproxy
%_datadir/%name

%changelog
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

