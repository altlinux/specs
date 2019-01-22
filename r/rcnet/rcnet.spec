%define with_docs 0

Name: rcnet
Version: 1.0
Release: alt1
Group: System/Base
Summary: minimalistic and extremely flexible network setup environment
License: WTFPL
Source0: %name-%version.tar.xz
# devlink and other functions
Requires: iproute2 >= 4.12.0
# network stack is not a daemon
Conflicts: systemd
# there should be only one network-config-subsystem
Conflicts: etcnet NetworkManager
# these tools are using obsolete kernel functions
Conflicts: net-tools bridge-utils vlan-utils ifrename ifplugd ipset
Provides: network-config-subsystem
BuildArch: noarch
# most build environments would safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The %name is a %summary
primarily designed for servers and embedded systems, including (but
not limited to) network equipment.

%package netdevconf
Group: System/Base
Summary: Network device pre-configuration script for %name
BuildArch: noarch
%description netdevconf
%summary

%package -n sysconfig-network
Group: System/Base
Summary: One-file package to satisfy archaic dependencies
BuildArch: noarch
%description -n sysconfig-network
%summary

%if %with_docs
%package doc
Group: Documentation
Summary: Optional documentation for %name
BuildArch: noarch
%description doc
%summary
%endif

%prep
%setup

%install
rm -rf %buildroot
mkdir -pm755 \
  %buildroot%_initdir \
  %buildroot%_sysconfdir/sysconfig \
  %buildroot%_sbindir
install -m755 %name.init.network \
  %buildroot%_initdir/network
install -m755 %name.init.netdevconf \
  %buildroot%_initdir/netdevconf
install -m755 %name.rc.network \
  %buildroot%_sysconfdir/rc.d/rc.network
install -m755 %name.rc.firewall \
  %buildroot%_sysconfdir/rc.d/rc.firewall
install -m755 %name.rc.netdevconf \
  %buildroot%_sysconfdir/rc.d/rc.netdevconf
install -m644 %name.sysconfig \
  %buildroot%_sysconfdir/sysconfig/network
install -m755 sbin/* \
  %buildroot%_sbindir/


%post
chkconfig --add network

%post netdevconf
chkconfig --add netdevconf


%clean
rm -rf %buildroot


%files
%_initdir/network
%config(noreplace) %_sysconfdir/rc.d/rc.network
%config(noreplace) %_sysconfdir/rc.d/rc.firewall
%_sbindir/*

%files netdevconf
%_initdir/netdevconf
%config(noreplace) %_sysconfdir/rc.d/rc.netdevconf

%files -n sysconfig-network
%config(noreplace) %_sysconfdir/sysconfig/network

%if %with_docs
%files doc
%doc *.txt
%endif


%changelog
* Tue Jan 22 2019 Gremlin from Kremlin <gremlin@altlinux.org> 1.0-alt1
- first release for Sisyphus
