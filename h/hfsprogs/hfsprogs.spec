Name: hfsprogs
Version: 540.1.linux3
Release: alt1

Summary: mkfs and fsck for Apple HFS and HFS+ file systems
Summary(ru_RU.UTF-8): Утилиты для работы с файловыми системами Linux

License: APSL 2.0
Group: System/Configuration/Hardware
Url: http://gentoo-wiki.com/HOWTO_hfsplus

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: https://opensource.apple.com/tarballs/diskdev_cmds/diskdev_cmds-%version.tar.gz
# Source-url: http://cavan.codon.org.uk/~mjg59/diskdev_cmds/diskdev_cmds-%version.tar.gz
Source: %name-%version.tar

Source100: apsl-2.0.txt

# those tools are outdated, given the rebuilt mkfs/fsck.hfsplus in this
# package.  However, I don't want to Obsolete that package yet, as some people
# may have a valid use for it on their systems. 
Conflicts: hfsplusutils

Patch0: hfsplus-tools-no-blocks.patch
Patch1: hfsplus-tools-learn-to-stdarg.patch

BuildRequires: libuuid-devel libssl-devel

# we want this to end up with the other mkfs.*'s, in /sbin
%define _exec_prefix /

%description
HFS+, HFS Plus, or Mac OS Extended are names for a file system developed by
Apple Computer to replace their Hierarchical File System (HFS). In addition to
being the default file system on modern Apple computers, HFS+ is one of two
formats, FAT being the other, that are supported by the iPod hard-disk based
music player. Unlike FAT, HFS+ supports UNIX style file permissions, which
makes it useful, for serving and sharing files in a secured manner. As Apple
Computer's devices and systems become increasingly ubiquitous, it becomes
important that Linux fully support this format.  This package provides tools
to create and check HFS+ filesystems under Linux.

The Linux kernel does not support writing to HFS+ journals, writing to a
hfsplus partition is recommended only after disabling journaling; however, the
kernel, as of version 2.6.16, supports case-sensitivity (also known as HFSX)
commit.


%prep
%setup
%patch0 -p1
%patch1 -p1

# remove errant execute bits
find . -type f -name '*.[ch]' -exec chmod -c -x {} +

# make life easier on doc
cp %{SOURCE100} .


%build
export CFLAGS="%{optflags}"
%make_build -f Makefile

%install
mkdir -p %buildroot%_sbindir/
#mkdir -p %buildroot%_datadir/hfsbootdata/
#install -m 644 newfs_hfs.tproj/hfsbootdata.img %buildroot%_datadir/hfsbootdata/

install -m 755 newfs_hfs.tproj/newfs_hfs   %buildroot%_sbindir/mkfs.hfsplus
install -m 755 fsck_hfs.tproj/fsck_hfs     %buildroot%_sbindir/fsck.hfsplus

# man pages -- a mildly non-invasive name change is in order
mkdir -p %{buildroot}/%{_mandir}/man8
cat fsck_hfs.tproj/fsck_hfs.8 | sed -e 's/[F|f]sck_hfs/fsck.hfsplus/g' \
    > %{buildroot}/%{_mandir}/man8/fsck.hfsplus.8
cat newfs_hfs.tproj/newfs_hfs.8 | sed -e 's/[N|n]ewfs_hfs/mkfs.hfsplus/g' \
    > %{buildroot}/%{_mandir}/man8/mkfs.hfsplus.8

# and a utility symlink...
cd %{buildroot}/%{_sbindir}
ln -s fsck.hfsplus fsck.hfs
cd %{buildroot}/%{_mandir}/man8
ln -s fsck.hfsplus.8 fsck.hfs.8


%files
%doc apsl-2.0.txt
%_sbindir/mkfs.hfsplus
%_sbindir/fsck.hfsplus
%_sbindir/fsck.hfs
%_man8dir/mkfs.hfsplus.*
%_man8dir/fsck.hfsplus.*
%_man8dir/fsck.hfs.*

%changelog
* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 540.1.linux3-alt1
- new version 540.1.linux3 (thanks, Fedora!)

* Tue Jul 31 2012 Vitaly Lipatov <lav@altlinux.ru> 332.25-alt2
- fix build: disable FORTIFY_SOURCE

* Fri Dec 16 2011 Vitaly Lipatov <lav@altlinux.ru> 332.25-alt1
- initial build for ALT Linux Sisyphus


