Name: scalpel
Version: 2.0
Release: alt1

Summary: A Frugal, High Performance File Carver
License: GPLv2+
Group: Text tools

Url: https://github.com/machn1k/Scalpel-2.0
Source0: %name-%version.tar.gz
Source1: scalpel.conf.odf

# Automatically added by buildreq on Sun Apr 13 2014
# optimized out: gnu-config libcloog-isl4
BuildRequires: libtre-devel

%description
Scalpel is a fast file carver that reads a database of header and footer
definitions and extracts matching files from a set of image files or raw
device files. Scalpel is filesystem-independent and will carve files from
FATx, NTFS, ext2/3/4, or raw partitions. It is useful for both digital
forensics investigation and file recovery.

%prep
%setup
sed -i 's|scalpel.conf|%_sysconfdir/&|' src/scalpel.h
chmod -x gpl.txt README Changelog src/*.h src/*.c
rm -f *.exe *.dll

# modify configuration to have some usable one out of box:
# everything is commented out within the stock file;
# this sed script uncomments common file extensions
sed -i -e "s/^#[ ]*$//;
           s/\t/        /g;
           s/^#   [ ]*\([a-z][a-z] \)/        \1/;
           s/^#   [ ]*\([a-z][a-z][a-z] \)/        \1/;
           s/^#   [ ]*\([a-z][a-z][a-z][a-z] \)/        \1/;
           s/^\(.*case[ ]*size\)/#\1/" %name.conf

# a few more more bits
cat %SOURCE1 >> scalpel.conf

%build
%configure
%make_build

%install
%makeinstall_std
install -pDm644 scalpel.conf %buildroot%_sysconfdir/scalpel.conf

%files
%config(noreplace) %_sysconfdir/scalpel.conf
%_bindir/*
%_man1dir/*

%changelog
* Sun Apr 13 2014 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- 2.0
  + NB: ODT/Thunderbird configuration "patch" used to work for 1.60,
    I don't know if it's still effective with 2.0
  + dropped patch
- updated Url:
- buildreq

* Wed Feb 29 2012 Michael Shigorin <mike@altlinux.org> 1.60-alt2
- added OpenDocument and Thunderbird patterns archived
  at http://ubuntuforums.org/showthread.php?p=9814022,
  originally from www.logicalprogressions.net/blog/tag/odt/
- minor spec tweaks

* Sat Mar 08 2008 Victor Forsyuk <force@altlinux.org> 1.60-alt1
- Initial build.
