%define _sbin %_prefix/sbin

Name: rinetd
License: GPL2+
Group: Networking/Other
Version: 0.62
Release: alt3
Summary: TCP Redirection Server
Url: http://www.boutell.com/rinetd/
Source0: %name-%version.tar
Source1: %name.init
Source2: logrotate.%name
Source3: %name.service
Patch0: %name-doc.patch
Patch1: %name-syslog.patch
Patch2: %name-conf.patch

%description
rinetd redirects TCP connections from one IP address and port to
another address and port. rinetd is a single-process server which
handles any number of connections to the address or port pairs
specified in the file /etc/rinetd.conf. Because rinetd runs as a single
process using nonblocking I/O, it is able to redirect a large number of
connections without a severe impact on the machine. This makes it
practical to run TCP services on machines inside an IP masquerading
firewall.

Note: rinetd can not redirect FTP because FTP requires more than one
socket.

%prep
%setup
%patch0
%patch1
%patch2

%build
%make_build

%install
mkdir -p %buildroot%_man8dir %buildroot%_initdir %buildroot%_logrotatedir %buildroot%_sbin %buildroot%_unitdir
touch %buildroot%_sysconfdir/%name.conf
install -m 700 %name %buildroot%_sbin
install -m 644 %name.8 %buildroot%_man8dir
install -m 755 %SOURCE1 %buildroot%_initdir/%name
install -m 644 %SOURCE2 %buildroot%_logrotatedir/%name
install -m 644 %SOURCE3 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbin/%name
%config %_initdir/%name
%_unitdir/%name.service
%config(missingok,noreplace) %ghost %_sysconfdir/%name.conf
%config(noreplace) %_logrotatedir/%name
%_man8dir/%name.8.*
%doc CHANGES README index.html %name.conf.sample

%changelog
* Thu Sep 25 2014 Terechkov Evgenii <evg@altlinux.org> 0.62-alt3
- Systemd unit file added

* Tue Jan 28 2014 Terechkov Evgenii <evg@altlinux.org> 0.62-alt2
- Spec cleanup

* Tue Jan 28 2014 Terechkov Evgenii <evg@altlinux.org> 0.62-alt1
- Initial build for ALT Linux Sisyphus
