Summary: The EXTLINUX bootloader, for booting the local system.
Name: extlinux
Version: 4.05
Release: alt1
License: GPL2
Group: System/Base
Url: http://www.syslinux.org/wiki/index.php/The_Syslinux_Project
Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Source1: configs.tar
Source2: extlinux.sysconfig
Source3: extlinux-config
Source4: extlinux.filetrigger

Patch0:  syslinux-global-append.patch
Patch1:  syslinux-addappend-directive.patch
Patch2:  syslinux-use-ext2fs.patch
Patch3:  syslinux-fix-isohybrid.patch

BuildRequires: libe2fs-devel libuuid-devel nasm python-module-distribute

Requires: libshell util-linux parted

Obsoletes: syslinux4-extlinux
Provides: syslinux4-extlinux = %version-%release

%description
The EXTLINUX bootloader, for booting the local system, as well as all
the SYSLINUX/PXELINUX modules in /boot.

%package doc
Summary: Extlinux documentation.
Group: Documentation

%description doc
Extlinux documentation.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -rf mk/devel.mk
make

%install
make extbootinstall \
	INSTALLROOT="%buildroot" \
	EXTLINUXDIR=/boot/extlinux

cp -a mbr/*mbr.bin %buildroot/boot/extlinux/

mkdir -p -- %buildroot/%_sysconfdir/sysconfig \
            %buildroot/%_rpmlibdir \
            %buildroot/%_man1dir \
            %buildroot/sbin \
            %buildroot/boot

install -m644 man/extlinux.1 %buildroot/%_man1dir/
install -m644 %SOURCE2 %buildroot/%_sysconfdir/sysconfig/extlinux
install -m755 extlinux/extlinux %buildroot/sbin/
install -m755 %SOURCE3 %buildroot/sbin/
install -m755 %SOURCE4 %buildroot/%_rpmlibdir/

tar -C %buildroot/boot/extlinux -xf %SOURCE1

cd %buildroot/boot
ln -s . boot

cd %buildroot/%_sysconfdir
ln -s ../boot/extlinux/extlinux.conf   .
ln -s ../boot/extlinux/extlinux.conf.d .

%pre
[ ! -L /sbin/extlinux-config ] || rm -f -- /sbin/extlinux-config

%post
[ "$1" = 1 ] || /sbin/extlinux-config

%files
%config(noreplace) /boot/extlinux/extlinux.conf
%config(noreplace) /boot/extlinux/extlinux.conf.d/*.conf
%config(noreplace) %_sysconfdir/sysconfig/extlinux
%_sysconfdir/extlinux.conf
%_sysconfdir/extlinux.conf.d
/boot/boot
/boot/extlinux
/sbin/extlinux
/sbin/extlinux-config
%_rpmlibdir/*
%_man1dir/*

%files doc
%doc COPYING NEWS doc/*
%doc sample

%changelog
* Thu May 24 2012 Alexey Gladkov <legion@altlinux.ru> 4.05-alt1
- New release (4.05).
- There is only a bootloader.
- extlinux-config: Add gpt support.

* Fri Dec 24 2010 Alexey Gladkov <legion@altlinux.ru> 4.03-alt6
- extlinux-config: Fix root device detection.

* Thu Nov 25 2010 Alexey Gladkov <legion@altlinux.ru> 4.03-alt5
- New release (4.03).

* Fri Oct 01 2010 Alexey Gladkov <legion@altlinux.ru> 4.03-alt4
- extlinux-config: Add --root option.

* Fri Sep 24 2010 Alexey Gladkov <legion@altlinux.ru> 4.03-alt3
- Package docs in a seperate package (ALT#24151).
- Add symlink to /boot (ALT#24150).
- Move extlinux-config to /sbin (ALT#24149).

* Wed Sep 22 2010 Alexey Gladkov <legion@altlinux.ru> 4.03-alt2
- Fix extlinux-config.
- Add mbr.bin to extlinux.

* Thu Sep 09 2010 Alexey Gladkov <legion@altlinux.ru> 4.03-alt1
- Initial build.

