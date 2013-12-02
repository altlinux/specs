%def_with udev
%def_with heartbeat

%define _localstatedir %_var

Name: drbd
Summary: Distributed Redundant Block Device
Version: 8.3.16
Release: alt1
Source: %name-%version.tar
Patch: %name-%version-%release.patch
License: GPLv2+
Group: System/Kernel and hardware
Url: http://www.%name.org/
Obsoletes: %{name}83 %{name}83-udev
Provides: %{name}83 = %version-%release
Provides: %{name}83-udev = %version-%release

BuildPreReq: rpm-build-kernel
BuildRequires(pre): rpm-build-linux-ha
BuildRequires: docbook-dtds docbook-style-xsl flex xsltproc

%description
Drbd is a distributed replicated block device. It mirrors a block device over the
network to another machine. Think of it as networked raid 1. It is a building
block for setting up high availability (HA) clusters.


%package tools
Summary: Distributed Redundant Block Device utilities
Group: System/Kernel and hardware
Provides: %{name}83-tools = %version-%release
Obsoletes: %{name}83-tools

%description tools
Drbd is a distributed replicated block device. It mirrors a block device over the
network to another machine. Think of it as networked raid 1. It is a building
block for setting up high availability (HA) clusters.

This package contains the programs that will control the drbd kernel module
provided in kernel-source-drbd. You will need a clustering service (such as
heartbeat) to fully implement it.


%package -n kernel-source-%name
Summary: Kernel source for DRBD
Group: Development/Kernel
BuildArch: noarch
Provides: kernel-src-%name = %version-%release
Obsoletes: kernel-source-%{name}83

%description -n kernel-source-%name
This is the source of the kernel-dependant driver for DRBD.


%if_with heartbeat
%package heartbeat
Summary: Heartbeat resource agent for DRBD
Group: System/Kernel and hardware
BuildArch: noarch
Requires: %name-tools = %version-%release
Requires: %_ha_resource_dir
Requires: heartbeat
Provides: %{name}83-heartbeat = %version-%release
Obsoletes: %{name}83-heartbeat

%description heartbeat
This package contains the DRBD resource agents for the Heartbeat cluster resource
manager (in v1 compatibility mode).
%endif


%prep
%setup -q
%patch -p1
install -d -m 0755 %name-%version/scripts
ln -sf ../%name %name-%version/
ln -sf ../../scripts/adjust_drbd_config_h.sh %name-%version/scripts/


%build
./autogen.sh
%configure \
	--with-utils \
	%{subst_with udev} \
	%{subst_with heartbeat} \
	--without-xen \
	--without-km \
	--without-bashcompletion \

%make_build tools doc
gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std
install -d -m 0755 %buildroot%_sysconfdir/sysconfig %kernel_srcdir

cat > %buildroot%_sysconfdir/%name.conf <<__EOF__
#
# please have a a look at the example configuration file in
# %_docdir/%name-utils-%version/
#
include "%name.d/global_common.conf";
include "%name.d/*.res";
__EOF__


cat > %buildroot%_sysconfdir/sysconfig/%name <<__EOF__
DEFAULTFILE="%_sysconfdir/sysconfig/%name"
DRBDADM="/sbin/%{name}adm"
PROC_DRBD="/proc/%name"
MODPROBE="/sbin/modprobe"
RMMOD="/sbin/rmmod"
UDEV_TIMEOUT=10
ADD_MOD_PARAM=""
__EOF__

tar -cJhf %kernel_srcdir/%name-%version.tar.xz %name-%version


%files tools
%doc scripts/drbd.conf.example README ChangeLog.*
/sbin/*
%_sbindir/*
%_initddir/*
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/%name.d
%{?_with_udev:%config %_sysconfdir/udev/rules.d/*}
/usr/lib/%name
%exclude /usr/lib/%name/crm-*
%_man5dir/*
%_man8dir/*
%dir %_localstatedir/lib/%name


%files -n kernel-source-%name
%_usrsrc/kernel


%if_with heartbeat
%files heartbeat
%_ha_resource_dir/*
%_libexecdir/ocf/resource.d/*
/usr/lib/%name/crm-*
%endif


%changelog
* Mon Dec 02 2013 Led <led@altlinux.ru> 8.3.16-alt1
- 8.3.16

* Mon Dec 24 2012 Led <led@altlinux.ru> 8.3.15-alt1
- 8.3.15

* Thu Oct 25 2012 Led <led@altlinux.ru> 8.3.14-alt1
- 8.3.14

* Sun May 13 2012 Led <led@massivesolutions.co.uk> 8.3.13-cx1
- initial build
