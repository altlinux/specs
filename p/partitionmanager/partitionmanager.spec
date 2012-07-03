Name: 		partitionmanager
Version: 	1.0.3
Release: 	alt1.qa1

Summary: 	KDE Partition Manager
License: 	GPL
Group: 		Graphical desktop/KDE

Url: 		http://sourceforge.net/projects/partitionman/

Packager: Evgeny V Shishkov <shev@altlinux.org>

Source0: %name-%version.tar.bz2

Requires: kde4libs
BuildRequires(pre): kde4libs-devel

# Automatically added by buildreq on Mon Apr 26 2010
BuildRequires: gcc-c++ libblkid-devel libparted-devel libuuid-devel

%description
KDE Partition Manager is a utility program to help you manage the disk devices, partitions and
file systems on your computer. It allows you to easily create, copy, move, delete, resize without
losing data, backup and restore partitions.
KDE Partition Manager supports a large number of file systems, including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.
It makes use of external programs to get its job done, so you might have to install additional software
(preferably packages from your distribution) to make use of all features and get full support for all file systems.

%prep
%setup

%build
%K4cmake -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix`
%K4make

%install
%K4install

%K4find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/*.so
%_desktopdir/kde4/%name.desktop
%_K4apps/%name/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for partitionmanager

* Mon Sep 06 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.0.3-alt1
- version 1.0.3

* Mon Apr 26 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.0.2-alt1
- Initial build

