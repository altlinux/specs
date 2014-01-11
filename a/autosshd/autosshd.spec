# vim: set ft=spec : -*- rpm-spec -*-
%define autossh_user      _autossh
%define autossh_group     _autossh

Name: autosshd
Version: 0.0.2
Release: alt8

Summary: System administration - AutoSSH system level service
Group: System/Servers
License: GPL
Url: http://wiki.etersoft.ru/Autosshd
Packager: Vitaly Lipatov <lav@altlinux.ru>

# http://git.etersoft.ru/people/lav/packages/autosshd.git
Source: %name.tar

BuildArch: noarch

PreReq: pwgen shadow-utils openssh-common

BuildPreReq: rpm-build-intro

Requires: autossh

%description
Run autossh as system service at startup.

%prep
%setup -n autosshd

%install
mkdir -p %buildroot%_initdir/
mkdir -p %buildroot%_sysconfigdir/
mkdir -p %buildroot/var/run/%name/
mkdir -p %buildroot/var/lock/subsys/%name/
mkdir -p %buildroot/lib/tmpfiles.d
echo 'd /var/run/%name 0755 %autossh_user %autossh_group' > %buildroot/lib/tmpfiles.d/%name.conf
echo 'd /var/lock/subsys/%name 0755 root root' >> %buildroot/lib/tmpfiles.d/%name.conf
mkdir -p %buildroot/var/lib/%name/.ssh
mkdir -p %buildroot%_docdir/%name/

install -D -m750 etc/rc.d/init.d/autosshd %buildroot%_initdir/%name
install -D -m640 etc/sysconfig/autosshd %buildroot%_sysconfigdir/%name

%pre
# Add the "_autossh" user
%_sbindir/groupadd -r -f %autossh_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %autossh_group -c 'Autossh daemon' \
	-s /dev/null -d /var/lib/autosshd %autossh_user 2>/dev/null ||:
%_sbindir/usermod -p `pwgen -s 24 1` %autossh_user

%post
if [ ! -f /var/lib/autosshd/.ssh/id_dsa ]; then
    mkdir -p /var/lib/autosshd/.ssh
    /usr/bin/ssh-keygen -t dsa -b 1024 -C "AutoSSH daemon" -N "" -q -f /var/lib/autosshd/.ssh/id_dsa
    echo "StrictHostKeyChecking no" > /var/lib/autosshd/.ssh/config
    cp /var/lib/autosshd/.ssh/id_dsa.pub /var/lib/autosshd/.ssh/authorized_keys
fi
chown -R %autossh_user:%autossh_group /var/lib/autosshd/

%post_service %name

%preun
%preun_service %name

%triggerpostun -- autosshd < 0.0.2-alt5
echo "Fixing permissions after faulty previous package:"
%_sbindir/groupadd -r -f %autossh_group ||:
%_sbindir/useradd  -r -g %autossh_group -c 'Autossh daemon' \
	-s /dev/null -d /var/lib/autosshd %autossh_user ||:
%_sbindir/usermod -p `pwgen -s 24 1` %autossh_user
# We need to re-create the dir because userdel -r (from old postun) has removed it
if [ ! -f /var/lib/autosshd/.ssh/id_dsa ]; then
    mkdir -p /var/lib/autosshd/.ssh
    /usr/bin/ssh-keygen -t dsa -b 1024 -C "AutoSSH daemon" -N "" -q -f /var/lib/autosshd/.ssh/id_dsa
    echo "StrictHostKeyChecking no" > /var/lib/autosshd/.ssh/config
    cp /var/lib/autosshd/.ssh/id_dsa.pub /var/lib/autosshd/.ssh/authorized_keys
fi
chown -R %autossh_user:%autossh_group /var/lib/autosshd/
chown %autossh_user:%autossh_group /var/run/autosshd/

%files
%doc doc/*
%_initdir/%name
%config(noreplace) %_sysconfigdir/%name
/lib/tmpfiles.d/%name.conf
%attr(755,%autossh_user,%autossh_group) %dir /var/lib/%name/
%attr(755,%autossh_user,%autossh_group) %dir /var/run/%name/
%dir /var/lock/subsys/%name/

%changelog
* Sat Jan 11 2014 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt8
- doc: Added links to some guides (how to make use of autosshd).

* Fri Jan 10 2014 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt7
- Declare lav@ as the maintainer

* Sat Dec 28 2013 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt6
- Handle /var/lock/subsys/* and /var/run/* in tmpfiles.d
  (otherwise they used to be gone from the tmpfs after a reboot)

* Sat Dec 28 2013 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt5
- Fix user deletion after an upgrade according to http://www.altlinux.org/PseudoUserPolicy

* Sat Dec 28 2013 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt4
- Correct wrong paths in scripts, configs, and examples.

* Tue Nov 19 2013 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt3
- initial build to ALT Linux Sisyphus

* Tue Oct 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt2
- cleanup spec

* Mon Apr 09 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.2-alt1
- Code rewritten to work with multiple connections

* Thu Apr 05 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt4
- Fixed bugs in postinstall and postuninstal scripts

* Tue Apr 03 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt3
- Fixes

* Tue Apr 03 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt2
- Ready for testing

* Mon Apr 02 2012 Dmitriy Kruglikov <dkr@altlinux.org> 0.0.1-alt1
- Initial draft
