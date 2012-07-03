Name: daemontools-astmanproxy
Summary: Daemontools script for Asterisk manager proxy
Version: 0.1
Release: alt7
License: GPL
Group: System/Servers
Url: http://git.altlinux.org/people/mithraen/packages/daemontools-astmanproxy.git

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name

Requires(pre): daemontools
Requires(pre): astmanproxy

BuildPreReq: daemontools-common

%description
%summary

%install
%daemontools_install %SOURCE0 astmanproxy

%triggerpostun -- astmanproxy
%daemontools_postun astmanproxy astmanproxy _asterisk

%triggerin -- astmanproxy
%daemontools_postin astmanproxy

%files
%daemontools_conf/astmanproxy
%changelog
* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt7
- auto rebuild

* Mon Apr 20 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt6
- add Url (for repocop)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt5
- cleanup spec

* Fri Nov 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt4
- rebuild for last daemontools

* Sat Aug 26 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt3
- cleanup

* Fri Aug 25 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- fix patch to daemontools dir

* Wed Aug 23 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus
