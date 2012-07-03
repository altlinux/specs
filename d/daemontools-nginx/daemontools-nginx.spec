Name: daemontools-nginx
Summary: Daemontools script for nginx
Version: 0.1
Release: alt7
License: GPL
Group: System/Servers
Url: http://git.altlinux.org/people/mithraen/packages/daemontools-nginx.git

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name

Requires(pre): daemontools
Requires(pre): nginx

BuildPreReq: daemontools-common

%description
%summary

%install
%daemontools_install %SOURCE0 nginx

%triggerpostun -- nginx1.3
%daemontools_postun nginx nginx _nginx

%triggerin -- nginx1.3
%daemontools_postin nginx

%files
%daemontools_conf/nginx

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
