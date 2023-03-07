
Name: mom
Version: 0.6.4
Release: alt1
Summary: Dynamically manage system resources on virtualization hosts

Group: System/Configuration/Other
License: GPLv2
Url: https://www.ovirt.org
Source: %name-%version.tar
Source1: momd.init
# Patch2: %name-%version-altlinux.patch
Patch0001: 0001-Fix-import-modules-from-vdsm.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

# MOM makes use of libvirt by way of the python bindings to monitor and
# interact with virtual machines.
Requires: libvirt python3-module-libvirt libvirt-daemon-driver-qemu
Requires: procps

%description
MOM is a policy-driven tool that can be used to manage overcommitment on KVM
hosts. Using libvirt, MOM keeps track of active virtual machines on a host. At
a regular collection interval, data is gathered about the host and guests. Data
can come from multiple sources (eg. the /proc interface, libvirt API calls, a
client program connected to a guest, etc). Once collected, the data is
organized for use by the policy evaluation engine. When started, MOM accepts a
user-supplied overcommitment policy. This policy is regularly evaluated using
the latest collected data. In response to certain conditions, the policy may
trigger reconfiguration of the system's overcommitment mechanisms. Currently
MOM supports control of memory ballooning and KSM but the architecture is
designed to accommodate new mechanisms such as cgroups.

%prep
%setup
%patch0001 -p1

%build
echo "v%version-%release" > VERSION
%autoreconf
%configure \
	PYTHON="%__python3"
%make_build

%install
%makeinstall_std
install -Dp -m 755 %SOURCE1 %buildroot%_initdir/momd
install -Dp -m 644 contrib/momd.service %buildroot%_unitdir/momd.service
install -Dp -m 644 doc/mom-balloon+ksm.conf %buildroot%_sysconfdir/momd.conf

rm -rf %buildroot%_datadir/doc/mom

%post
%post_service momd

%preun
%preun_service momd

%files
%_sbindir/momd
%_initdir/momd
%_unitdir/momd.service
%python3_sitelibdir/*
%config(noreplace) %_sysconfdir/momd.conf
%doc README.md doc/*.rules doc/*.conf

%changelog
* Wed Mar 01 2023 Alexey Shabalin <shaba@altlinux.org> 0.6.4-alt1
- 0.6.4

* Sun Aug 08 2021 Alexey Shabalin <shaba@altlinux.org> 0.6.1-alt1
- 0.6.1

* Thu Sep 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Tue May 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Jan 27 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt2
- 0.3.2 stable

* Fri Dec 06 2013 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- Initial package
- upstream git snaphot 2691f259ce0ff22b747d0ade7897137e6d89942e
