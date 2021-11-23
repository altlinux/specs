%filter_from_requires /\/etc\/rc.d\/init.d\/openvswitch/d

Name: mlnx-tools
Version: 5.1.3
Release: alt2

Summary: Mellanox userland tools and scripts

License: GPL-2.0
Group: System/Kernel and hardware
Url: https://github.com/Mellanox/mlnx-tools

Vendor: Mellanox Technologies

Source: https://github.com/Mellanox/mlnx-tools/releases/download/v%version/%name-%version.tar.gz
Patch: mlnx-tools-5.1.3-alt-disable-conf-detection.patch
Patch1: mlnx-tools-5.1.3-alt-syntax.patch

BuildRequires: perl-devel python3-devel
BuildRequires: openvswitch /usr/bin/systemctl startup
Requires: openvswitch python3-module-termcolor python3-module-anytree mstflint

%description
Mellanox userland tools and scripts

%package -n python3-module-mlnx
Summary: Python3 bindings for %name
Group: Development/Python3

%description -n python3-module-mlnx
The package provides python3 bindings for %name.

%prep
%setup -n %name-%version
%patch -p1
%patch1 -p1

sed -i 's|/etc/init.d/openvswitch-switch|/etc/init.d/openvswitch|' \
    ofed_scripts/mlnx-post-hlk \
    ofed_scripts/mlnx-pre-hlk
# fix python shebangs
sed -i 's|/usr/bin/env python|%__python3|' $(find ./ -name '*.py')
sed -i 's|/usr/bin/python|%__python3|' $(find ./ -name '*.py')
sed -i 's|/usr/lib/python2.7|%python3_libdir|' $(find ./ -name '*.py')

%install
add_env()
{
	efile=$1
	evar=$2
	epath=$3

cat >> $efile << EOF
if ! echo \$${evar} | grep -q $epath ; then
	export $evar=$epath:\$$evar
fi

EOF
}

cd ofed_scripts/utils
mlnx_python_sitelib=%python3_sitelibdir
if [ "$(echo %prefix | sed -e 's@/@@g')" != "usr" ]; then
	mlnx_python_sitelib=$(echo %python3_sitelibdir | sed -e 's@/usr@%prefix@')
fi
%__python3 setup.py install -O1 --prefix=%buildroot%prefix --install-lib=%buildroot${mlnx_python_sitelib}
cd -

install -d %buildroot/sbin
install -d %buildroot%_sbindir
install -d %buildroot%_bindir
install -d %buildroot/lib/udev
install -d %buildroot%_udevrulesdir
install -d %buildroot%_sysconfdir/modprobe.d
install -d %buildroot%_sysconfdir/systemd/system/
install -m 0755 ofed_scripts/sysctl_perf_tuning     %buildroot/sbin
install -m 0755 ofed_scripts/cma_roce_mode          %buildroot%_sbindir
install -m 0755 ofed_scripts/cma_roce_tos           %buildroot%_sbindir
install -m 0755 ofed_scripts/*affinity*             %buildroot%_sbindir
install -m 0755 ofed_scripts/setup_mr_cache.sh      %buildroot%_sbindir
install -m 0755 ofed_scripts/odp_stat.sh            %buildroot%_sbindir
install -m 0755 ofed_scripts/show_counters          %buildroot%_sbindir
install -m 0755 ofed_scripts/show_gids              %buildroot%_sbindir
install -m 0755 ofed_scripts/mlnx*hlk               %buildroot%_sbindir
install -m 0755 ofed_scripts/ibdev2netdev           %buildroot%_bindir
install -m 0755 ofed_scripts/roce_config.sh         %buildroot%_bindir/roce_config
install -m 0755 kernel-boot/vf-net-link-name.sh     %buildroot/lib/udev/
install -m 0644 kernel-boot/82-net-setup-link.rules %buildroot%_udevrulesdir/
install -m 0644 kernel-boot/91-tmfifo_net.rules     %buildroot%_udevrulesdir/
install -m 0644 kernel-boot/92-oob_net.rules        %buildroot%_udevrulesdir/
install -m 0644 kernel-boot/mlnx-bf.conf            %buildroot%_sysconfdir/modprobe.d/
install -m 0755 kernel-boot/mlnx_bf_configure       %buildroot/sbin
install -m 0755 kernel-boot/mlnx-sf                 %buildroot/sbin
install -m 0644 kernel-boot/mlnx-bf-ctl.service     %buildroot%_sysconfdir/systemd/system/

if [ "$(echo %prefix | sed -e 's@/@@g')" != "usr" ]; then
	conf_env=/etc/profile.d/mlnx-tools.sh
	install -d %buildroot/etc/profile.d
	add_env %buildroot$conf_env PYTHONPATH $mlnx_python_sitelib
	add_env %buildroot$conf_env PATH %_bindir
	add_env %buildroot$conf_env PATH %_sbindir
fi

chmod +x %buildroot%python3_sitelibdir/dcbnetlink.py

# %%preun
# %%_bindir/systemctl disable mlnx-bf-ctl.service >/dev/null 2>&1 || :
#
# %%post
# %%_bindir/systemctl daemon-reload >/dev/null 2>&1 || :
# %%_bindir/systemctl enable mlnx-bf-ctl.service >/dev/null 2>&1 || :

%files
/sbin/sysctl_perf_tuning
/sbin/mlnx_bf_configure
/sbin/mlnx-sf
%_sbindir/*
%_bindir/*
/lib/udev/vf-net-link-name.sh
%_udevrulesdir/82-net-setup-link.rules
%_udevrulesdir/91-tmfifo_net.rules
%_udevrulesdir/92-oob_net.rules
%_sysconfdir/systemd/system/mlnx-bf-ctl.service
%_sysconfdir/modprobe.d/mlnx-bf.conf

%files -n python3-module-mlnx
%python3_sitelibdir/*

%changelog
* Mon Nov 22 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.3-alt2
- Added requires (ALT #41412).
- Fixed syntax errors in mlx_fs_dump (ALT #41411).

* Tue Nov 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.1.3-alt1
- Initial build for ALT Sisyphus (based on upstream spec).
- Built for ticket 2021110801000478 (redmine_65351).
