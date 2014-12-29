# vim: set ft=spec : -*- rpm-spec -*-
%define autossh_user      _autossh
%define autossh_group     _autossh
%define autossh_dir      /var/lib/autosshd

Name: autosshd
Version: 0.0.3
Release: alt8

Summary: System administration - AutoSSH system level service

Group: System/Servers
License: GPL
Url: http://wiki.etersoft.ru/Autosshd

Packager: Danil Mikhailov <danil@altlinux.org>

#Source-git: https://github.com/vitlav/autosshd
Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm-build-intro

Requires: shadow-utils openssh-common
Requires: autossh

%description
Run autossh as system service at startup.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/autossh.d/

mkdir -p %buildroot%_runtimedir/%name/
mkdir -p %buildroot%_locksubsysdir/%name/
mkdir -p %buildroot/%_tmpfilesdir/

cat <<EOF >%buildroot/%_tmpfilesdir/%name.conf
d %_runtimedir/%name 0755 %autossh_user %autossh_group
d %_locksubsysdir/%name 0755 root root
EOF

mkdir -p %buildroot/%autossh_dir/.ssh/
#echo "StrictHostKeyChecking no" > %buildroot%autossh_dir/.ssh/config

mkdir -p %buildroot%_docdir/%name/

install -D -m754 etc/rc.d/init.d/autosshd %buildroot%_initdir/%name
# TODO: we need automate filling of this config
install -D -m644 etc/sysconfig/autosshd %buildroot%_sysconfigdir/%name

install -m644 etc/autossh.d/*.conf.template %buildroot%_sysconfdir/autossh.d/

mkdir -p %buildroot%_datadir/%name/
mkdir -p %buildroot%_bindir/
cp usr/bin/autosshd-ssh %buildroot%_bindir/
cp share/autossh-conf %buildroot%_datadir/%name/
cp share/autosshd.setup* %buildroot%_datadir/%name/

%pre
# Add the "_autossh" user
%_sbindir/groupadd -r -f %autossh_group 2>/dev/null ||:
%_sbindir/useradd -M -r -g %autossh_group -c 'Autossh daemon' \
	-s /dev/null -d %autossh_dir %autossh_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc/*
%attr(750,%autossh_user,%autossh_group) %dir %autossh_dir/
%config(noreplace) %attr(750,%autossh_user,%autossh_group) %autossh_dir/.ssh/
%config(noreplace) %_sysconfigdir/%name
%_sysconfdir/autossh.d/
%_initdir/%name
%_tmpfilesdir/%name.conf
%attr(750,%autossh_user,%autossh_group) %dir %_runtimedir/%name/
%dir %_locksubsysdir/%name/
%dir %_datadir/%name/
%_datadir/%name/autossh-conf
%_datadir/%name/autosshd.setup
%_datadir/%name/autosshd.setup.user
%_bindir/autosshd-ssh

%changelog
* Mon Dec 29 2014 Danil Mikhailov <danil@altlinux.org> 0.0.3-alt8
- fixed test sudo autosshd-ssh anyssh.ru

* Wed Dec 17 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt7
- small fixes

* Thu Nov 27 2014 Danil Mikhailov <danil@altlinux.org> 0.0.3-alt6
- Cleanup git log

* Thu Sep 18 2014 Danil Mikhailov <danil@altlinux.org> 0.0.3-alt5
- Correct manual in config files

* Wed Sep 17 2014 Danil Mikhailov <danil@altlinux.org> 0.0.3-alt4
- added cheking for existing config

* Wed Sep 17 2014 Danil Mikhailov <danil@altlinux.org> 0.0.3-alt3
- move files in right directory
- fix start when already running

* Thu Sep 11 2014 Danil Mikhailov <danil@altlinux.org> 0.0.3-alt2
- rewrite doc
- rewrite init script
- added new scripts:
- autosshd-conf for export variables to _anyssh user
- autosshd-ssh for test connection over ssh

* Mon Jul 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt1
- development release
- rewrite init script
- add anyssh.ru.conf.example
- add unused generate key script
- cleanup spec, move initialize code to a separate script

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
