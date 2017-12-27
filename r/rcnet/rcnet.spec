%define with_docs 0

Name: rcnet
Version: 0.5
Release: alt1
Group: System/Base
Summary: minimalistic and extremely flexible network setup environment
License: WTFPL
Source0: %name.init
Source1: %name.rc
Source2: %name.sysconfig
# devlink and other functions
Requires: iproute2 >= 4.12.0
# network stack is not a daemon
Conflicts: systemd etcnet NetworkManager
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

%if %with_docs
%package doc
Group: System/Base
Summary: Optional documentation for %name
%description doc
%summary
%endif

%install
rm -rf %buildroot
mkdir -pm755 %buildroot%_initdir %buildroot%_sysconfdir/sysconfig
install -m755 %_sourcedir/%name.init \
  %buildroot%_initdir/network
install -m755 %_sourcedir/%name.rc \
  %buildroot%_sysconfdir/rc.d/rc.network
install -m644 %_sourcedir/%name.sysconfig \
  %buildroot%_sysconfdir/sysconfig/network

%post
chkconfig --add network

%clean
rm -rf %buildroot

%files
%_initdir/network
%config(noreplace) %_sysconfdir/rc.d/rc.network
%config(noreplace) %_sysconfdir/sysconfig/network

%if %with_docs
%files doc
%doc *.txt
%endif

%changelog
* Wed Dec 27 2017 Gremlin from Kremlin <gremlin@altlinux.org> 0.5-alt1
- initial build
