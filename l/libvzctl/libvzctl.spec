
# %%define _without_vcmmd yes
%{?_without_vcmmd:%global _without_vcmmd --without-vcmmd}

Name: libvzctl
Summary: OpenVZ Containers API library
Version: 7.0.726
Release: alt2
License: LGPLv2.1
Group: System/Libraries
Url: https://openvz.org/
Vcs: https://src.openvz.org/scm/ovzl/libvzctl.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64

Requires: libvzevent >= 7.0.0
Requires: libploop >= 7.0.199
Requires: cgroup
Requires: crtools-ovz >= 3.15.0.9
Requires: e2fsprogs gdisk iputils iproute2
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
export CFLAGS="%optflags -Wno-error=format-truncation -Wno-error=stringop-truncation -Wno-error=format-overflow -Wno-error=stringop-overflow"
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
* Wed Feb 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.0.726-alt2
- set_dns.sh: restore previous resolver choice

* Tue Feb 21 2023 Andrew A. Vasilyev <andy@altlinux.org> 7.0.726-alt1
- 7.0.726
- set_dns.sh: optimize and clear syntax

* Sat Dec 10 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.723-alt1
- 7.0.723

* Mon Nov 14 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.719-alt1
- 7.0.719

* Wed Oct 26 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.717-alt1
- 7.0.717

* Tue Jun 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.714-alt1
- 7.0.714

* Wed Jun 01 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.713-alt1
- 7.0.713

* Thu May 12 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.0.711-alt1
- 7.0.711

* Sat Nov 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.707-alt1
- 7.0.707

* Tue Oct 05 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.700-alt1
- 7.0.700

* Wed Sep 22 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.698-alt1
- 7.0.698
- move all ALT CFLAGS to spec
- fix -Warray-parameter in vzctl2_env_open_conf() declaration (gcc11)

* Fri Sep 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.697-alt1
- 7.0.697

* Wed Sep 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.689-alt1
- 7.0.689
- fix openvswitch dependency

* Thu Aug 05 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.678-alt1
- 7.0.678

* Wed Jul 28 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.674-alt1
- 7.0.674

* Thu Jul 15 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.671-alt1
- 7.0.671

* Tue Jul 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.664-alt2
- use "ip link" instead of brctl, no deps on bridge-utils now

* Thu Jul 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.664-alt1
- 7.0.664

* Wed Jun 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.659-alt1
- 7.0.659

* Mon Apr 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.651-alt1
- 7.0.651

* Fri Mar 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.648-alt1
- 7.0.648

* Fri Mar 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.647-alt1
- 7.0.647

* Mon Mar 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.645-alt1
- 7.0.645

* Wed Feb 10 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.641-alt1
- 7.0.641

* Thu Feb 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.640-alt1
- 7.0.640

* Sun Jan 31 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.639-alt2
- change resolver configuration for systemd
- remove default NS from systemd-networkd config
- change route command to "ip route" call

* Tue Jan 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.639-alt1
- 7.0.639

* Tue Dec 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.633-alt1
- 7.0.633

* Thu Dec 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.632-alt1
- 7.0.632

* Thu Nov 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.629-alt1
- 7.0.629

* Sat Oct 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.628-alt1
- 7.0.628

* Tue Oct 06 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.625-alt1
- 7.0.625

* Fri Oct 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.623-alt1
- 7.0.623
- add explicit requirements on e2fsprogs, gdisk and iputils packages

* Wed Sep 30 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.619-alt2
- change criu to criu-ovz in scripts

* Thu Sep 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.619-alt1
- 7.0.619

* Fri Sep 18 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.618-alt1
- 7.0.618

* Mon Sep 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.617-alt1
- 7.0.617
- R: crtools-ovz

* Thu Sep 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.616-alt1
- 7.0.616

* Fri Sep 04 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.614-alt1
- 7.0.614

* Fri Aug 28 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.605-alt1
- 7.0.605

* Tue Aug 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.604-alt1
- 7.0.604

* Mon Aug 03 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.601-alt1
- 7.0.601

* Fri Jul 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 7.0.598-alt1
- 7.0.598

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
