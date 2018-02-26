Name: yabeda
Version: 0.0.7
Release: alt1

Summary: Yabeda OVZ complainer
License: GPLv3
Group: System/Base

Url: http://www.assembla.com/wiki/show/yabeda
Source: %name-%version.tar.bz2
Packager: Pavlov Konstantin <thresh@altlinux.ru>

#Requires: ruby ruby-dbi mysql-ruby ruby-xmpp4r ruby-tmail
Requires: ruby
BuildRequires: libruby-devel ruby-stdlibs ruby
BuildArch: noarch

%description
Yabeda is an OpenVZ failcnt complainer which tends to be lightweight,
flexible and easily extendable.

Should be used on host machines (via some cron-job) to generate alerts
when failcnt gets increased. Failcnt is the counter used in OpenVZ
kernels to tell whether the needed parameter reached its limit.

Please install these packages for additional functionality:
- mysql needs:  mysql-ruby ruby-dbi ruby-dbd-mysql
- email needs:  ruby-tmail
- jabber needs: ruby-xmpp4r

%prep
%setup
touch state

%install
install -pDm600 state %buildroot%_localstatedir/yabeda/state
install -pDm750 yabeda.rb %buildroot%_sbindir/yabeda
install -pDm640 yabeda.conf %buildroot%_sysconfdir/yabeda/yabeda.conf
install -pDm644 yabeda.cron %buildroot%_sysconfdir/cron.d/yabeda

%files
%_sysconfdir/cron.d/yabeda
%_sbindir/yabeda
%dir %_localstatedir/yabeda
%ghost %config(noreplace) %attr(600,root,root) %_localstatedir/yabeda/state
%dir %_sysconfdir/yabeda
%config %_sysconfdir/yabeda/yabeda.conf

%changelog
* Sat Sep 25 2010 Michael Shigorin <mike@altlinux.org> 0.0.7-alt1
- a fork?:
  + fix for current sisyphus' ruby
  + drop MIME mail, do it plain and simple
- untie hardwired requires, list them in description instead

* Fri Oct 09 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.0.6-alt4
- Fix syntax for ruby 1.9 one more time.

* Wed Sep 09 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.0.6-alt3
- Fix wrong Requires.

* Thu Sep 03 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.0.6-alt2
- Fix syntax for ruby 1.9.
- Fix #18785.

* Fri May 15 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.0.6-alt1
- 0.0.6 release.

* Fri Aug 29 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.5-alt1
- 0.0.5 release.

* Fri Jul 04 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.4-alt1
- 0.0.4 release.

* Wed Jun 25 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.3-alt1
- 0.0.3 release.

* Thu May 15 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.2-alt1
- 0.0.2 release.

* Tue Feb 05 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.1-alt1
- 0.0.1 release.

