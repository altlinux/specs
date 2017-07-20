%define sname spiceterm
%define pname %sname-pve

Name: pve-%sname
Summary: SPICE Terminal Emulator
Version: 3.0.4
Release: alt1
License: GPLv2
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64

Source0: %sname.tar.xz
Source1: spice-0.12.8.tar.bz2
Source2: celt-0.5.1.3.tar.gz
Patch0: pve-allow-to-set-sasl-callbacks.patch
Patch1: CVE-2016-9577-and-CVE-2016-9578.patch

Patch10: spiceterm-alt.patch

BuildRequires: libgio-devel libjpeg-devel liblz4-devel libogg-devel libopus-devel libpixman-devel
BuildRequires: libsasl2-devel libssl-devel perl-Pod-Usage spice-protocol zlib-devel

%description
With spiceterm you can start commands and export its standard input and
output to any SPICE client (simulating a xterm Terminal).

%prep
%setup -q -n %sname -a1 -a2
ln -s spice-* spice
ln -s celt* celt

pushd spice
%patch0 -p1
%patch1 -p1
popd
%patch10 -p1

%build
pushd celt
ln -s libcelt celt051
%autoreconf
%configure \
	--enable-static
%make_build
popd

pushd spice
echo 0.12.8 > .tarball-version
%autoreconf
export CELT051_LIBS="-L%_builddir/spiceterm/celt/libcelt -lcelt051 -lm"
export CELT051_CFLAGS="-I%_builddir/spiceterm/celt"
%configure \
	--disable-smartcard \
	--enable-lz4=yes \
	--enable-opengl=no \
	--enable-static=yes \
	--with-sasl
%make_build
popd

%make

%install
%make DESTDIR=%buildroot install

%files
%_bindir/%sname
%_man1dir/%sname.1*

%changelog
* Wed Jul 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 3.0.4-alt1
- 3.0-4

* Tue Jun 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt2
- fixed keymaps path

* Mon Mar 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- initial release

