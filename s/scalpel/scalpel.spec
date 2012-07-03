Name: scalpel
Version: 1.60
Release: alt2

Summary: A Frugal, High Performance File Carver
License: GPLv2+
Group: Text tools

Url: http://www.digitalforensicssolutions.com/Scalpel/
Source0: %url/scalpel-%version.tar.gz
Source1: scalpel.conf.odf
Patch: scalpel-1.60-configfile.patch

%description
Scalpel is a fast file carver that reads a database of header and footer
definitions and extracts matching files from a set of image files or raw
device files. Scalpel is filesystem-independent and will carve files from
FATx, NTFS, ext2/3/4, or raw partitions. It is useful for both digital
forensics investigation and file recovery.

%prep
%setup
%patch -p1
cat %SOURCE1 >> scalpel.conf

%build
sed -i 's|scalpel.conf|%_sysconfdir/&|' scalpel.h
sed -i 's/$(CC) -c/$(CC) %optflags -c/' Makefile
%make_build

%install
install -pD -m755 scalpel %buildroot%_bindir/scalpel
install -pD -m644 scalpel.1 %buildroot%_man1dir/scalpel.1
install -pD -m644 scalpel.conf %buildroot%_sysconfdir/scalpel.conf

%files
%config(noreplace) %_sysconfdir/scalpel.conf
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 29 2012 Michael Shigorin <mike@altlinux.org> 1.60-alt2
- added OpenDocument and Thunderbird patterns archived
  at http://ubuntuforums.org/showthread.php?p=9814022,
  originally from www.logicalprogressions.net/blog/tag/odt/
- minor spec tweaks

* Sat Mar 08 2008 Victor Forsyuk <force@altlinux.org> 1.60-alt1
- Initial build.
