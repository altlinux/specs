%define sname spiceterm
%define pname %sname-pve

Name: pve-%sname
Summary: SPICE Terminal Emulator
Version: 3.1.1
Release: alt1
License: GPLv2
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64

Source0: %sname.tar.xz
Source1: spice-0.14.1.tar.bz2
Source2: spice-protocol.tar.xz
Patch0: allow-to-set-sasl-callbacks.patch

Patch10: spiceterm-alt.patch
Patch11: pve-spice-protocol.patch

BuildRequires: libgio-devel libjpeg-devel liblz4-devel libogg-devel libopus-devel libpixman-devel
BuildRequires: libsasl2-devel libssl-devel perl-Pod-Usage zlib-devel libgdk-pixbuf-devel
BuildRequires: python-modules python-module-pyparsing python-module-six

%description
With spiceterm you can start commands and export its standard input and
output to any SPICE client (simulating a xterm Terminal).

%prep
%setup -q -n %sname -a1 -a2
ln -s spice-0* spice

pushd spice
%patch0 -p1
popd
%patch10 -p1 -b .alt
%patch11 -p0

rm -f spice/subprojects/spice-common/common/generated_*

%build
pushd spice
%autoreconf
%configure \
	--disable-smartcard \
	--disable-celt051 \
	--enable-lz4 \
	--enable-static \
	--with-sasl
%make_build
popd

%make -C src

%install
%make -C src VERSION=%version DESTDIR=%buildroot install

%files
%_bindir/%sname
%_man1dir/%sname.1*

%changelog
* Mon Aug 05 2019 Valery Inozemtsev <shrek@altlinux.ru> 3.1.1-alt1
- 3.1-1

* Wed Nov 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.5-alt1
- 3.0-5

* Tue Nov 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 3.0.4-alt1.2
- rebuild

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.0.4-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 3.0.4-alt1
- 3.0-4

* Tue Jun 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt2
- fixed keymaps path

* Mon Mar 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- initial release

