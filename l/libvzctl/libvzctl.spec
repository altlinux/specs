
# %%define _without_vcmmd yes
%{?_without_vcmmd:%global _without_vcmmd --without-vcmmd}

Name: libvzctl
Summary: OpenVZ Containers API library
Version: 7.0.596
Release: alt1
License: LGPLv2.1
Group: System/Libraries
Url: https://openvz.org/
# git-vsc https://src.openvz.org/scm/ovzl/libvzctl.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

Requires: libvzevent >= 7.0.0
Requires: libploop >= 7.0.199
Requires: cgroup
Requires: crtools >= 2.8.0.15
BuildRequires: kernel-headers-ovz-el7 >= 3.10.0
BuildRequires: libvzevent-devel >= 5.0.0
BuildRequires: libploop-devel >= 7.0.199
BuildRequires: libe2fs-devel
BuildRequires: libxml2-devel >= 2.6.16
BuildRequires: libuuid-devel
BuildRequires: libdbus-devel

%if 0%{!?_without_vcmmd:1}
Requires: libvcmmd >= 7.0.22
BuildRequires: libvcmmd-devel >= 7.0.22
%endif

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
%configure %{?_without_vcmmd}
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
* Tue Jul 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.596-alt1
- 7.0.596

* Tue Jul 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.592-alt1
- 7.0.592
- ability to build without vcmmd

* Wed Jun 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.590-alt1
- 7.0.590

* Wed Jun 17 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.588-alt1
- 7.0.588

* Wed May 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.583-alt1
- 7.0.583

* Wed May 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.580-alt1
- 7.0.580

* Sat Apr 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.578-alt1
- 7.0.578

* Mon Apr 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.574-alt1
- 7.0.574

* Wed Apr 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.571-alt1
- 7.0.571

* Tue Mar 31 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.568-alt1
- 7.0.568
- remove with_ub due to autodetect of UB

* Tue Mar 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.567-alt1
- 7.0.567

* Thu Mar 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.566-alt1
- 7.0.566

* Wed Mar 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.564-alt1
- 7.0.564

* Tue Mar 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.563-alt1
- 7.0.563

* Thu Feb 27 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.561-alt1
- 7.0.561

* Wed Feb 12 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.560-alt1
- 7.0.560

* Mon Feb 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.558-alt1
- 7.0.558

* Fri Jan 31 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.556-alt1
- 7.0.556

* Tue Jan 28 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.555-alt1
- 7.0.555

* Wed Jan 22 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.553-alt1
- 7.0.553

* Wed Jan 22 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.552-alt2
- modify scripts for networkd

* Tue Dec 17 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.552-alt1
- 7.0.552

* Tue Dec 10 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.551-alt1
- 7.0.551

* Mon Dec 09 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.550-alt1
- 7.0.550

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
