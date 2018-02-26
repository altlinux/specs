Summary: Cluster-based virtualization management software
Name: ganeti
Version: 2.5.1
Release: alt1
License: GPLv2
Group: System/Configuration/Other
Url: http://code.google.com/p/ganeti/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://ganeti.googlecode.com/files/ganeti-%version.tar.gz
BuildArch: noarch
BuildRequires: python-module-OpenSSL python-module-simplejson python-module-pyinotify python-module-pyparsing pylint socat python-module-sphinx docbook-utils graphviz openssh-server python-module-pycurl pandoc iproute2 python-tools-pep8
BuildRequires: /proc
%py_requires roman
%py_requires readline
%py_requires hashlib
%py_requires md5
%py_requires sha
Requires: python-module-pyinotify >= 0.9.0-alt1
Requires: socat
Requires: service >= 0.5.20-alt1

%add_findreq_skiplist /usr/lib/%name/tools/xm-console-wrapper

%description
Ganeti is a virtual server cluster management software tool built on top
of the Xen virtual machine monitor and other Open Source software. After
setting it up it will provide you with an automated environment to
manage highly available virtual machine instances.

It has been designed to facilitate cluster management of virtual servers
and to provide fast and simple recovery after physical failures using
commodity hardware.

It will take care of operations such as redundant disk creation and
management, operating system installation  (in cooperation with OS-specific
install scripts), startup, shutdown, failover of instances between physical
systems.

%package initrd-generator
Requires: make-initrd
Group: System/Kernel and hardware
Summary: Package for automatic initrd creation for ganeti instances

%description initrd-generator
Package for automatic initrd creation for ganeti instances

%prep
%setup -q
%autoreconf

%build
%configure \
  --localstatedir=/var \
  --libdir=/usr/lib \
  --with-ssh-initscript=%_initdir/sshd \
  --with-export-dir=%_localstatedir/%name/export \
  --with-os-search-path=%_datadir/%name/os,%_libdir/%name/os,/usr/local/lib/%name/os,/srv/%name/os,%_localstatedir/%name/os \
  --with-iallocator-search-path=%_libdir/%name/iallocators \
  --with-ssh-config-dir=%_sysconfdir/openssh \
  --with-file-storage-dir=%_localstatedir/%name/file-storage \
  --with-user-prefix=gnt \
  --with-group-prefix=gnt

%make

%check
%make -k check

%install
%makeinstall_std

mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sysconfdir/sysconfig

install -m 755 -d %buildroot%_sysconfdir/%name

mkdir -p %buildroot%_docdir/%name
mkdir -p %buildroot/%_datadir/%name/os
mkdir -p %buildroot/%_localstatedir/%name/export
mkdir -p %buildroot/%_localstatedir/%name/file-storage
cp -ar doc/html %buildroot%_docdir/%name
install -m 755 doc/examples/ganeti.initd %buildroot%_initdir/%name

mkdir -p %buildroot/%_datadir/make-initrd/data/modules
install -m 755 alt/130-copy-initrd-modules.sh %buildroot/%_datadir/make-initrd/data/modules
install -m 644 alt/initrd.mk %buildroot%_sysconfdir/%name/
install -m 755 alt/ganeti-initrd-generator %buildroot/%_sbindir/

touch %buildroot%_sysconfdir/%name/kvm-vif-bridge
chmod 755 %buildroot%_sysconfdir/%name/kvm-vif-bridge

%triggerpostun -- ganeti < 2.4.0
echo >&2 "\
Warning: do not forget to upgrade your cluster configuration using /usr/lib/ganeti/tools/cfgupgrade"

%pre
%_sbindir/groupadd -r -f gntrapi
%_sbindir/groupadd -r -f gntadmin
%_sbindir/groupadd -r -f gntconfd
%_sbindir/groupadd -r -f gntmasterd
%_sbindir/groupadd -r -f gntdaemons
%_sbindir/useradd -r -n -g gntmasterd -G gntrapi,gntadmin,gntconfd,gntmasterd,gntdaemons -d /var/empty -s /bin/false -c "Ganeti masterd user" gntmasterd >/dev/null 2>&1 ||:
%_sbindir/useradd -r -n -g gntrapi -G gntrapi,gntadmin,gntdaemons -d /var/empty -s /bin/false -c "Ganeti rapi user" gntrapi >/dev/null 2>&1 ||:
%_sbindir/useradd -r -n -g gntconfd -G gntconfd,gntdaemons -d /var/empty -s /bin/false -c "Ganeti confd user" gntconfd >/dev/null 2>&1 ||:

%post
/usr/lib/ganeti/ensure-dirs -f
%post_service ganeti

%preun
%preun_service ganeti

%files
%config(noreplace) %_sysconfdir/%name/kvm-vif-bridge
%attr(755,root,root) %config %_initdir/%name
%_docdir/%name
%_sbindir/*
%exclude %_sbindir/ganeti-initrd-generator
/usr/lib/%name
%python_sitelibdir/%name
%_mandir/man*/*
%dir /%_datadir/%name/os
%dir /%_localstatedir/%name/export
%dir /%_localstatedir/%name/file-storage
%dir %_sysconfdir/%name
%attr(755,gntmasterd,gntmasterd) %dir /var/lib/%name
%attr(770,gntmasterd,gntdaemons) %dir /var/log/%name
%attr(770,gntmasterd,gntdaemons) %dir /var/run/%name

%files initrd-generator
%_datadir/make-initrd/data/modules/130-copy-initrd-modules.sh
%_sysconfdir/%name/initrd.mk
%_sbindir/ganeti-initrd-generator

%changelog
* Tue May 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Fri Apr 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Thu Dec 29 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.5-alt2
- fix docs build

* Thu Nov 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt1.1
- Rebuild with Python-2.7

* Mon Sep 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Sun Aug 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Fri May 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Tue Apr 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Dec 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Dec 01 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Fri Nov 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Tue Oct 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Oct 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Mon Oct 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Sep 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0-alt0.rc2
- 2.2.0-rc2

* Wed Aug 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.0-alt0.rc1
- 2.2.0-rc1

* Tue Aug 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Wed Aug 04 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.6-alt1
- 2.1.6
- fix initrd module copying

* Thu Jun 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Fri May 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.2.1-alt1
- 2.1.2.1

* Fri May 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Sat Mar 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Tue Mar 02 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1
- 2.1.0 final release

* Mon Feb 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt0.rc5
- Initial
