Name: partitionmanager
Version: 1.1.0
Release: alt1

Summary: KDE Partition Manager
License: GPL
Group: Graphical desktop/KDE

Url: https://www.kde.org/applications/system/kdepartitionmanager/

Packager: Evgeny V Shishkov <shev@altlinux.org>

Source: http://download.kde.org/stable/partitionmanager/1.1.0/src/%name-%version.tar.xz

Requires: kde4libs
BuildRequires(pre): kde4libs-devel

BuildRequires: gcc-c++ libblkid-devel libparted-devel libuuid-devel
BuildRequires: libatasmart-devel

%description
KDE Partition Manager is a utility program to help you manage the disk
devices, partitions and file systems on your computer. It allows you to
easily create, copy, move, delete, resize without losing data, backup and
restore partitions. KDE Partition Manager supports a large number of file
systems, including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.
It makes use of external programs to get its job done, so you might have
to install additional software (preferably packages from your
distribution) to make use of all features and get full support for all
file systems.

%prep
%setup

%build
%K4cmake -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix`
%K4make

%install
%K4install

%K4find_lang --with-kde %name

%files -f %name.lang
%_bindir/*
%_libdir/*.so
%_libdir/kde4/pmdummybackendplugin.so
%_libdir/kde4/pmlibpartedbackendplugin.so
%_desktopdir/kde4/%name.desktop
%_datadir/kde4/services/pmdummybackendplugin.desktop
%_datadir/kde4/services/pmlibpartedbackendplugin.desktop
%_datadir/kde4/servicetypes/pmcorebackendplugin.desktop
%_K4apps/%name/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_datadir/icons/hicolor/*x*/apps/%name.png
%_datadir/appdata/%name.appdata.xml

%changelog
* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for partitionmanager

* Mon Sep 06 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.0.3-alt1
- version 1.0.3

* Mon Apr 26 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.0.2-alt1
- Initial build

