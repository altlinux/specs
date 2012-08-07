Name: setup-rsyslog-client
Version: 0.1
Release: alt2

Summary: setup rsyslog client
License: Public domain
Group: System/Configuration/Other

Source: %name
Requires: rsyslog
BuildArch: noarch

%description
a script to %summary

%prep

%install
install -pDm755 %SOURCE0 %buildroot%_sbindir/%name

%files
%_sbindir/*

%changelog
* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- clarified description a bit

* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

