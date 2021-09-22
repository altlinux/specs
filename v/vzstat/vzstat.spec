
Name: vzstat
Version: 7.0.25
Release: alt3
Summary: vzstat utility for node monitoring

Group: System/Base
License: GPLv2+
Url: https://src.openvz.org/projects/OVZ/repos/vzstat
Source: %name-%version.tar
Patch: %name-%version.patch
ExclusiveArch: x86_64

BuildRequires: libvzctl-devel
BuildRequires: libncurses-devel
BuildRequires: libuuid-devel
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0

%description
This package contains statistic monitoring utility for OpenVZ HW node.

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags -Wno-error=stringop-truncation -Wno-stringop-truncation -Wno-error=misleading-indentation"
%make_build

%install
%makeinstall_std MANDIR="%_mandir"

%files
%_sbindir/%name
%config(noreplace) %_sysconfdir/vz/%name.conf
%_man8dir/%name.*
%doc README.md COPYING

%changelog
* Wed Sep 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.25-alt3
- FTBFS: -Werror=misleading-indentation (gcc11)
- move ALT CFLAGS to spec

* Tue Mar 30 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.25-alt2
- fix FTBFS

* Wed Jul 01 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.25-alt1
- 7.0.25

* Fri Feb 07 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.24-alt1
- 7.0.24

* Mon Dec 02 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.21-alt1
- 7.0.21
- fix Licence
- suppress stringop-truncation error

* Mon Sep 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.20-alt1
- 7.0.20

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.19-alt1
- initial packaging

