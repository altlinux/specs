%define postgrey_user postgrey
%define postgrey_group postgrey
%define postgrey_home %_localstatedir/%name

Name: postgrey
Version: 1.33
Release: alt1.1

Summary: Greylisting Policy Server for Postfix and Exim
License: GPL
Group: System/Servers

URL: http://postgrey.schweikert.ch
BuildArch: noarch
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %{name}_clients_dump
Source6: %name.README.ALT

BuildPreReq: perl perl-base perl-IO-Multiplex perl-Net-Server perl-BerkeleyDB perl-Net-DNS
Requires: perl-IO-Multiplex
BuildRequires: perl-podlators

%description
Postgrey is a Postfix policy server implementing greylisting.
When a request for delivery of a mail is received by Postfix 
via SMTP, the triplet CLIENT_IP / SENDER / RECIPIENT is built. 
If it is the first time that this triplet is seen, or if the 
triplet was first seen less than 5 minutes, then the mail gets 
rejected with a temporary error. Hopefully spammers or viruses 
will not try again later, as it is however required per RFC.
Edit your configuration files:
/etc/postfix/main.cf:
  smtpd_recipient_restrictions = ...
    check_policy_service unix:postgrey/socket, ...
or if you like to use inet sockets (modify the IP if needed):
/etc/sysconfig/postgrey:
  OPTIONS="--inet=127.0.0.1:60000"
/etc/postfix/main.cf:
  smtpd_recipient_restrictions = ...
    check_policy_service inet:127.0.0.1:60000, ...

%prep
%setup

%install
# directories
install -d -m1711 %buildroot%_localstatedir/%name
install -d -m1755 %buildroot%_var/run/%name

# binaries
install -pD -m0755 %name %buildroot%_sbindir/%name
install -pD -m0755 contrib/postgreyreport %buildroot%_sbindir/postgreyreport
install -m0755 %SOURCE3 %buildroot%_sbindir/%{name}_clients_dump

# initscript and sysconfig-file
install -pD -m0755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

# whitelists
install -pD -m0644 postgrey_whitelist_clients %buildroot%_sysconfdir/%name/whitelist_clients
install -pD -m0644 postgrey_whitelist_recipients %buildroot%_sysconfdir/%name/whitelist_recipients
touch %buildroot%_sysconfdir/%name/whitelist_clients.local

# README.ALT
install -pD -m0644 %SOURCE6 README.ALT

# manpages
pod2man %name >%name.1
install -pD -m0644 %name.1 %buildroot%_man1dir/%name.1
pod2man contrib/postgreyreport > postgreyreport.1
install -pD -m0644 postgreyreport.1  %buildroot%_man1dir/postgreyreport.1

%pre
/usr/sbin/groupadd -r -f %postgrey_group ||:
/usr/sbin/useradd -g %postgrey_group -c 'The Postgrey Daemon' \
        -d %postgrey_home -s /dev/null -r %postgrey_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/%name/*
%dir %attr(1771,root,%postgrey_group) %_localstatedir/%name
%dir %attr(1775,root,%postgrey_group) %_var/run/%name
%_man1dir/*
%doc README* Changes

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jun 04 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.33-alt1
- 1.33

* Wed Nov 18 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.32-alt2
- Update targrey patch to targrey-0.31-postgrey-1.32.patch.

* Wed Aug 20 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.32-alt1
- 1.32

* Sun May 25 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.31-alt2
- Fixed 'collecd socket' option name in help text
- Dropped dogwatch subpackage. Please use monit instead

* Fri Sep 14 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.31-alt1
- 1.31

* Wed Aug 15 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.30-alt2
- Fix whitelists filenames. This bug introduced in version 1.28.
  (Closes: #12572)

* Tue Aug 07 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.30-alt1
- 1.30

* Tue Jul 24 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.29-alt1
- 1.29

* Thu Jul 19 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.28-alt1
- 1.28

* Tue Feb 13 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.27-alt4
- Add tarpitting support (patch by SATOH Kiyoshi)
- Add collectd support (patch by Alexander Wirt)
- Integrate patches

* Wed Nov 22 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.27-alt3
- Fix default path to database in postgreyreport script (Closes: #10288)
- Move postgreyreport and postgrey_clients_dump from contrib to %%_sbindir
- Generate manpage for postgreyreport

* Tue Oct 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.27-alt2
- Enabled manpage generation

* Tue Jul 25 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.27-alt1
- 1.27
- Enhanced Summary (because added support for Exim)

* Fri Mar 17 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.24-alt2
- Corrected path to whitelist_recipients file (reported by dfo@)

* Tue Feb 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.24-alt1
- 1.24
- Rediffed postgrey-1.21-alt.patch and renamed to postgrey-1.24-alt.patch
- Don't use %%__install macro anymore

* Sat Nov 26 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.23-alt1
- 1.23

* Thu Oct 27 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.22rc1-alt1
- Updated to version 1.22rc1 due to possible bug with format-string problems
- Changed permissions of /var/lib/postgrey/ and /var/run/postgrey due to ALT
  security policy
- Fixed stupid bug with contrib-packaging
- Added postgrey-dogwatch by dfo@ request (separate package)
- Removed postfix from Requires
- Minor spec changes
- Added README.ALT

* Wed Oct 12 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.21-alt3
- Fix missing requires (perl-IO-Multiplex) (Closes: #8202)
- Service postgrey now disabled on any runlevels by default

* Tue Sep 06 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.21-alt2
- Spec cleanup
- Removed unneeded actions in %%postun

* Mon Jul 25 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 1.21-alt1
- Initial build for Sisyphus
- Added postgrey-1.21-alt.patch - fix default user/group, config and DB locations.
- Added postgrey_clients_dump script from Debian into contrib.
