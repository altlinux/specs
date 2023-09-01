Name: mtd-utils
Version: 2.1.6
Release: alt1

Summary: Tools for maintaining Memory Technology Devices
License: GPLv2
Group: System/Kernel and hardware
Url: http://www.linux-mtd.infradead.org/

Source: %name-%version-%release.tar

BuildRequires: libacl-devel liblzo2-devel libssl-devel libuuid-devel libzstd-devel zlib-devel

%description
This package contains tools for erasing and formatting flash devices,
including JFFS2, M-Systems DiskOnChip devices, etc.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%_sbindir/*
%_libexecdir/mtd-utils
%_man1dir/mkfs.jffs2.*
%_man8dir/lsmtd.*
%_man8dir/ubinize.*

%changelog
* Fri Sep 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.6-alt1
- 2.1.6 released

* Mon Oct 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.5-alt1
- 2.1.5 released

* Mon Feb 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.4-alt1
- 2.1.4 released

* Mon Jul 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.3-alt1
- 2.1.3 released

* Mon Apr 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.2-alt2
- fixed 2G+ mtd devices handling

* Mon Jul 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.2-alt1
- 2.1.2 released

* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- 2.1.1 released

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2
- backport some patches from upstream master

* Fri Jul 06 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Mon Apr 02 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.9-alt1
- 1.4.9 released
