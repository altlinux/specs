Summary: Inotify cron system
Name: incron
Version: 0.5.12
Release: alt4

Group: System/Base
License: GPLv2
Url: http://inotify.aiken.cz
Source0: http://inotify.aiken.cz/download/incron/%name-%version.tar
Source1: incrond.init
Source2: incrontab.control
Source3: incrond.service
Patch0: %name-%version-alt.patch

# Automatically added by buildreq on Sun May 24 2009
BuildRequires: gcc-c++

%description
This program is an "inotify cron" system.
It consists of a daemon and a table manipulator.
You can use it a similar way as the regular cron.
The difference is that the inotify cron handles
filesystem events rather than time periods.

%prep
%setup -q
%patch0 -p1

%build
%make CXXFLAGS="%optflags -std=c++14"

%install
#install files manually since source Makefile tries to do it as root
install -D -p incrond %buildroot%_sbindir/incrond
install -D -p -m 4755 incrontab %buildroot%_bindir/incrontab
install -d %buildroot%_var/spool/%name
install -d %buildroot%_sysconfdir/%name.d
install -D -p %SOURCE1 %buildroot%_initdir/incrond
install -D -p %SOURCE2 %buildroot%_controldir/incrontab
install -D -p -m 0644 incron.conf.example %buildroot%_sysconfdir/%name.conf
install -D -m644 %SOURCE3 %buildroot%_unitdir/incrond.service

# install manpages
make install-man MANPATH="%buildroot%_mandir" INSTALL="install -D -p"

%pre
/usr/sbin/groupadd -r -f incrontab &>/dev/null
%pre_control incrontab

%post
%post_control incrontab
%post_service incrond

%preun
%preun_service incrond

%files
%doc COPYING CHANGELOG README TODO LICENSE-GPL
%attr(700,root,root) %_bindir/incrontab
%_sbindir/incrond
%_initdir/incrond
%config(noreplace) %_sysconfdir/%name.conf
%_controldir/incrontab
%_mandir/man1/incrontab.1.*
%_mandir/man5/incrontab.5.*
%_mandir/man5/incron.conf.5.*
%_mandir/man8/incrond.8.*
%attr(3730,root,incrontab) %dir %_var/spool/%name
%attr(700,root,root) %dir %_sysconfdir/%name.d
%_unitdir/incrond.service

%changelog
* Tue Nov 22 2022 Anton Farygin <rider@altlinux.ru> 0.5.12-alt4
- added patch from upstream against zombie processes (closes: #43764)

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 0.5.12-alt3
- fixed FTBFS: force C++14

* Wed Jan 16 2019 Anton Farygin <rider@altlinux.ru> 0.5.12-alt2
- removed ubt

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 0.5.12-alt1
- added %%ubt

* Thu Jul 21 2016 Anton Farygin <rider@altlinux.ru> 0.5.12-alt1
- new version

* Fri Aug 15 2014 Denis Smirnov <mithraen@altlinux.ru> 0.5.10-alt2
- add systemd unit

* Wed Oct 09 2013 Anton Farygin <rider@altlinux.ru> 0.5.10-alt1
- new version

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.1
- Fixed build with glibc 2.16

* Thu Sep 10 2009 Anton Farygin <rider@altlinux.ru> 0.5.9-alt1
- new version

* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 0.5.8-alt2
- use group incrontab instead of crontab

* Sun May 24 2009 Anton Farygin <rider@altlinux.ru> 0.5.8-alt1
- first build for Sisyphus, based on RH spec

