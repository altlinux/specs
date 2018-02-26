Name: autordp
Version: 0.1
Release: alt2

Summary: autologin setup to start grdesktop
License: Public domain
Group: System/X11

Url: http://www.altlinux.org/Installer/beans
Source0: xinit-rdp
Source1: xsession-grdesktop
Source2: autologin.sysconfig
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: autologin grdesktop

# as in livecd
%define autordp_user altlinux

%description
%name is a glue between autologin and grdesktop packages
so that the former would be set up to run the latter and
user could log into a windows terminal session directly

%prep
%install
install -pD -m755 %SOURCE0 %buildroot%_bindir/xinit-rdp
install -pD -m755 %SOURCE1 %buildroot%_bindir/xsession-grdesktop
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/autologin

%pre
%_sbindir/useradd -c '%name user' -G xgrp %autordp_user \
                  2>/dev/null ||: # no need for -r, we need $HOME

%files
%_bindir/*
%config(noreplace) %_sysconfdir/sysconfig/autologin

%changelog
* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- yes, we add pseudo real user not pseudo system user. :)

* Fri Aug 01 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release
