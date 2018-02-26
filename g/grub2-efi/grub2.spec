%define _optlevel s

Name: grub2-efi
Version: 1.99
Release: alt9

Summary: GRand Unified Bootloader
License: GPL
Url: http://www.gnu.org/software/grub/grub.en.html
Group: System/Kernel and hardware
Source0: grub2-%version.tar.bz2
Source1: grub2-sysconfig

Source3: 39_memtest
Source4: grub2.filetrigger

Source5: grub-extras-%version.tar.bz2

Source6: grub-autoupdate
Source7: firsttime

Patch1: grub-1.99-os-alt.patch
Patch2: grub-1.98-sysconfig-path-alt.patch
Patch3: grub-1.99-altlinux-theme.patch
Patch4: grub-1.99-evms-crap-alt.patch
Patch5: grub-1.99-os-alt-xen.patch
Patch6: grub-1.99-debian-disable_floppies.patch
Patch7: grub-1.99-grubinstall-evms-sync-alt.patch
Patch8: grub-1.99_fix_for_automake_1.11.2.patch
Patch9: grub-1.99_alt_datadir_scripts.patch

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

BuildRequires: flex fonts-bitmap-misc libfreetype-devel python-modules ruby autogen
BuildRequires: liblzma-devel help2man zlib-devel

Exclusivearch: %ix86 x86_64

Conflicts: grub
Obsoletes: grub < %version-%release

Conflicts: grub2 < 1.99-alt8
Conflicts: grub2-pc

Requires: gettext efibootmgr

%description
GNU GRUB is a multiboot boot loader. It was derived from GRUB. It is an
attempt to produce a boot loader for IBM PC-compatible machines that
has both the ability to be friendly to beginning or otherwise
nontechnically interested users and the flexibility to help experts in
diverse environments. It is compatible with Free/Net/OpenBSD and Linux.
It supports Win 9x/NT and OS/2 via chainloaders. It has a menu
interface and a command line interface.
It implements the Multiboot standard, which allows for flexible loading
of multiple boot images (needed for modular kernels such as the GNU
Hurd).

%prep
%setup -q -n grub2-%version
%setup -b 5 -n grub2-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p2
%patch8 -p1
%patch9 -p2

mv ../grub-extras-%version ./grub-extras

sed -i configure.ac -e "s/^AC_INIT.*/AC_INIT(\[GRUB\],\[%version-%release\],\[bug-grub@gnu.org\])/"

%build
export GRUB_CONTRIB=`pwd`/grub-extras
./autogen.sh
%configure --prefix=/ --disable-werror --with-platform=efi
%make_build

%install
export GRUB_CONTRIB=`pwd`/grub-extras
%makeinstall
mkdir -p %buildroot/etc/sysconfig
install -pD -m644 %SOURCE1 %buildroot/etc/sysconfig/grub2
%find_lang grub
mkdir -p %buildroot/boot/grub
%buildroot/%_bindir/grub-mkfont -o %buildroot/boot/grub/unifont.pf2 %_datadir/fonts/bitmap/misc/8x13.pcf.gz
install -pD -m755 %SOURCE3 %buildroot/etc/grub.d/
sed -i 's,^libdir=,libdir=%_libdir,g' %buildroot/etc/grub.d/39_memtest
sed -i 's,@LOCALEDIR@,%_datadir/locale,g' %buildroot/etc/grub.d/*
mkdir -p %buildroot/%_rpmlibdir
install -pD -m755 %SOURCE4 %buildroot/%_rpmlibdir/
install -pD -m755 %SOURCE6 %buildroot/%_sbindir/
mkdir -p %buildroot/%_sysconfdir/firsttime.d
install -pD -m755 %SOURCE7 %buildroot/%_sysconfdir/firsttime.d/grub-mkconfig

%files -f grub.lang
%dir %_sysconfdir/grub.d
%dir /boot/grub
/boot/grub/*.pf2
%_sysconfdir/grub.d/00_header
%_sysconfdir/grub.d/05_altlinux_theme
%_sysconfdir/grub.d/10_linux
%_sysconfdir/grub.d/20_linux_xen
%_sysconfdir/grub.d/30_os-prober
%_sysconfdir/grub.d/39_memtest
%config(noreplace) %_sysconfdir/grub.d/40_custom
%config(noreplace) /etc/sysconfig/grub2
%_sysconfdir/firsttime.d/*
%_bindir/*
%_libdir/grub
%_datadir/grub
%_sbindir/*
%_infodir/grub.info.*
%_infodir/grub-dev.info.*
%_rpmlibdir/*.filetrigger
%_man1dir/*.gz
%_man8dir/*.gz

%post
%_sbindir/grub-autoupdate

%changelog
* Fri May 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt9
- fix build with automake >= 1.11.2

* Mon Aug 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.99-alt8
- grub2-efi
