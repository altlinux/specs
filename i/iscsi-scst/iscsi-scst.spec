Name: iscsi-scst
Version: 3.1.0
Release: alt1
Summary: iSCSI SCST Target
License: GPLv2
Group: System/Kernel and hardware
URL: http://scst.sf.net

Requires: scst-utils

Source: %name-%version.tar.bz2

BuildRequires: rpm-build-kernel scst-devel kernel-headers-modules-std-def

%description
ISCSI-SCST is a deeply reworked fork of iSCSI Enterprise Target (IET)

%package -n kernel-source-%name
Summary: ISCSI-SCST modules sources for Linux kernel
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release

%description -n kernel-source-%name
This package contains ISCSI-SCST modules sources for Linux kernel.

%prep
%setup -q

%build
%make KDIR=%_usrsrc/linux-*-std-def SCST_INC_DIR=%_includedir/scst include/iscsi_scst_itf_ver.h progs

%install
install -pD -m0755 usr/%{name}d %buildroot%_sbindir/%{name}d
install -m0755 usr/%{name}-adm %buildroot%_sbindir/
install -pD -m0644 doc/manpages/%{name}-adm.8 %buildroot%_man8dir/%{name}-adm.8
install -m0644 doc/manpages/%{name}d.8 %buildroot%_man8dir/
install -pD -m0644 doc/manpages/%{name}d.conf.5 %buildroot%_man5dir/%{name}d.conf.5

tar -cJf %name-%version.tar.xz Makefile kernel include README README.iser*
install -pD -m0644 %name-%version.tar.xz %kernel_srcdir/%name-%version.tar.xz

mkdir -p %buildroot%_unitdir
cat << __EOF__ > %buildroot%_unitdir/%name.service
[Unit]
Description=iSCSI SCST Target Daemon
Documentation=man:iscsi-scstd(8)
After=network.target
Before=scst.service
Conflicts=shutdown.target

[Service]
EnvironmentFile=-/etc/sysconfig/scst
PIDFile=/var/run/iscsi-scstd.pid
ExecStartPre=/sbin/modprobe iscsi-scst
ExecStart=/usr/sbin/iscsi-scstd \$ISCSID_OPTIONS

[Install]
WantedBy=multi-user.target
__EOF__

%preun
if [ $1 -eq 0 ] ; then
	/sbin/systemctl disable %name.service > /dev/null 2>&1 || :
fi

%files
%doc README README.iser*
%_unitdir/%name.service
%_sbindir/*
%_man5dir/*.5*
%_man8dir/*.8*

%files -n kernel-source-%name
%_usrsrc/kernel

%changelog
* Sun Oct 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- initial release

