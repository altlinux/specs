Name:		boot0
Version:	236712
Release:	alt1
Group:		System/Kernel and hardware
Summary:	1st-level bootloader used in FreeBSD distribution
License:	BSD
# see Makefile for real SVN source
Source:		%name-%version.tar
Url:		http://www.freebsd.org/cgi/cvsweb.cgi/src/sys/boot/i386/boot0/
Patch:		%name-%version-%release.patch


%description
The boot manager scans the partition table and prints the menu on the
screen so the user can select what disk and what slice to boot. By
pressing an appropriate key, boot0 performs the following actions:
    * modifies the bootable flag for the selected partition to make it
      bootable, and clears the previous
    * saves itself to disk to remember what partition (slice) has been
      selected so to use it as the default on the next boot
    * loads the first sector of the selected partition (slice) into
      memory and jumps there

%prep
%setup
%patch -p1

%build
%make

%install
%makeinstall

%files
%_sbindir/*
%_man8dir/*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 236712-alt1
- Version update

* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 196074-alt4
- Fix new binutils build

* Sat Aug 08 2009 Fr. Br. George <george@altlinux.ru> 196074-alt3
- Accidential clean(*argv) removed
- Linux version (LBA ext, LVM, SWAP and RAID suport)

* Thu Aug 06 2009 Fr. Br. George <george@altlinux.ru> 196074-alt2
- Add boot0ext, 1024-byte boot manager

* Thu Aug 06 2009 Fr. Br. George <george@altlinux.ru> 196074-alt1
- Initial build from scratch

