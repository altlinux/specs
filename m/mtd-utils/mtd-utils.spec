Name: mtd-utils
Version: 1.5.0
Release: alt1

Summary: Tools for maintaining Memory Technology Devices
License: GPL
Group: System/Kernel and hardware
Url: http://www.linux-mtd.infradead.org/

Provides: mtd
Obsoletes: mtd

Source: %name-%version-%release.tar

BuildRequires: libacl-devel liblzma-devel liblzo2-devel libuuid-devel zlib-devel

%description
This package contains tools for erasing and formatting flash devices,
including JFFS2, M-Systems DiskOnChip devices, etc.

%prep
%setup

%build
%make_build

%install
make DESTDIR=%buildroot install

%files
%doc COPYING
%_sbindir/*
%_man1dir/mkfs.jffs2.*

%changelog
* Fri Jul 06 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Mon Apr 02 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.9-alt1
- 1.4.9 released
