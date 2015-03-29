Name: livecd-0ad
Version: 0.2
Release: alt1

Summary: start 0ad
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: livecd-runapp SysVinit-usermode

%define confdir %_sysconfdir/sysconfig
%define conffile %confdir/livecd-runapp

%description
%summary

%prep

%build

%install
mkdir -p %buildroot%confdir
cat > %buildroot%conffile << _EOF_
BINARY=0ad
_EOF_

%files
%conffile

%changelog
* Tue Mar 17 2015 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- rewrote using livecd-runapp

* Mon Mar 16 2015 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-fgfs)

