%define oname ddumbfs
Name: fuse-ddumbfs
Version: 1.1
Release: alt1

Summary: fast inline de-duplicating file system based on FUSE

License: GPL
Group: System/Kernel and hardware
Url: http://www.magiksys.net/ddumbfs

BuildRequires: libmhash-devel
BuildRequires: libfuse-devel
BuildRequires: pkg-config

Requires: fuse

# Source-url: http://www.magiksys.net/download/ddumbfs/%oname-%version.tar.gz
Source: %name-%version.tar

%description
ddumbfs is a fast inline deduplication filesystem for Linux based on FUSE
and released under the GNU GPL.
Deduplication is a technique to avoid data duplication on disks and to
increase its virtual capacity.
ddumbfs works at block level. Before to write a block to the filesystem
ddumbfs calculate its SHA1 or TIGER hash and search for it in the
index. If the block already exists the reference is used, if not, the
block is written and the index updated.
It is especially useful to store successive backup, when data are mostly
identical.
ddumbfs is especially efficient with backups of disk images or virtual
machines, when blocks stay aligned on a block boundary.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_man8dir/alterddumbfs.8
rm -rf %buildroot%_docdir/%oname-%version/

%files
%doc doc/MISC doc/TODO doc/Changelog
%_bindir/ddumbfs
%_bindir/mkddumbfs
%_bindir/fsckddumbfs
%_bindir/cpddumbfs
%_bindir/migrateddumbfs
%_man8dir/*

%changelog
* Mon Feb 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Dec 17 2012 Alain Spineux <alain.spineux@gmail.com> - 1.1-1
- added tools : migrateddumbfs
- updated description
- ran rpmlint
* Sun Nov  6 2011 Alain Spineux <alain.spineux@gmail.com> - 1.0b11-1
- update
* Fri May  6 2011 Alain Spineux <alain.spineux@gmail.com> - 0.4-1
- first release
