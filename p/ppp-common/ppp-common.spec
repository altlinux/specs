Name: ppp-common
Version: 0.5.1
Release: alt1

Summary: PPP and ALTLinux shared files
License: GPL
Group: System/Base
Source: %name-%version.tar.bz2

BuildArch: noarch
Conflicts: net-scripts < 0:0.5.5
Provides: %_sysconfdir/ppp/ip-up.d, %_sysconfdir/ppp/ip-down.d

Summary(ru_RU.UTF-8): Разделяемые файлы для PPP и ALTLinux

%description
This package contains a set of files required to integrate PPP
and other packages.

%description -l ru_RU.UTF-8
Этот пакет содержит набор файлов, необходимых для интеграции PPP
с другими пакетами.

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir
cp -a ppp %buildroot%_sysconfdir/
mkdir -p %buildroot%_sysconfdir/ppp/ip-{up,down}.d

%post
grep -iqs '#.*ppp temp entry' /etc/resolv.conf \
&& echo '***
*** ppp-common: warning: consider removing "ppp temp entry" lines
***             from /etc/resolv.conf to enable automatic DNS; see
***             https://bugzilla.altlinux.org/show_bug.cgi?id=13773
***             for details
***' >&2 \
||:

%files
%config %_sysconfdir/ppp/ip-up
%config %_sysconfdir/ppp/ip-down
%dir %_sysconfdir/ppp/ip-*.d

%changelog
* Wed Jun 03 2009 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- /etc/ppp/ip-up: Fixed bug in openresolv support.

* Mon Jun 01 2009 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- Added openresolv support (by Mikhail Efremov; closes: #19635).

* Mon Dec 31 2007 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- I felt there's still a bug somewhere thus didn't close #13773...
  thanks Andrew Kornilov (hiddenman@) for pointing out the tiny
  little problem with defunctionization of update_chrooted call

* Wed Dec 26 2007 Michael Shigorin <mike@altlinux.org> 0.4.1-alt2
- added %%post-script to warn the administrator in case there was
  a record which should (and now is) indicating that no modification
  of /etc/resolv.conf is needed, and which was treated exactly the
  opposite way before 0.4.1

* Mon Dec 24 2007 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- 0.4.1:
  + should fix #13773 (related to missing /etc/resolv.conf updates)

* Sun Sep 25 2005 Denis Ovsienko <pilot@altlinux.ru> 0.4-alt1
- new version should fix #7845

* Thu Aug 04 2005 Denis Ovsienko <pilot@altlinux.ru> 0.3-alt1
- new version should fix:
	#4249 (stuck "# ppp temp entry" in %_sysconfdir/resolv.conf)
	#3861 (ip-up doesn't update a bunch of resolv.conf's!)
- adjusted Conflicts version

* Thu Jan 13 2005 Denis Ovsienko <pilot@altlinux.ru> 0.2-alt1
- #5840 bugfix

* Mon Jan 03 2005 Denis Ovsienko <pilot@altlinux.ru> 0.1-alt1
- moved %_sysconfdir/ppp/* from net-scripts into ppp-common
- network-config-subsystem'isation
