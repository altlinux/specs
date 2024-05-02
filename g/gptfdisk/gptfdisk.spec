Name: gptfdisk
Version: 1.0.10
Release: alt1

Summary: GPT partitioning and MBR repair software
License: GPLv2
Group: System/Configuration/Hardware

Url: https://www.rodsbooks.com/gdisk
Source: %name-%version.tar
# GIT: git://git.code.sf.net/p/gptfdisk/code

BuildRequires(pre): rpm-macros-make
BuildRequires: gcc-c++ libuuid-devel libpopt-devel libncursesw-devel

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
%make_ext

%check
./gdisk_test.sh

%install
mkdir -p %buildroot{%_sbindir,%_man8dir}
install -pm755 [^u]*disk fixparts %buildroot%_sbindir/
install -pm644 *.8 %buildroot%_man8dir/

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
* Thu May 02 2024 Alexey Shabalin <shaba@altlinux.org> 1.0.10-alt1
- 1.0.10

* Wed Oct 05 2022 Alexey Shabalin <shaba@altlinux.org> 1.0.9.1-alt1
- Fix NULL dereference when duplicating string argument (ALT#43956)

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.0.9-alt1
- 1.0.9

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.8-alt1
- 1.0.8 (Fixes: CVE-2020-0256, CVE-2021-0308)

* Tue Jun 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.5-alt1
- 1.0.5

* Mon Jan 11 2016 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1
  + upstream dropped cgdisk
- don't build with libicu (huge runtime deps, unneeded as of 0.8.9)
- minor spec cleanup

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.11-alt1.git20140329
- Version 0.8.11

* Sun Jan 05 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.8-alt1
- New version

* Mon Oct 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7-alt1.git.e3ee733f
- New version snapshot

* Tue Feb 19 2013 Michael Shigorin <mike@altlinux.org> 0.8.6-alt1
- New version

* Thu Aug 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.5-alt1
- New version

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

