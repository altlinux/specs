Name: lastlog-notification
Version: 0.3
Release: alt1

Summary: Notify user about last login via freedesktop notification
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar
Requires: shadow-log openldap-clients bind-utils

%description
Notify user about last login via freedesktop notification. It support
both local and kerberos logins. In kerberos case last login on any
workstation time is shown.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/
mkdir -p %buildroot%_bindir
install -pm755 lastlog-notification-{store,show} %buildroot%_bindir
mkdir -p %buildroot/etc/xdg/autostart
install -pm644 lastlog-notification.desktop %buildroot/etc/xdg/autostart/
mkdir -p %buildroot/var/cache/lastlog-notification

%files
%hookdir/*
%_bindir/*
/etc/xdg/autostart/*
%dir /var/cache/lastlog-notification

%changelog
* Thu Aug 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- move cache out from /home

* Thu Aug 29 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- ability to run install script outside of installer

* Tue Aug 27 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- added support for never logged users

* Fri Aug 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build



