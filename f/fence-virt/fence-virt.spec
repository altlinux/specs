%define _unpackaged_files_terminate_build 1

# like subst_with, but replacing '_' with '-'
%define subst_enable_dash() %{expand:%%(echo '%%{subst_enable %1}' | sed 's/_/-/g')}

%def_enable cpg_plugin
%def_disable libvirt_qmf_plugin

%global commit      c2ca768a8e57a73b5ec2899305439122285aa4a9
%global shortcommit c2ca768
#%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: fence-virt
Version: 0.4.0
Release: alt0.1.%shortcommit
Summary: A pluggable fencing framework for virtual machines
License: GPLv2+
Group: System/Base

Url: http://fence-virt.sourceforge.net
Source0: %name-%version.tar
Source11: fence_virtd.init

BuildRequires: gcc-c++
BuildRequires: libcorosync-devel libvirt-devel
BuildRequires: libxml2-devel nss-devel nspr-devel
BuildRequires: flex libuuid-devel

%description
Fencing agent for virtual machines.

%package -n fence-virtd
Summary: Daemon which handles requests from fence-virt
Group: System/Base

%description -n fence-virtd
This package provides the host server framework, fence_virtd,
for fence_virt.  The fence_virtd host daemon is resposible for
processing fencing requests from virtual machines and routing
the requests to the appropriate physical machine for action.

%package -n fence-virtd-multicast
Summary: Multicast listener for fence-virtd
Requires: fence-virtd
Group: System/Base

%description -n fence-virtd-multicast
Provides multicast listener capability for fence-virtd.

%package -n fence-virtd-serial
Summary: Serial VMChannel listener for fence-virtd
Requires: libvirt >= 0.6.2
Requires: fence-virtd
Group: System/Base

%description -n fence-virtd-serial
Provides serial VMChannel listener capability for fence-virtd.

%package -n fence-virtd-tcp
Summary: TCP listener for fence-virtd
Requires: fence-virtd
Group: System/Base

%description -n fence-virtd-tcp
Provides TCP listener capability for fence-virtd.

%package -n fence-virtd-vsock
Summary: VSOCK listener for fence-virtd
Requires: fence-virtd
Group: System/Base

%description -n fence-virtd-vsock
Provides VSOCK listener capability for fence-virtd.

%package -n fence-virtd-libvirt
Summary: Libvirt backend for fence-virtd
Requires: libvirt >= 0.6.0
Requires: fence-virtd
Group: System/Base

%description -n fence-virtd-libvirt
Provides fence_virtd with a connection to libvirt to fence
virtual machines.  Useful for running a cluster of virtual
machines on a desktop.

%package -n fence-virtd-cpg
Summary: CPG/libvirt backend for fence-virtd
Requires: fence-virtd
Group: System/Base

%description -n fence-virtd-cpg
Provides fence_virtd with a connection to libvirt to fence
virtual machines. Uses corosync CPG to keep track of VM
locations to allow for non-local VMs to be fenced when VMs
are located on corosync cluster nodes.

%prep
%setup

%build
#%autoreconf
./autogen.sh
%configure %{subst_enable_dash cpg_plugin} %{subst_enable_dash libvirt_qmf_plugin}
%make_build

%install
%makeinstall_std

# Systemd unit file
mkdir -p %buildroot{%_unitdir,%_initdir}
install -m 0644 fence_virtd.service %buildroot%_unitdir/
install -m 0755 %SOURCE11 %buildroot%_initdir/fence_virtd

%post
%post_service fence_virtd

%preun
%preun_service fence_virtd

%files
%doc COPYING TODO README
%_sbindir/fence_virt
%_sbindir/fence_xvm
%_man8dir/fence_virt.*
%_man8dir/fence_xvm.*

%files -n fence-virtd
%_sbindir/fence_virtd
%_unitdir/fence_virtd.service
%_initdir/fence_virtd
%config(noreplace) %_sysconfdir/fence_virt.conf
%dir %_libdir/%name
%_man5dir/fence_virt.conf.*
%_man8dir/fence_virtd.*

%files -n fence-virtd-multicast
%_libdir/%name/multicast.so

%files -n fence-virtd-serial
%_libdir/%name/serial.so

%files -n fence-virtd-tcp
%_libdir/%name/tcp.so

%files -n fence-virtd-vsock
%_libdir/%name/vsock.so

%files -n fence-virtd-libvirt
%_libdir/%name/libvirt.so

%files -n fence-virtd-cpg
%_libdir/%name/cpg.so

%changelog
* Tue May 07 2019 Andrew A. Vasilyev <andy@altlinux.org> 0.4.0-alt0.1.c2ca768
- master snapshot c2ca768a8e57a73b5ec2899305439122285aa4a9

