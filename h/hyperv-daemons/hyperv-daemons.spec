%define kernel_base_version 4.4
%define kernel_source kernel-source-%kernel_base_version

Name: hyperv-daemons
Version: %kernel_base_version
Release: alt1
Summary:  HyperV daemons suite
License: GPLv2
Group: Emulators
URL: http://www.kernel.org


# git://git.altlinux.org/gears/h/%name.git
# Patch: %name-%version-%release.patch
#Patch2: %name-altlinux.patch

Source5: hv_get_dhcp_info.sh
Source6: hv_get_dns_info.sh
Source7: hv_set_ifconfig.sh

Source11: hypervkvpd.init
Source12: hypervvssd.init
Source13: hypervfcopyd.init

Source21: hypervkvpd.service
Source22: hypervvssd.service
Source23: hypervfcopyd.service

Source31: hypervkvpd.rules
Source32: hypervvssd.rules
Source33: hypervfcopyd.rules

ExclusiveArch:  %ix86 x86_64

Requires: hypervkvpd = %version-%release
Requires: hypervvssd = %version-%release
Requires: hypervfcopyd = %version-%release

BuildRequires: rpm-build-kernel
BuildRequires: %kernel_source = 1.0.0

%description
Suite of daemons that are needed when Linux guest
is running on Windows Host with HyperV.

%package -n hypervkvpd
Summary: HyperV key value pair (KVP) daemon
Group: Emulators
Provides: hv_kvp_daemon

%description -n hypervkvpd
Hypervkvpd is an implementation of HyperV key value pair (KVP)
functionality for Linux. The daemon first registers with the
kernel driver. After this is done it collects information
requested by Windows Host about the Linux Guest. It also supports
IP injection functionality on the Guest.


%package -n hypervvssd
Summary: HyperV VSS daemon
Group: Emulators
Provides: hv_vss_daemon

%description -n hypervvssd
Hypervvssd is an implementation of HyperV VSS functionality
for Linux. The daemon is used for host initiated guest snapshot
on HyperV hypervisor. The daemon first registers with the
kernel driver. After this is done it waits for instructions
from Windows Host if to "freeze" or "thaw" the filesystem
on the Linux Guest.

%package -n hypervfcopyd
Summary: HyperV host to guest copy functionality daemon
Group: Emulators
Provides: hv_fcopy_daemon

%description -n hypervfcopyd
Hypervfcopyd is an mplementation of host to guest copy 
functionality for Linux.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar
cd %kernel_source
# %patch -p1
# %patch2 -p1

%build
%add_optflags -I../../include/uapi -I../../include
export CFLAGS="%optflags"
make -C %kernel_source/tools hv

%install
#make -C %kernel_source/tools hv_install
pushd %kernel_source/tools/hv

mkdir -p %buildroot%_sbindir
install -p -m 0755 hv_kvp_daemon %buildroot%_sbindir/hypervkvpd
install -p -m 0755 hv_vss_daemon %buildroot%_sbindir/hypervvssd
install -p -m 0755 hv_fcopy_daemon %buildroot%_sbindir/hypervfcopyd

popd

# Shell scripts for the KVP daemon
install -p -m 0755 %SOURCE5 %buildroot%_sbindir/hv_get_dhcp_info
install -p -m 0755 %SOURCE6 %buildroot%_sbindir/hv_get_dns_info
install -p -m 0755 %SOURCE7 %buildroot%_sbindir/hv_set_ifconfig

# SysV init scripts
mkdir -p %buildroot%_initdir
install -p -m 0755 %SOURCE11 %buildroot%_initdir/hypervkvpd
install -p -m 0755 %SOURCE12 %buildroot%_initdir/hypervvssd
install -p -m 0755 %SOURCE13 %buildroot%_initdir/hypervfcopyd

