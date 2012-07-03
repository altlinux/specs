Name: vblade
Version: 19
Release: alt1

Summary: Virtual EtherDrive (R) blade daemon
Group: System/Kernel and hardware
License: GPLv2

Url: http://sourceforge.net/projects/aoetools/
Packager: Alexander Volkov <vaa@altlinux.org>
Source: http://dl.sf.net/aoetools/%name-%version.tgz
Source1: %name.init
Source2: %name.conf
Patch0: %name-makefile.patch

%description
The vblade is the virtual EtherDrive (R) blade, a program that makes a
seekable file available over an ethernet local area network (LAN) via
the ATA over Ethernet (AoE) protocol.

The seekable file is typically a block device like /dev/md0 but even
regular files will work.  When vblade exports the block storage over
AoE it becomes a storage target.  Another host on the same LAN can
access the storage if it has a compatible aoe kernel driver.

%prep
%setup -q
%patch0 -p1

%build
%make

%install
%makeinstall_std
#mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot/var/run/%name
mkdir -p %buildroot%_initdir
install -D -m755 %SOURCE1 %buildroot%_initdir/%name
install -D -m644 %SOURCE2 %buildroot%_sysconfdir/%name.conf

%preun
%preun_service %name
%post
%post_service %name

%files
%doc COPYING HACKING NEWS README
%config(noreplace) %_sysconfdir/%name.conf
%dir /var/run/%name
%_initdir/%name
%_sbindir/vblade
%_sbindir/vbladed
%_man8dir/vblade.8*

%changelog
* Sat Oct 25 2008 Alexander Volkov <vaa@altlinux.org> 19-alt1
- New build for ALT

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 14-4
- Bump-n-build for GCC 4.3

