Name: rsyslog-server-listen
Version: 0.1
Release: alt2

Summary: provide rsyslog configuration for listening
License: Public domain
Group: System/Configuration/Other

Url: http://www.rsyslog.com/using-the-syslog-receiver-module/
Requires: rsyslog
BuildArch: noarch

%define rsyslogdir %_sysconfdir/rsyslog.d

%description
%summary

%prep

%install
install -d %buildroot%rsyslogdir
cat > %buildroot%rsyslogdir/90_server.conf << "EOF"
$ModLoad immark # provides --MARK-- message capability
$ModLoad imudp # provides UDP syslog reception
$ModLoad imtcp # provides TCP syslog reception and GSS-API (if compiled to support it)

$UDPServerRun 514
$InputTCPServerRun 514
EOF

%files
%rsyslogdir/90_server.conf

%changelog
* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- whoops, added missing Requires:

* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

