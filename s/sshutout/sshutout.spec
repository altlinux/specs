Name: sshutout
Version: 1.0.6
Release: alt2

Summary: Stop SSH dictionary attacks
License: GPL
Group: Security/Networking

Url: http://www.techfinesse.com/sshutout/sshutout.html
Source0: %name-%version.tar.gz
Source1: %name.init
Source2: %name.conf
Packager: Michael Shigorin <mike@altlinux.org>

Requires: net-tools iptables

%description
sshutout periodically monitors log files looking for multiple
failed login attempts via the sshd (optionally, sshd2).  It is
meant to mitigate what is commonly known as "dictionary attacks,"
i.e. scripted brute force attacks that use lists of user IDs and
passwords to effect unauthorized intrusions.  Typically such
attacks fill up the system logs with hundreds or even thousands
of log entries for the failed login attempts.  Aside from the
nuisance of wasted space, wasted bandwidth, and reduced signal
to noise ratio in the logs, the attacks can pose a real danger
to systems with weak ID and password combinations.

This package blunts such attacks by creating firewall rules to
block individual offenders from accessing the system.  These rules
are created when an attack signature is detected, and after a
configurable expiry interval has elapsed, the rules are deleted.

While sshutout can help reduce the severity and impact of
dictionary attacks, it is by no means a substitute for a good
password policy.  A password policy is the front line of defense
against intrusion and should be given careful consideration.
sshutout is merely one small tool intended to help reduce log
clutter and diminish the incentive to mount dictionary attacks.

%prep
%setup

%build
%make_build

%install
install -pDm755 %name %buildroot%_sbindir/%name
install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/%name.conf

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%name
%_initdir/%name
%_sysconfdir/%name.conf
%doc License README TODO sshutout.html 

%changelog
* Tue Jan 12 2010 Michael Shigorin <mike@altlinux.org> 1.0.6-alt2
- added Requires: net-tools iptables (closes: #22723)
  + thanks Andrey Chichak for the suggestion

* Mon Dec 07 2009 Michael Shigorin <mike@altlinux.org> 1.0.6-alt1
- 1.0.6
  + dropped patches (merged upstream)
- default sshd_log_file changed (less noisy):
  from /var/log/messages
    to /var/log/auth/secure
- trivial spec cleanup

* Wed Oct 14 2009 Michael Shigorin <mike@altlinux.org> 1.0.5-alt3
- applied patch by A.Kitouwaykin <cetus newmail ru> to add
  "UNKNOWN USER" pattern recognition (closes: #21869)
- minor spec cleanup

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 1.0.5-alt2
- fix FTBFS against recent glibc

* Thu Jul 03 2008 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- built for ALT Linux

