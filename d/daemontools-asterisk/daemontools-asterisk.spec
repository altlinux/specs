Name: daemontools-asterisk
Summary: Daemontools script for Asterisk
Version: 0.6
Release: alt1
License: GPL
Group: System/Servers
Url: http://git.altlinux.org/people/mithraen/packages/daemontools-asterisk.git

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name

Requires(pre): daemontools-common
Requires: virt-what
Requires: asterisk-initscript >= 0.69

BuildPreReq: daemontools-common

%description
%summary

%install
%daemontools_install %SOURCE0 asterisk
touch %buildroot%_sysconfdir/daemontools.d/asterisk/down

%files
%_sysconfdir/daemontools.d/asterisk
%changelog
* Fri Feb 12 2016 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt1
- not wait for dahdi when started inside VE

* Tue Aug 11 2015 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt1
- start Asterisk from initscript

* Sat Aug 21 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4-alt1
- create coredumps
- wait for DAHDI initialize before start

* Tue Sep 22 2009 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- fix requires

* Mon Sep 14 2009 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- pbxadmin group support
- dahdi support

* Mon Apr 20 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt7
- add Url (for repocop)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt6
- cleanup spec

* Fri Nov 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt5
- rebuild for last daemontools

* Mon Sep 24 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt4
- fix triggers

* Mon Apr 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt3
- update to asterisk1.4

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- not requires asterisk, but requires asterisk-initscript

* Wed Aug 23 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus
