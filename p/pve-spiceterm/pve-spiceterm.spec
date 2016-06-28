%define sname spiceterm
%define pname %sname-pve

Name: pve-%sname
Summary: SPICE Terminal Emulator
Version: 2.0
Release: alt2
License: GPLv2
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64

Source0: %sname.tar.xz
Source1: SPICE-0.12.7.tar
Source2: spice-common.tar
Patch0: pve-allow-to-set-sasl-callbacks.patch
Patch1: spiceterm-alt.patch

BuildRequires: glib2-devel libsasl2-devel perl-Pod-Usage gcc-c++ libjpeg-devel libpixman-devel
BuildRequires: zlib-devel libssl-devel python-module-pyparsing libcacard-devel spice-protocol
BuildRequires: libopus-devel liblz4-devel python-module-six libgio-devel

%description
With spiceterm you can start commands and export its standard input and
output to any SPICE client (simulating a xterm Terminal).

%prep
%setup -q -n %sname -a1
%patch0 -p0
%patch1 -p1

ln -s SPICE-* SPICE

%build
pushd SPICE*
tar -xf %SOURCE2
echo 0.12.7 > .tarball-version
%autoreconf
%configure \
    --disable-celt051 \
    --enable-lz4 \
    --disable-opengl \
    --disable-smartcard \
    --enable-static=yes \
    --with-sasl
%make_build
popd

make %sname
make %sname.1

%install
install -pD -m0755 %sname %buildroot%_bindir/%sname
install -pD -m0644 %sname.1 %buildroot%_man1dir/%sname.1

%files
%_bindir/%sname
%_man1dir/%sname.1*

%changelog
* Tue Jun 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt2
- fixed keymaps path

* Mon Mar 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- initial release

