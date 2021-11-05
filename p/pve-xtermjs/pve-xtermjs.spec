Name: pve-xtermjs
Summary: HTML/JS Shell client
Version: 4.12.0
Release: alt1
License: GPL
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %name.tar.xz
Source1: proxmox-0.10.0.tar.xz
Source2: %name-cargo.tar

Patch0: %name-cargo.patch

ExclusiveArch: x86_64 aarch64
BuildRequires: /proc clang-devel rust-cargo pkgconfig(openssl) libuuid-devel

%description
This is an xterm.js client for PVE Host, Container and Qemu Serial Terminal

%prep
%setup -q -n %name -a1 -a2
%patch0 -p1

%build
rm -fr .cargo
export CARGO_HOME=%_builddir/%name/cargo
cargo build --release --offline

sed -i 's|Proxmox|PVE|' src/www/index.html.tpl.in
sed -e "s/@VERSION@/%version/" src/www/index.html.tpl.in > src/www/index.html.tpl
sed -e "s/@VERSION@/%version/" src/www/index.html.hbs.in > src/www/index.html.hbs
rm src/www/index.html.tpl.in src/www/index.html.hbs.in

%install
install -pD -m755 target/release/termproxy %buildroot%_bindir/termproxy
mkdir -p %buildroot%_datadir/%name
cp src/www/* %buildroot%_datadir/%name/

%files
%_bindir/termproxy
%_datadir/%name

%changelog
* Fri Nov 05 2021 Valery Inozemtsev <shrek@altlinux.ru> 4.12.0-alt1
- 4.12.0-1

* Fri Mar 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.10.1-alt1
- 3.10.1-2

* Fri Jul 20 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0-5

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- initial release

