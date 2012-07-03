%define rname syslinux
Summary: Simple kernel loader which boots from a FAT filesystem
Name: %{rname}1
Version: 1.62
Release: alt4.1
License: GPL v2 or later
Group: System/Kernel and hardware
Packager: Kachalov Anton <mouse@altlinux.ru>
Url: http://syslinux.zytor.com

Source: ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/Old/%rname-%version.tar.bz2
Patch: %rname-%version.patch.bz2

BuildPrereq: nasm, perl, libpng3

# Automatically added by buildreq on Mon Jun 23 2003
BuildRequires: nasm netpbm

%description
Syslinux is a simple kernel loader. It normally loads the kernel (and an
optional initrd image) from a FAT filesystem. It can also be used as a
PXE bootloader during network boots.

%prep
%setup -n %rname-%version
%patch -p1

%build
chmod +x add_crc
make clean
make

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/%rname
#make INSTALLROOT=%buildroot install
install -c ppmtolss16 %buildroot%_bindir
install -c syslinux %buildroot%_bindir
install -c gethostip %buildroot%_bindir
install -c lss16toppm %buildroot%_bindir
install -c ldlinux.bin %buildroot%_libdir/%rname
install -c isolinux.bin %buildroot%_libdir/%rname
install -c isolinux-debug.bin %buildroot%_libdir/%rname
install -c copybs.com %buildroot%_libdir/%rname
install -c pxelinux.0 %buildroot%_libdir/%rname

%files
%doc NEWS README TODO
%doc distrib.doc isolinux.doc pxelinux.doc syslinux.doc
%_bindir/lss16toppm
%_bindir/ppmtolss16
%_bindir/syslinux
%_libdir/syslinux

%changelog
* Thu Aug 09 2007 Slava Semushin <php-coder@altlinux.ru> 1.62-alt4.1
- NMU
- Changed License tag from 'BSD' to 'GPL v2 or later' (#12459)
- Added Url tag, updated url in Source tag
- Set Packager tag to previous maintainer
- Exclude standart COPYING file from package
- Spec cleanup

* Wed Sep 17 2003 Kachalov Anton <mouse@altlinux.ru> 1.62-alt4
- rebuild in hasher

* Thu Jul 03 2003 Kachalov Anton <mouse@altlinux.ru> 1.62-alt3
- rebuilding *.bin

* Fri Jun 27 2003 Kachalov Anton <mouse@altlinux.ru> 1.62-alt2
- bugfix with vga parameter

* Mon Jun 23 2003 Rider <rider@altlinux.ru> 1.62-alt1
- first build for Sisyphus with patches from SuSE (gfxboot)
