
Name: libvzctl
Summary: OpenVZ Containers API library
Version: 7.0.548
Release: alt1
License: LGPLv2.1
Group: System/Libraries
Url: https://openvz.org/
# git-vsc https://src.openvz.org/scm/ovzl/libvzctl.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

Requires: libvzevent >= 7.0.0
Requires: libploop >= 7.0.92
Requires: cgroup
Requires: crtools >= 2.8.0.15
Requires: libvcmmd >= 7.0.22
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0
BuildRequires: libvzevent-devel >= 5.0.0
BuildRequires: libploop-devel >= 7.0.92
BuildRequires: libvcmmd-devel >= 7.0.14
BuildRequires: libe2fs-devel
BuildRequires: libxml2-devel >= 2.6.16
BuildRequires: libuuid-devel
BuildRequires: libdbus-devel

%def_with ub

%add_findreq_skiplist %_datadir/%name/dists/scripts/*
%filter_from_requires /^\/etc\/vz\/vz.conf/d
%define _pkglibdir %_libdir/%name

%description
OpenVZ Containers API library

%package devel
Summary: OpenVZ Containers API development library
Group: Development/C
License: LGPLv2.1
Requires: %name  = %version-%release

%description devel
OpenVZ Containers API development library

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure %{subst_with ub}
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_pkglibdir
%_datadir/%name

%files devel
%_libdir/*.so
%_includedir/vzctl

%changelog
* Fri Dec 06 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.548-alt1
- 7.0.548

* Thu Nov 14 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.545-alt5
- fix criu scripts path
- spec cleanup

* Fri Nov 08 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.545-alt4
- fix broken Requires

* Wed Nov 06 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.545-alt3
- revert 1d53de2b265fe21c7df7bc to lower diff with upstream

* Wed Nov 06 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.545-alt2
- fix USE_UB absence

* Tue Nov 05 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.545-alt1
- 7.0.545

* Fri Nov 01 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.544-alt1
- 7.0.544
- fix /sbin/blkid path

* Fri Oct 25 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.540-alt1
- 7.0.540

* Wed Oct 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.539-alt1
- 7.0.539

* Wed Oct 16 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.538-alt2
- add/remove device for systemd/networkd service

* Mon Oct 14 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.538-alt1
- 7.0.538
- fix /sbin/ip path

* Mon Oct 07 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.537-alt1
- 7.0.537

* Thu Sep 12 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.536-alt3
- fix systemd-networkd discovery

* Tue Sep 03 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.536-alt2
- add interface and IPs for networkd

* Mon Aug 26 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.536-alt1
- 7.0.536

* Fri Aug 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.535-alt2
- fixed alt scripts
- fixed arping full path
- fixed awk regexp warning

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.535-alt1
- 7.0.535

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.499-alt1
- 7.0.499

* Mon Feb 19 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.463-alt1
- Initial build
