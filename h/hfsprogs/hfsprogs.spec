Name: hfsprogs
Version: 332.25
Release: alt1

Summary: mkfs and fsck for HFS and HFS+ file systems
Summary(ru_RU.UTF-8): Утилиты для работы с файловыми системами Linux

License: APSL
Group: System/Configuration/Hardware
Url: http://packages.debian.org/ru/sid/hfsprogs

Source: %name-%version.tar
Packager: Vitaly Lipatov <lav@altlinux.ru>

Patch0: 00-create_makefiles.patch
Patch1: 10-linux_specific_code.patch
Patch2: 20-apple_specific_files.patch
Patch3: 25-64-bit-fix.patch
Patch4: 30-formatting_strings.patch
Patch5: 40-printf_types.patch
Patch6: 50-typo-new_fs-manpage.diff
Patch7: 60-hfs-wrapper-boot-in-usr-share.diff
Patch8: 70-diskdev_cmds_system_check-332.14.patch
Patch9: 80-fix_manpages.patch
Patch10: 90-rename_dprintf.patch
Patch11: 91-remove-nils.patch
Patch12: 92-fix-types.patch

# Automatically added by buildreq on Fri Dec 16 2011
BuildRequires: libbsd-devel libssl-devel

%description
The HFS+ file system used by Apple Computer for their Mac OS is
supported by the Linux kernel.  Apple provides mkfs and fsck for
HFS+ with the Unix core of their operating system, Darwin.

This package is a port of Apple's tools for HFS+ filesystems.

 For users, HFS+ seems to be a good compromise to carry files between
 MacOS X and Linux Machines, as HFS+ doesn't suffer the problems of
 FAT32 like:

 * huge space waste (in slack space as devices grow faster);
 * ability to create files that are more than 4GB in size (especially
   good for those working with multimedia and that need to carry large
   ISO files);
 * ability to use case preserving (and even sensitivity!);
 * ability to use uid's and gid's on the filesystem.

Users in general can enjoy such benefits since it is expected to have
more HFS+ filesystems in use, as Apple has announced Macintoshes for
ix86-64, besides the filesystem being already supported by PowerPC
systems since the beginning.


%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%add_optflags -DDEBUG_BUILD=0 -D_FILE_OFFSET_BITS=64 -D LINUX=1 -D BSD=1 -I$(pwd)/include
%make_build -f Makefile.lnx CFLAGS="%optflags"

%install
mkdir -p %buildroot%_sbindir/ %buildroot%_man8dir/ %buildroot%_datadir/hfsbootdata/
install -m 644 newfs_hfs.tproj/hfsbootdata.img %buildroot%_datadir/hfsbootdata/
install -m 755 newfs_hfs.tproj/newfs_hfs   %buildroot%_sbindir/mkfs.hfsplus
install -m 755 fsck_hfs.tproj/fsck_hfs     %buildroot%_sbindir/fsck.hfsplus
install -m 644 newfs_hfs.tproj/newfs_hfs.8 %buildroot%_man8dir/mkfs.hfsplus.8
install -m 644 fsck_hfs.tproj/fsck_hfs.8   %buildroot%_man8dir/fsck.hfsplus.8

%files
%_sbindir/mkfs.hfsplus
%_sbindir/fsck.hfsplus
%_datadir/hfsbootdata/
%_man8dir/*

%changelog
* Fri Dec 16 2011 Vitaly Lipatov <lav@altlinux.ru> 332.25-alt1
- initial build for ALT Linux Sisyphus

