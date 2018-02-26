Summary: Create Ganeti ALT-based VMs
Name: ganeti-instance-altbootstrap
Version: 0.9
Release: alt4
License: GPLv2
Group: System/Configuration/Other
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: ganeti-instance-altbootstrap-%version.tar.gz
BuildArch: noarch
Requires: multipath-tools /usr/bin/mkve-cache

%description
Create Ganeti ALT-based VMs

%prep
%setup -q
%autoreconf

%build
%configure --with-os-dir=%_datadir/ganeti/os --localstatedir=/var

%make

%install
%makeinstall_std
cp -a defaults %buildroot/%_sysconfdir/ganeti/instance-altbootstrap/
mkdir -p %buildroot/%_cachedir/%name

%pre
%_sbindir/groupadd -r -f gntinstancer
%_sbindir/useradd -r -n -m -g gntinstancer -c "Ganeti user for instance creation" gntinstancer >/dev/null 2>&1 ||:
%_sbindir/hasher-useradd gntinstancer >/dev/null 2>&1 ||:

%files
%doc COPYING NEWS README
%_datadir/ganeti/os/altbootstrap
%dir %_sysconfdir/ganeti/instance-altbootstrap
%dir %_sysconfdir/ganeti/instance-altbootstrap/variants
%config(noreplace) %_sysconfdir/ganeti/instance-altbootstrap/defaults
%config(noreplace) %_sysconfdir/ganeti/instance-altbootstrap/variants/*.conf
%_cachedir/%name

%changelog
* Thu Oct 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt4
- update to pv_ops xen (hvc0 instead of xvc0 console)

* Thu Jun 10 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt3
- pack configs as configs

* Wed Jun 02 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt2
- change buildreq for mkve-cache

* Tue May 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9-alt1
- numerous bugs fixed

* Tue May 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1
- add xen-pvm and kvm osvariants instead of default

* Fri Feb 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1
- initial
