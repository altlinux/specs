%define snapshot 20040310

%define spam_check_user _spam_check
%define spam_check_group _spam_check
%define spam_check_home %_localstatedir/%name

Name: spam_check
Version: 0.2.5
Release: alt8.%snapshot

Summary: Adaptive spam-blocking tool for Postfix and sendmail
License: GPL
Group: System/Servers

Url: http://www.opennet.ru/dev/spam_check
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name.conf
Source2: %name.clean_dn.conf
Source3: %name.cron
Source4: %name.arc_bl.sh
Source5: %name.arc_bl.conf
Source6: %name.copy_bl.sh
Source7: %name.copy_bl.conf
Source8: %name.logrotate
Source9: %name.init
Source20: %name.README.ALT

BuildRequires: perl-BerkeleyDB, perl-File-Tail, perl-base
Requires: su

%description
Adaptive spam-blocking tool for postfix and sendmail

%prep
%setup

%install
install -pD -m0755 spam_check.pl %buildroot%_sbindir/%name.pl
install -pD -m0755 util/access2rbldns.pl %buildroot%_sbindir/access2rbldns.pl
install -pD -m0755 util/rbldns2access.pl %buildroot%_sbindir/rbldns2access.pl
install -pD -m0755 util/clean_dn.pl %buildroot%_sbindir/clean_dn.pl
install -pD -m0644 %SOURCE1 %buildroot%_sysconfdir/%name/%name.conf
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/%name/clean_dn.conf
install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/cron.d/%name
install -pD -m0755 %SOURCE4 %buildroot%_sbindir/arc_bl.sh
install -pD -m0644 %SOURCE5 %buildroot%_sysconfdir/%name/arc_bl.conf
install -pD -m0755 %SOURCE6 %buildroot%_sbindir/copy_bl.sh
install -pD -m0644 %SOURCE7 %buildroot%_sysconfdir/%name/copy_bl.conf
install -pD -m0644 %SOURCE8 %buildroot%_sysconfdir/logrotate.d/%name
install -pD -m0755 %SOURCE9  %buildroot%_initdir/%name
install -pD -m0644 %SOURCE20 README.ALT
install -d -m1771 %buildroot%_var/log/%name
install -d -m1771 %buildroot%_localstatedir/%name
install -d -m1771 %buildroot%_localstatedir/%name/blocklist

%pre
/usr/sbin/groupadd -r -f %spam_check_group ||:
/usr/sbin/useradd -g %spam_check_group -G adm -c 'The spam_check pseudouser' \
	-d %spam_check_home -s /dev/null -r %spam_check_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%_initdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/cron.d/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %_sysconfdir/%name
%dir %attr(1771,root,%spam_check_group) %_var/log/%name
%dir %attr(1771,root,%spam_check_group) %_localstatedir/%name
%dir %attr(1771,root,%spam_check_group) %_localstatedir/%name/blocklist
%doc CHANGES README* TODO dsl_stoplist.txt law_notes.txt tech_notes.txt unknown_notes.txt

%changelog
* Tue Dec 08 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.2.5-alt8.20040310
- Thanslate all russian comments to english in all configs.
- Modify some default settings:
  + cfg_log_watch_mode = 1
  + cfg_ignore_mask = '' (empty)
- README.ALT: include block_list_arc.* to example settings
- Fix rotation number in logrotate script.
- Package accidently forgotten /var/lib/spam_check/blocklist

* Thu Oct 22 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.2.5-alt7.20040310
- Store blocklist in /var/lib/spam_check/ instead of /etc/spam_check/.
- Strip ".txt" postfix from default blocklist names.
- sources/spam_check.logrotate: add rotation of block_list_arc.
- arc_bl.sh, copy_bl.sh: quote variables, improve code appearance.
- arc_bl.sh, copy_bl.sh: use shell-error, rewrite config inclusion.
- copy_bl.conf: add more variables.
- copy_bl.sh: use variables for accessing files.
- arc_bl.sh: fix quoting.

* Tue May 20 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.5-alt6.20040310
- Add dependency on su(1)

* Thu Jan 24 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.5-alt5.20040310
- arc_bl.sh, copy_bl.sh: use .cdb file extensions (Closes: #14100)
- Return true in clean_dn.conf (Closes: #14101)
- Recode all files to utf8
- Enhance domain-masks regexp

* Mon Jan 15 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.5-alt4.20040310
- Now we use config variable $postmap in *_bl.sh , don't call postmap(1)
  directly because it generates dependency on postfix (Closes: #10660)
- Removed #!/usr/bin/perl headers from config files

* Tue Dec 05 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.5-alt3.20040310
- Implemented initscript for work in tail-mode (Closes: #10302)
- Integrate patches into source-tree of 'master' branch

* Tue Aug 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.5-alt2.20040310
- Added spam_check-0.2.5-alt-sendmail.patch for fix access table format when
  used with sendmail (submitted by combr@)

* Thu Jun 29 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2.5-alt1.20040310
- Initial build for Sisyphus 
