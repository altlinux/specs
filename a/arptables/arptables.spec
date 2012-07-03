%define ver 0.0.3
%define over 4
Name: arptables
Version: %ver.%over
Release: alt1

Summary: A filtering tool for a bridging firewall
License: GPL
Group: System/Kernel and hardware

URL: http://ebtables.sourceforge.net
Packager: Boris Savelev <boris@altlinux.org>
Source: %name-v%ver-%over.tar.gz

%description
The ebtables program is a filtering tool for a bridging firewall.
The filtering is focussed on the Link Layer Ethernet frame fields.
Apart from filtering, it also gives the ability to alter the
Ethernet MAC addresses and implement a brouter.

%prep
%setup -n %name-v%ver-%over
sed -i "s|-o root -g root||g" Makefile

%build
%make_build

%install
mkdir -p %buildroot{%_initdir,%_sysconfdir/sysconfig}
touch %buildroot%_sysconfdir/%name
%makeinstall_std PREFIX=%_prefix BINDIR=/sbin MANDIR=%_mandir INITDIR=%_initdir

%files
%_initdir/%name
%config %_sysconfdir/%name
/sbin/%{name}*
%_man8dir/%name.*

%changelog
* Mon Mar 08 2010 Boris Savelev <boris@altlinux.org> 0.0.3.4-alt1
- new version
- add service, man, scripts

* Fri Oct 24 2008 Boris Savelev <boris@altlinux.org> 0.0.3.3-alt1
- initial build for Sisyphus.

