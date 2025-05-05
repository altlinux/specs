Name: livecd-attract
Version: 0.1
Release: alt2

Summary: start attract
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Artyom Bystrov <arbars@altlinux.org>
BuildArch: noarch

Requires: livecd-runapp

%define confdir %_sysconfdir/sysconfig
%define conffile %confdir/livecd-runapp

%description
%summary

%prep

%build

%install
mkdir -p %buildroot%confdir
cat > %buildroot%conffile << _EOF_
BINARY=attract
_EOF_

%files
%conffile

%changelog
* Mon May 05 2025 Anton Midyukov <antohami@altlinux.org> 0.1-alt2
- NMU: Remove runtime dependency on SysVinit-usermode

* Mon Oct 24 2022 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- forked from livecd-0ad

* Tue Mar 17 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- rewrote using livecd-runapp

* Mon Mar 16 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-fgfs)

