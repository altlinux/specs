Summary: GPT partitioning and MBR repair software
Name: gptfdisk
Version: 0.8.1
Release: alt1
License: GPLv2
Group: System/Configuration/Hardware
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
URL: http://www.rodsbooks.com/gdisk
Source: http://www.rodsbooks.com/gdisk/%name-%version.tar.gz

BuildRequires: gcc-c++ libuuid-devel libpopt-devel libicu-devel ncurses-devel

%description
Partitioning software for GPT disks and to repair MBR
disks. The gdisk and sgdisk utilities (in the gdisk
package) are GPT-enabled partitioning tools; the
fixparts utility (in the fixparts package) fixes some
problems with MBR disks that can be created by buggy
partitioning software.

%package -n gdisk
Group: System/Configuration/Hardware
Summary: An fdisk-like partitioning tool for GPT disks

%description -n gdisk
An fdisk-like partitioning tool for GPT disks. GPT
fdisk features a command-line interface, fairly direct
manipulation of partition table structures, recovery
tools to help you deal with corrupt partition tables,
and the ability to convert MBR disks to GPT format.

%package -n cgdisk
Group: System/Configuration/Hardware
Summary: A ncurses-based GUID partition table (GPT) manipulator

%description -n cgdisk
A ncurses-based GUID partition table (GPT) manipulator.

%package -n fixparts
Group: System/Configuration/Hardware
Summary: A tool for repairing certain types of damage to MBR disks

%description -n fixparts
A program that corrects errors that can creep into MBR-partitioned
disks. Removes stray GPT data, fixes mis-sized extended partitions,
and enables changing primary vs. logical partition status. Also
provides a few additional partition manipulation features.

%prep
%setup

%build
%make

%install
install -D gdisk %buildroot%_sbindir/gdisk
install -D sgdisk %buildroot%_sbindir/sgdisk
install -D cgdisk %buildroot%_sbindir/cgdisk
install -D fixparts %buildroot%_sbindir/fixparts
install -D gdisk.8 %buildroot%_man8dir/gdisk.8
install -D sgdisk.8 %buildroot%_man8dir/sgdisk.8
install -D cgdisk.8 %buildroot%_man8dir/cgdisk.8
install -D fixparts.8 %buildroot%_man8dir/fixparts.8

%files -n gdisk
%doc NEWS COPYING README
%_sbindir/gdisk
%_sbindir/sgdisk
%_man8dir/gdisk*
%_man8dir/sgdisk*

%files -n cgdisk
%_sbindir/cgdisk
%_man8dir/cgdisk*

%files -n fixparts
%doc NEWS COPYING README
%_sbindir/fixparts
%_man8dir/fixparts*


%changelog
* Sat Oct 08 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.1-alt1
- New version
- Add subpackage cgdisk

* Sun Jul 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- New version

* Thu Mar 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.0-alt1
- New version
- Rename main package from gdisk -> gptfdisk
- Add 2 subpackage gdisk and fixparts

* Wed Jan 12 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.14-alt1
- New version

* Sun Sep 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.11-alt1
- New version

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.10-alt1
- New version

* Wed Aug 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.9-alt1
- New version

* Tue Feb 09 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.6.3-alt1
- New version
- Add sgdisk
- Apdate BuildRequires

* Fri Jan 15 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.3-alt1
- New version

* Fri Dec 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.1-alt1
- New version

* Mon Oct 12 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.0-alt2
- Add URL
- Update spec

* Fri Oct 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.0-alt1
- Build for ALT

