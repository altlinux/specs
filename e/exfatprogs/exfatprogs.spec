%define _sbindir /sbin

Name: exfatprogs
Version: 1.2.0
Release: alt1

Summary:  Official utilities for exFAT file system
Group: System/Kernel and hardware
License: GPL-2.0
Url: https://github.com/exfatprogs/exfatprogs
Vcs: https://github.com/exfatprogs/exfatprogs.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: exfat-utils
Provides: %_sbindir/dump.exfat %_sbindir/exfatlabel %_sbindir/fsck.exfat
Provides: %_sbindir/mkfs.exfat %_sbindir/tune.exfat

%{?_enable_check:BuildRequires: losetup}
%description
As new exfat filesystem is merged into linux-5.7 kernel, exfatprogs is
created as an official userspace utilities that contain all of the standard
utilities for creating and fixing and debugging exfat filesystem in linux
system. The goal of exfatprogs is to provide high performance and quality
at the level of exfat utilities in windows.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_sbindir/dump.exfat
%_sbindir/exfatlabel
%_sbindir/fsck.exfat
%_sbindir/mkfs.exfat
%_sbindir/tune.exfat
%_sbindir/exfat2img
%_man8dir/*
%doc NEWS README*

%changelog
* Tue Nov 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Nov 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Thu May 20 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Thu May 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt2
- moved utilities to /sbin (ALT #40043)

* Thu May 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1.1
- Obsoletes: exfat-utils (ALT #40035)

* Wed Apr 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Feb 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Tue Jan 26 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

