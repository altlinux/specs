
Name: corosync-qdevice
Summary: The Corosync Cluster Engine Qdevice
Version: 3.0.2
Release: alt1
Group: System/Base
License: BSD
Url: https://github.com/corosync/corosync-qdevice
Source: %name-%version.tar
Source2: corosync-qdevice-init
Source3: corosync-qnetd-init
Patch: %name-%version.patch

# Runtime bits
Requires: corosync >= 2.4.0
Requires: libcorosync >= 2.4.0
Requires: nss-utils

BuildRequires: systemd-devel
BuildRequires: libcorosync-devel
BuildRequires: libnss-devel


%define _localstatedir %_var

%description
This package contains the Corosync Cluster Engine Qdevice, script for creating
NSS certificates and an init script.

%package -n corosync-qnetd
Summary: The Corosync Cluster Engine Qdevice Network Daemon
Group: System/Base
Requires: nss-utils

%description -n corosync-qnetd
This package contains the Corosync Cluster Engine Qdevice Network Daemon,
script for creating NSS certificates and an init script.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-systemd \
	--enable-qdevices \
	--enable-qnetd \
	--enable-user-flags \
	--with-initddir=%_initdir \
	--with-systemddir=%_unitdir \
	--docdir=%_docdir

%make_build

%install
%makeinstall_std

## tree fixup
# drop docs and html docs for now
rm -rf %buildroot%_docdir/*
mkdir -p %buildroot%_sysconfdir/sysconfig
# /etc/sysconfig/corosync-qdevice
install -p -m 644 init/corosync-qdevice.sysconfig.example \
   %buildroot%_sysconfdir/sysconfig/corosync-qdevice
# /etc/sysconfig/corosync-qnetd
install -p -m 644 init/corosync-qnetd.sysconfig.example \
   %buildroot%_sysconfdir/sysconfig/corosync-qnetd

mkdir -p %buildroot%_initdir
install -m 755 %SOURCE2 %buildroot%_initdir/corosync-qdevice
install -m 755 %SOURCE3 %buildroot%_initdir/corosync-qnetd

sed -i -e 's/^#User=/User=/' \
   %buildroot%_unitdir/corosync-qnetd.service


%check
%make check

%pre -n corosync-qnetd
%_sbindir/groupadd -r -f coroqnetd 2> /dev/null ||:
%_sbindir/useradd -r -l -M -g coroqnetd -d /var/empty -s /dev/null -c "User for corosync-qnetd" coroqnetd 2> /dev/null ||:

%post
%post_service corosync-qdevice

%preun
%preun_service corosync-qdevice

%post -n corosync-qnetd
%post_service corosync-qnetd

%postun -n corosync-qnetd
%preun_service corosync-qnetd

%files
%dir %_sysconfdir/corosync/qdevice
%dir %config(noreplace) %_sysconfdir/corosync/qdevice/net
%_sbindir/corosync-qdevice*
%config(noreplace) %_sysconfdir/sysconfig/corosync-qdevice
%_unitdir/corosync-qdevice.service
%_initrddir/corosync-qdevice
%_man8dir/*qdevice*

%files -n corosync-qnetd
%dir %config(noreplace) %attr(770, root, coroqnetd) %_sysconfdir/corosync/qnetd
%_bindir/corosync-qnetd*
%config(noreplace) %_sysconfdir/sysconfig/corosync-qnetd
%_unitdir/corosync-qnetd.service
%_initrddir/corosync-qnetd
%_man8dir/*qnetd*

%changelog
* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 3.0.2-alt1
- new version 3.0.2

* Fri Jan 15 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.1-alt1
- new version 3.0.1

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- initial build as separated package
