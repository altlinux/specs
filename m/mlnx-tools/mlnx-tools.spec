%filter_from_requires /\/etc\/mellanox\/mlnx-ovs.conf/d
%filter_from_requires /\/etc\/mellanox\/mlnx-sf.conf/d
%filter_from_requires /\/etc\/mellanox\/mlnx-bf.conf/d
%filter_from_requires /systemd/d
%filter_from_requires /\/bin\/systemctl/d
%filter_from_requires \/sbin\/sysctl/d
%filter_from_requires \/etc\/sysconfig/d

%define _udevrulesdir /lib/udev/rules.d
%define _udevdir /lib/udev

Name: mlnx-tools
Version: 24.10.1
Release: alt1

Summary: Mellanox userland tools and scripts

License: BSD-style or CPL-1.0 or GPL-2.0-only and GPL-2.0-or-later and MIT
Group: System/Kernel and hardware
Url: https://github.com/Mellanox/mlnx-tools
Vcs: https://github.com/Mellanox/mlnx-tools.git

Source: https://github.com/Mellanox/mlnx-tools/releases/download/v%version/%name-%version.tar.gz
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
sed -i 's|/usr/share/mlnx-tools/python|%python3_sitelibdir/%name|g' \
    Makefile \
    python/Python/dcbnetlink.py \
    python/mlnx_qos
sed -e 's|/usr/bin/python|%__python3|;' \
    -e 's|/usr/bin/env python3|%__python3|;' \
    -e 's|/usr/bin/env python|%__python3|;' \
    -i $(find ./python -type f -print) \
    -i tsbin/mlnx-sf
sed -i 's|openvswitch-switch|openvswitch|g' \
    tsbin/mlnx_bf_configure

%install
%makeinstall_std
chmod +x %buildroot%python3_sitelibdir/%name/dcbnetlink.py

%files
%doc doc/*
%config(noreplace) %_sysconfdir/modprobe.d/mlnx-bf.conf
/sbin/sysctl_perf_tuning
/sbin/mlnx_bf_configure
/sbin/mlnx_bf_configure_ct
/sbin/mlnx-sf
%_sbindir/*
%_bindir/*
%_man8dir/ib2ib_setup.8*
%_udevdir/mlnx_bf_udev
%_udevdir/auxdev-sf-netdev-rename
%_udevdir/mlnx_bf_assign_ct_cores.sh
%_udevrulesdir/82-net-setup-link.rules
%_udevrulesdir/83-mlnx-sf-name.rules
%_udevdir/sf-rep-netdev-rename
%_udevdir/vf-net-link-name.sh

%files -n python3-module-mlnx
%python3_sitelibdir/%name/

%changelog
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