# Systemd unit file
mkdir -p %buildroot%_unitdir
install -p -m 0644 %SOURCE21 %buildroot%_unitdir/hypervkvpd.service
install -p -m 0644 %SOURCE22 %buildroot%_unitdir/hypervvssd.service
install -p -m 0644 %SOURCE23 %buildroot%_unitdir/hypervfcopyd.service

# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m 0644 %SOURCE31 %buildroot%_udevrulesdir/hypervkvpd.rules
install -p -m 0644 %SOURCE32 %buildroot%_udevrulesdir/hypervvssd.rules
install -p -m 0644 %SOURCE33 %buildroot%_udevrulesdir/hypervfcopyd.rules

# Directory for pool files
mkdir -p %buildroot%_sharedstatedir/hyperv

%post -n hypervkvpd
# auto enable service for Hyper-V guest
if [ $1 -eq 1 ]; then
    board_vendor=
    product_name=
    [ -r /sys/class/dmi/id/board_vendor ] && board_vendor="`cat /sys/class/dmi/id/board_vendor`"
    [ -r /sys/class/dmi/id/product_name ] && board_vendor="`cat /sys/class/dmi/id/product_name`"

    if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"; then
	echo "Enabling hypervkvpd on '${product_name}' from '${board_vendor}'"
	chkconfig hypervkvpd on
    fi
fi
%post_service hypervkvpd

%preun -n hypervkvpd
%preun_service hypervkvpd

%post -n hypervvssd
if [ $1 -eq 1 ]; then
    board_vendor=
    product_name=
    [ -r /sys/class/dmi/id/board_vendor ] && board_vendor="`cat /sys/class/dmi/id/board_vendor`"
    [ -r /sys/class/dmi/id/product_name ] && board_vendor="`cat /sys/class/dmi/id/product_name`"

    if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"; then
	echo "Enabling hypervvssd on '${product_name}' from '${board_vendor}'"
	chkconfig hypervvssd on
    fi
fi
%post_service hypervvssd

%preun -n hypervvssd
%preun_service hypervvssd

%post -n hypervfcopyd
%post_service hypervfcopyd

%preun -n hypervfcopyd
%preun_service hypervfcopyd

%files
# the base package does not contain any files.

%files -n hypervkvpd
%_sbindir/hypervkvpd
%_sbindir/hv_*
%_initdir/hypervkvpd
%_unitdir/hypervkvpd.service
%_udevrulesdir/hypervkvpd.rules
%dir %_sharedstatedir/hyperv

%files -n hypervvssd
%_sbindir/hypervvssd
%_initdir/hypervvssd
%_unitdir/hypervvssd.service
%_udevrulesdir/hypervvssd.rules

%files -n hypervfcopyd
%_sbindir/hypervfcopyd
%_initdir/hypervfcopyd
%_unitdir/hypervfcopyd.service
%_udevrulesdir/hypervfcopyd.rules

%changelog
* Tue Jan 26 2016 Alexey Shabalin <shaba@altlinux.ru> 4.4-alt1
- build from kernel-source-4.4

* Wed Sep 16 2015 Alexey Shabalin <shaba@altlinux.ru> 4.2-alt1
- build from kernel-source-4.2

* Tue Apr 21 2015 Alexey Shabalin <shaba@altlinux.ru> 3.19-alt1
- build from kernel-source-3.19.5

* Thu Oct 09 2014 Alexey Shabalin <shaba@altlinux.ru> 3.17-alt1
- build from kernel-source-3.17

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14-alt5
- update from 3.14.5
- fixed typo in init scripts

* Thu Apr 17 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14-alt2
- sem@: hv_get_dns_info: Use resolvconf for retrieving DNS servers
- patch from fedora: Fix for long file names from readdir

* Wed Apr 16 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14-alt1
- up version to %%kernel_base_version
- sem@: hv_set_ifconfig: Improve script

* Tue Apr 08 2014 Alexey Shabalin <shaba@altlinux.ru> 0-alt1
- Initial build
