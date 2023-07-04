%filter_from_requires /\/etc\/rc.d\/init.d\/openvswitch/d
%filter_from_requires /\/etc\/mellanox\/mlnx-bf.conf/d
%filter_from_requires /\/etc\/mellanox\/mlnx-ovs.conf/d
%filter_from_requires /systemd/d

Name: mlnx-tools
Version: 23.04
Release: alt1

Summary: Mellanox userland tools and scripts

License: (BSD or CPL-1.0 or GPL-2.0) and GPL-2.0+ and MIT
Group: System/Kernel and hardware
Url: https://github.com/Mellanox/mlnx-tools

Source: https://github.com/Mellanox/mlnx-tools/releases/download/v%version/%name-%version.tar.gz
Patch: mlnx-tools-5.2.0-alt-disable-conf-detection.patch
Patch1: mlnx-tools-5.2.0-alt-syntax.patch

BuildRequires: perl-devel python3-devel
Requires: python3-module-termcolor python3-module-anytree
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
%patch -p1
%patch1 -p1

sed -i 's|/etc/init.d/openvswitch-switch|/etc/init.d/openvswitch|' \
  tsbin/mlnx_bf_configure
# fix python shebangs
sed -i 's|%_bindir/env python|%__python3|' \
  python/ib2ib_setup \
  python/mlnx_tune
# sed -i 's|%_bindir/python|%__python3|' \
#   python/*
# sed -i 's|%_libexecdir/python2.7|%python3_libdir|' \
#   python/*
sed -i 's|%_bindir/env python3|%__python3|' \
  tsbin/mlnx-sf

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

touch mlnx-tools-files
mlnx_python_sitelib=%python3_sitelibdir
if [ "$(echo %prefix | sed -e 's@/@@g')" != "usr" ]; then
  mlnx_python_sitelib=$(echo %python3_sitelibdir | sed -e 's@/usr@%prefix@')
fi
export PKG_VERSION="%version"
%makeinstall_std PYTHON="%__python3" PYTHON_SETUP_EXTRA_ARGS="-O1 --prefix=%buildroot%prefix --install-lib=%buildroot${mlnx_python_sitelib}"

if [ "$(echo %prefix | sed -e 's@/@@g')" != "usr" ]; then
  conf_env=/etc/profile.d/mlnx-tools.sh
  install -d %buildroot/etc/profile.d
  add_env %buildroot$conf_env PYTHONPATH $mlnx_python_sitelib
  add_env %buildroot$conf_env PATH %_bindir
  add_env %buildroot$conf_env PATH %_sbindir
  echo $conf_env >> mlnx-tools-files
fi

find %buildroot${mlnx_python_sitelib} -type f -print | sed -e 's@%buildroot@@' >> mlnx-tools-files

%files
%doc doc/*
/sbin/sysctl_perf_tuning
/sbin/mlnx_bf_configure
/sbin/mlnx_bf_configure_ct
/sbin/mlnx-sf
%_sbindir/*
%_bindir/*
%_man8dir/ib2ib_setup.8*
%_man8dir/mlnxofedctl.8*
/lib/udev/mlnx_bf_udev

%files -n python3-module-mlnx -f mlnx-tools-files
%python3_sitelibdir/*

%changelog
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
