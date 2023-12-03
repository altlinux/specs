%define spamd_dir %_localstatedir/spamd/.spamassassin
%define spamd_sock %_var/run/spamd/socket
%define spamd_user spamd
%define spamd_group spamd
%define spamd_conf %_sysconfdir/sysconfig/spamd

Name: sa-content-filter
Version: 0.1
Release: alt3.qa2

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: spamassassin based content filter
License: GPL
Group: System/Base
BuildArch: noarch

Source1: sa.filter
Source2: sa.conf
Source3: filter.conf
Source4: sa-content-filter-tmpfiles.conf

Requires(pre): postfix >= 2.3.7-alt2.1 spamassassin spamassassin-spamd spamassassin-spamc

%define spamd_options "--socketpath=%spamd_sock -x -P -L --username=%spamd_user --virtual-config-dir=%spamd_dir"

%description
spamassassin based content filter

%install
install -Dpm755 %SOURCE1 %buildroot%_bindir/content-filter
subst 's,@SOCKET@,%spamd_sock,' %buildroot%_bindir/content-filter
install -Dpm755 %SOURCE2 %buildroot%spamd_dir/user_prefs
install -Dpm755 %SOURCE3 %buildroot%_sysconfdir/%name/system
install -Dpm644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
mkdir -p  %buildroot%_var/run/spamd/

%pre
/usr/sbin/useradd -r -g %spamd_group -d /dev/null -s /dev/null -n _filter >/dev/null 2>&1 ||:

%post
if [ "$1" -eq 1 ]; then
	subst 's,SPAMDOPTIONS=.*,SPAMDOPTIONS=%spamd_options,' %spamd_conf
fi
%post_service spamd

%postun
if [ "$1" -eq 0 ]; then
	subst 's,SPAMDOPTIONS=%spamd_options,SPAMDOPTIONS="",' %spamd_conf
fi

%files
%_sysconfdir/%name
%_tmpfilesdir/%name.conf
%_bindir/*
%attr(755,%spamd_user,%spamd_group) %dir %spamd_dir
%attr(644,%spamd_user,%spamd_group) %spamd_dir/user_prefs
%attr(710,%spamd_user,%spamd_group) %dir %_var/run/spamd/

%changelog
* Sun Dec 03 2023 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt3.qa2
- NMU: fix postun trigger

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3.qa1
- NMU: applied repocop patch

* Wed Jul 16 2014 Mikhail Efremov <sem@altlinux.org> 0.1-alt3
- Add /etc/tmpfiles.d/ config.
- Drop all changes in the spamd config if package is removed.

* Fri May 25 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- Use automatic whitelist by default.
- Show default score for some usefull rules.

* Mon Feb 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
