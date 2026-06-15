%filter_from_requires /\/etc\/mellanox\/mlnx-ovs.conf/d
%filter_from_requires /\/etc\/mellanox\/mlnx-sf.conf/d
%filter_from_requires /\/etc\/mellanox\/mlnx-bf.conf/d
%filter_from_requires /systemd/d
%filter_from_requires /\/bin\/systemctl/d
%filter_from_requires /\/sbin\/systemctl/d
%filter_from_requires \/sbin\/sysctl/d
%filter_from_requires \/etc\/sysconfig/d
%filter_from_requires /\/etc\/mlnx-release/d

%define _udevrulesdir /lib/udev/rules.d
%define _udevdir /lib/udev

Name: mlnx-tools
Version: 2607.0.1
Release: alt1

Summary: Mellanox userland tools and scripts

License: BSD-style or CPL-1.0 or GPL-2.0-only and GPL-2.0-or-later and MIT
Group: System/Kernel and hardware
Url: https://github.com/Mellanox/mlnx-tools
Vcs: https://github.com/Mellanox/mlnx-tools

# Source-url: https://github.com/Mellanox/mlnx-tools/releases/download/v%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel python3-devel
Requires: python3-module-termcolor python3-module-anytree
# python3-module-mlnx includes dcbnetlink
%add_python3_req_skip dcbnetlink
Requires: python3-module-mlnx

%description
Mellanox userland tools and scripts

%package -n python3-module-mlnx
Summary: Python3 bindings for %name
Group: Development/Python3

%description -n python3-module-mlnx
The package provides python3 bindings for %name.

%prep
%setup -n %name-%version
%autopatch -p1
sed -e 's|/usr/share/mlnx-tools/python|%python3_sitelibdir/%name|g' \
    -i Makefile \
    -i python/Python/dcbnetlink.py \
    -i python/mlnx_qos
sed -e 's|/usr/bin/env python3|%__python3|;' \
    -i $(find ./python -type f -print) \
    -i tsbin/mlnx-sf \
    -i tsbin/doca-hugepages
sed -e 's|openvswitch-switch|openvswitch|g;' \
    -e 's|/usr/lib/systemd/system|%_unitdir|;' \
    -i tsbin/mlnx_bf_configure

%install
%makeinstall_std
chmod +x %buildroot%python3_sitelibdir/%name/dcbnetlink.py

%files
%doc doc/* COPYING LICENSE README.md debian/changelog
/sbin/sysctl_perf_tuning
/sbin/mlnx_bf_configure
/sbin/mlnx-sf
/sbin/doca-hugepages
/lib/udev/mlnx_bf_udev
%_sbindir/*
%_bindir/*
%_man8dir/ib2ib_setup.8*
%_man8dir/mlnxofedctl.8*

%files -n python3-module-mlnx
%python3_sitelibdir/%name/

%changelog
* Mon Jun 15 2026 Leontiy Volodin <lvol@altlinux.org> 2607.0.1-alt1
- New version 2607.0.1 (2604.0.18).

* Fri Jun 05 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.17-alt1
- New version 2604.0.17.

* Fri May 08 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.16-alt1
- New version 2604.0.16.

* Wed Apr 29 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.15-alt1
- New version 2604.0.15.

* Mon Apr 27 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.13-alt1
- New version 2604.0.13.

* Wed Apr 22 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.12-alt1
- New version 2604.0.12.

* Mon Apr 13 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.11-alt1
- New version 2604.0.11.

* Thu Mar 26 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.10-alt1
- New version 2604.0.10.

* Tue Mar 24 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.9-alt1
- New version 2604.0.9.

* Fri Mar 20 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.7-alt1
- New version 2604.0.7.

* Tue Mar 17 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.6-alt1
- New version 2604.0.6.

* Tue Mar 10 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.5-alt1
- New version 2604.0.5.

* Thu Mar 05 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.3-alt1
- New version 2604.0.3.

* Mon Mar 02 2026 Leontiy Volodin <lvol@altlinux.org> 2604.0.2-alt1
- New version 2604.0.2.

* Thu Feb 19 2026 Leontiy Volodin <lvol@altlinux.org> 2601.0.4-alt1
- New version 2601.0.4.

* Fri Feb 06 2026 Leontiy Volodin <lvol@altlinux.org> 2601.0.3-alt1
- New version 2601.0.3.

* Fri Jan 30 2026 Leontiy Volodin <lvol@altlinux.org> 2601.0.2-alt1
- New version 2601.0.2.

* Thu Jan 15 2026 Leontiy Volodin <lvol@altlinux.org> 2601.0.1-alt1
- New version 2601.0.1.

* Thu Dec 04 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.16-alt1
- New version 2510.0.16.

* Wed Oct 29 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.14-alt1
- New version 2510.0.14.

* Wed Oct 22 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.12-alt1
- New version 2510.0.12.

* Tue Oct 07 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.11-alt1
- New version 2510.0.11.

* Tue Sep 30 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.9-alt1
- New version 2510.0.9.

* Fri Sep 19 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.8-alt1
- New version 2510.0.8.

* Fri Sep 12 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.6-alt1
- New version 2510.0.6.

* Fri Sep 05 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.5-alt1
- New version 2510.0.5.

* Fri Aug 22 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.3-alt1
- New version 2510.0.3.

* Thu Aug 21 2025 Leontiy Volodin <lvol@altlinux.org> 2510.0.2-alt1
- New version 2510.0.2.

* Thu Feb 20 2025 Leontiy Volodin <lvol@altlinux.org> 24.10.1-alt1
- New version 24.10.1.
- Added vcs tag.

* Mon Jan 22 2024 Leontiy Volodin <lvol@altlinux.org> 23.10.0-alt1
- New version v23.10.0.

* Tue Jul 04 2023 Leontiy Volodin <lvol@altlinux.org> 23.04-alt1
- New version 23.04.
- Updated license tag.

* Thu Jul 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.1.3-alt3
- Built with python2 (ALT #43337).

* Mon Nov 22 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.3-alt2
- Added requires (ALT #41412).
- Fixed syntax errors in mlx_fs_dump (ALT #41411).

* Tue Nov 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.3-alt1
- Initial build for ALT Sisyphus (based on upstream spec).
- Built for ticket 2021110801000478 (redmine_65351).
