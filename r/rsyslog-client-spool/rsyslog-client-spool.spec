Name: rsyslog-client-spool
Version: 0.1
Release: alt2

Summary: provide rsyslog configuration for spooling
License: Public domain
Group: System/Configuration/Other

Url: http://www.rsyslog.com/doc/rsyslog_reliable_forwarding.html
Requires: rsyslog
BuildArch: noarch

%define rsyslogdir %_sysconfdir/rsyslog.d

%description
%summary

%prep

%install
install -d %buildroot%rsyslogdir
cat > %buildroot%rsyslogdir/90_client.conf << "EOF"
$ActionQueueType LinkedList   # use asynchronous processing
$WorkDirectory /var/spool/rsyslog  # default location for work (spool) files
#$ActionQueueFileName srvfwd   # set file name, also enables disk mode
$ActionResumeRetryCount -1    # infinite retries on insert failure
$ActionQueueSaveOnShutdown on # save in-memory data if rsyslog shuts down
EOF

%files
%rsyslogdir/90_client.conf

%changelog
* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- whoops, added missing Requires:

* Tue Aug 07 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

