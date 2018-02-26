Summary: Create Ganeti IMAGE-based VMs
Name: ganeti-instance-image
Version: 0.4
Release: alt3
License: GPLv2
Group: System/Configuration/Other
URL: http://code.osuosl.org/projects/ganeti-image
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: ganeti-instance-image-%version.tar.gz
BuildArch: noarch

BuildRequires: dump multipath-tools sfdisk qemu losetup

%description
This is a guest OS definition for Ganeti (http://code.google.com/p/ganeti). It
will install a Linux-based image using either a tarball, filesystem dump, or a
qemu-img disk image file. This definition also allows for manual creation of an
instance by simply setting only the disks up and allowing you to boot via the
install cd manually.  The goal of this instance is to allow fast and flexible
installation of instances without the need for external tools such as
debootstrap.

%prep
%setup -q
%autoreconf

%build
PATH=$PATH:/sbin %configure --with-os-dir=%_datadir/ganeti/os --localstatedir=/var

%make

%install
%makeinstall_std
cp -a defaults %buildroot/%_sysconfdir/ganeti/instance-image/
mkdir -p %buildroot/%_cachedir/%name

%files
%doc COPYING NEWS README
%_datadir/ganeti/os/image
%dir %_sysconfdir/ganeti/instance-image
%dir %_sysconfdir/ganeti/instance-image/variants
%_sysconfdir/ganeti/instance-image/hooks
%_sysconfdir/ganeti/instance-image/networks
%_sysconfdir/ganeti/instance-image/overlays
%config(noreplace) %_sysconfdir/ganeti/instance-image/*
%config(noreplace) %_sysconfdir/ganeti/instance-image/variants/*.conf
%_cachedir/%name

%changelog
* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt3
- repair build

* Wed Dec 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2
- NOMOUNT option to allow Windows install (upstream merge)

* Wed Sep 01 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1
- Initial
