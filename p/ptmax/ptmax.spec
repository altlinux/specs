Name: ptmax
Version: 2018
Release: alt1

Summary: Maximize partition in partition table to include it's trailing unallocated space

Group: System/Configuration/Hardware
License: GPL
Url: https://github.com/amarao/ptmax

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/amarao/ptmax.git
Source: %name-%version.tar

%description
Anyone, who have tried to resize a partition with LVM's PV on it do know
that felling: What the hell, we are dealing with a 64-bytes 35-years
old fixed size structure with bunch of INTs and still CAN NOT JUST
RESIZE partiton.

All existing utilities looks grim. Fdisk allows us to do this, but with
'DELETE and CREATE' (if you miss numbers, you are fckd up), parted says
it don't know how to do with LVM partition and so on.

If we had an 'old plain spinning drive' with misarranged paritions, we can
say: 'think before creating'. Because bare metall hard drives don't scale.

But now we live in the world of virtual machines, iscsi, LVM, MD which
offers way to 'change disk size in 2 clicks'. And what the hell you are
supposed to do after drive (block device) size changed, but the partition
table is still the same?

Yep. This utility partially solve the problem. It takes parition name
(/dev/sda1, /dev/xvda2 and so on) and attemts to maximize partition. Only
4 bytes in partition table (size filed), nothing more. After that you
can run pvreze, or resize2fs, or whatever, to reflect the change on a
higher level.

Usage is pertty simple:

ptmax /dev/sda3

That's all.

It cautious to avoid doing do bad things, so it will max partition
size only if PT is sane  and there is a free space after the targeted
partition. It will not move partitions, attempt to use leading
unpartitioned space, change the partition number, or alter in any other
way the original partitioning schema or data inside partition.

Currently there is no support for CHS, LBA only (?), so don't try it on
<32Mb partitions.

See also http://habrahabr.ru/company/selectel/blog/139152/

%prep
%setup
subst 's|^.*strip %name||g' Makefile

%build
%make_build

%install
#makeinstall_std
install %name -D %buildroot%_sbindir/%name

%files
%doc README.MD
%_sbindir/%name

%changelog
* Tue Jan 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2018-alt1
- git-20180130 (fix function "ioctl" declared implicitly)

* Sun Jan  3 2016 Terechkov Evgenii <evg@altlinux.org> 2015-alt2
- Build with debuginfo

* Tue Dec  8 2015 Terechkov Evgenii <evg@altlinux.org> 2015-alt1
- git-20151208

* Wed Feb 12 2014 Vitaly Lipatov <lav@altlinux.ru> 2012-alt1
- add support for cciss device names
- use sysfs to detect correct device parent name

* Wed Mar 28 2012 Vitaly Lipatov <lav@altlinux.ru> 2011-alt1
- initial build for ALT Linux Sisyphus
