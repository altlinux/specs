%define _libexecdir /usr/libexec/

Name: jabberd2-jud
Version: 1.2
Release: alt5

Summary: Jabber2 Jabber User Directory (JUD)
License: GPL
Group: System/Servers
Packager: Alexey Sidorov <alexsid@altlinux.ru>
BuildArch: noarch

Source: http://jabberstudio.org/projects/users-agent/releases/Users-Agent-%version.tar.gz
Source1: jabberd2-jud-06jud.cfg
Source2: jabberd2-jud.init
Source3: jabberd2-jud.adapter

Patch1: jabberd2-jud-alt-perl.patch
Patch2: jabberd2-jud-alt-vcard.patch
Patch3: jabberd2-jud-alt-lostdbcon.patch
Patch4: jabberd2-jud-alt-searchall.patch

Patch5: jabberd2-jud-alt-vcard-by.patch
Patch6: jabberd2-jud-alt-pid.patch

Patch7: jabberd2-jud-alt-utf8.patch
Patch8: jabberd2-jud-alt-conf.patch

BuildPreReq: jabber-common perl-Net-Jabber perl-Net-XMPP perl-DBI

Requires: jabberd2-mysql perl-DBD-mysql

%description
Jabber JUD is are Jabber User Directory service for Jabberd2 server.
You can use it with mysql jabberd2's storage only

%prep
%setup -q -n users-agent-%version

# Common patches
%patch01 -p1
%patch02 -p1 

# mysql lost connection 
%patch03 

# for correct search by name/nick etc
%patch04

# search by option
%patch05

# patch for incorrect pid handling
%patch06

# patch for correct UTF8 handling
%patch07

# change default conf for jabberd2's default conf
%patch08 -p1

%build

%install

install -D -m755 users-agent %buildroot%_libexecdir/jabberd2/users-agent

install -D -m644 config.xml %buildroot%_sysconfdir/jabberd2/users-agent.xml
install -D -m644 %SOURCE1 %buildroot%_sysconfdir/jabberd2/cfg.d/06jud.cfg

install -D -m755 %SOURCE2 %buildroot%_initdir/%name

install -pD -m0755 %SOURCE3 %buildroot%_jabber_component_dir/%name

%post
%_jabber_config
%post_service %name

%preun
%preun_service %name

%files
%doc README CHANGES INSTALL
%_libexecdir/*
%attr(0640,root,jabberd2) %config(noreplace) %_sysconfdir/jabberd2/users-agent.xml
%attr(0640,root,jabberd2) %_sysconfdir/jabberd2/cfg.d/*
%_initdir/%name
%_jabber_component_dir/*

%changelog
* Thu Jun 19 2008 Alexey Sidorov <alexsid@altlinux.ru> 1.2-alt5
- Fixed conflict with jabberd2 in %_sysconfdir/jabberd2 dir

* Fri Dec 14 2007 Alexey Sidorov <alexsid@altlinux.ru> 1.2-alt4
- Fix config permissions

* Fri Dec 14 2007 Alexey Sidorov <alexsid@altlinux.ru> 1.2-alt3
- New packager
- fix pidfile
- fix service start/stop/status (fix #11360)
- description correction
- start/stop service on install/remove
- ALT Linux Jabber Policy package
- Added necessary requires
- Added jabberd2-jud-alt-conf.patch for default config for jabberd2
- clearing spec from unnecessary macros
- Build as noarch

* Fri Mar 03 2006 Pavel Boldin <bp@altlinux.ru> 1.2-alt2.1
- Added _libexecdir definition

* Tue Feb 28 2006 Pavel Boldin <bp@altlinux.ru> 1.2-alt2
- Initial release for Sisyphus.

* Wed Dec 07 2005 Pavel Boldin <bp@altlinux.ru> 1.2-alt0.10
- Fixed UTF8, full fix now.

* Tue Dec 06 2005 Pavel Boldin <bp@altlinux.ru> 1.2-alt0.9
- Fixed UTF8 decoding.

* Sun Nov 20 2005 Pavel Boldin <bp@altlinux.ru> 1.2-alt0.8
- Correct PID using.

* Wed Aug 31 2005 Pavel Boldin <bp@altlinux.ru> 1.2-alt0.6
- Fixed unsearchable bug.
- Fixed Search-By bug.

* Wed Aug 17 2005 Boldin Pavel <bp@altlinux.ru> 1.2-alt0.1
- initial build


