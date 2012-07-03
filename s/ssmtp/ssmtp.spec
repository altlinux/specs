Name: ssmtp
Summary: ssmtp - extremely simple MTA to get mail off the system to a mail hub
Version: 2.64
Release: alt2
License: GPL
Group: System/Servers
BuildRequires: libssl-devel
Packager: Denis Smirnov <mithraen@altlinux.ru>
Url: http://packages.qa.debian.org/s/ssmtp.html
Source: %name-%version-%release.tar
Conflicts: sendmail sendmail-submit
Conflicts: postfix
Conflicts: masqmail
Conflicts: exim exim-common
Provides: MTA
Requires: ssmtp-common = %version-%release

%package common
Summary: ssmtp - common files
Group: System/Servers
Conflicts: exim-common

%description common
extremely simple MTA to get mail off the system to a mail hub
A secure, effective and simple way of getting mail off a system to your
mail hub. It contains no suid-binaries or other dangerous things - no mail
spool to poke around in, and no daemons running in the background. Mail is
simply forwarded to the configured mailhost. Extremely easy configuration.
WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.


%package docs
Summary: ssmtp documentation
Group: System/Servers

%description docs
extremely simple MTA to get mail off the system to a mail hub
A secure, effective and simple way of getting mail off a system to your
mail hub. It contains no suid-binaries or other dangerous things - no mail
spool to poke around in, and no daemons running in the background. Mail is
simply forwarded to the configured mailhost. Extremely easy configuration.
WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.


%package ssl
Summary: ssmtp - extremely simple MTA to get mail off the system to a mail hub
Group: System/Servers
Provides: ssmtp
Conflicts: sendmail sendmail-submit
Conflicts: postfix
Conflicts: masqmail
Conflicts: exim exim-common
Requires: ssmtp-common = %version-%release

%description ssl
extremely simple MTA to get mail off the system to a mail hub
A secure, effective and simple way of getting mail off a system to your
mail hub. It contains no suid-binaries or other dangerous things - no mail
spool to poke around in, and no daemons running in the background. Mail is
simply forwarded to the configured mailhost. Extremely easy configuration.
WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.


%description
extremely simple MTA to get mail off the system to a mail hub
A secure, effective and simple way of getting mail off a system to your
mail hub. It contains no suid-binaries or other dangerous things - no mail
spool to poke around in, and no daemons running in the background. Mail is
simply forwarded to the configured mailhost. Extremely easy configuration.
WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.


%prep
%setup
mkdir nossl
cp * nossl/ ||:
cp -a debian md5auth nossl/ ||:

%build
%autoreconf
%configure --enable-ssl --enable-md5auth --enable-inet6
%make_build
cd nossl/
%configure --disable-ssl --enable-md5auth --enable-inet6
%make_build

%install
mkdir -p %buildroot{%_sbindir,%_sysconfdir/%name,%_man8dir}
install %name %buildroot%_sbindir/%name-ssl
install nossl/%name %buildroot%_sbindir/%name
install -m 644 %name.conf %buildroot%_sysconfdir/%name
install -m 644 revaliases %buildroot%_sysconfdir/%name
install -m 644 %name.8 %buildroot%_man8dir
ln -sf %_sbindir/%name %buildroot%_sbindir/sendmail
ln -sf %_sbindir/sendmail %buildroot%_sbindir/mailq
ln -sf %_sbindir/sendmail %buildroot%_sbindir/newaliases

%preun ssl
rm -f %_sbindir/sendmail

%post ssl
ln -sf %_sbindir/%name-ssl	%_sbindir/sendmail

%files
%_sbindir/sendmail
%_sbindir/%name

%files common
%_sbindir/mailq
%_sbindir/newaliases
%config(noreplace) %_sysconfdir/%name
%_man8dir/*

%files docs
%doc README TLS CHANGELOG_OLD INSTALL COPYING debian/changelog

%files ssl
%ghost %_sbindir/sendmail
%_sbindir/%name-ssl

%changelog
* Tue Jun 19 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.64-alt2
- fixed build with recent toolchain
- ipv6 support enabled
- in-tree patches applied (or dropped)

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 2.64-alt1
- 2.64
- fixed Url:

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt12
- rebuild with new openssl

* Sun Aug 29 2010 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt11
- ALT #23846

* Fri Aug 27 2010 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt10
- ALT #23964
- CVE-2008-7258

* Fri May 14 2010 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt9
- fix default config (ALT #23483)

* Fri Jul 03 2009 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt8
- add conflict to exim-common from smtp-common
- add Url tag

* Sun Apr 26 2009 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt7
- add UseSTARTTLE (ALT #10128)
- split package (create ssmtp-common with files common to ssmtp and ssmtp-tls)

* Sat Dec 13 2008 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt6
- add conflict to sendmail-submit

* Thu Dec 11 2008 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt5
- add some conflicts

* Mon Nov 24 2008 Denis Smirnov <mithraen@altlinux.ru> 2.62.2-alt4
- Add mailq and newaliases links
- cleanup spec
- update to 2.62.2

* Wed Apr 09 2008 Denis Smirnov <mithraen@altlinux.ru> 2.60.9-alt4
- don't use 'install -s'

* Tue Feb 07 2006 Denis Smirnov <mithraen@altlinux.ru> 2.60.9-alt3
- create separate packages ssmtp and ssmtp-ssl

* Sat Feb 05 2005 LAKostis <lakostis at altlinux dot ru> 2.60.9-alt2.3
- add %_sbindir/sendmail to file list.
- add conflicts section (guess other MTA should also update own conflicts)

* Sat Feb 05 2005 LAKostis <lakostis at altlinux dot ru> 2.60.9-alt2.2
- spec cleanup.
- add MTA to Provides.

* Sat Aug 14 2004 LAKostis <lakostis at altlinux dot ru> 2.60.9-alt2.1
- fix md5-auth patch.
- add manpage.

* Fri Jun 18 2004 LAKostis <lakostis at altlinux dot ru> 2.60.9-alt2
- comment out generate_config - it mostly useless.
- add docs section.
- fix permissions for config files.

* Fri Jun 18 2004 LAKostis <lakostis at altlinux dot ru> 2.60-alt1.9
- initial build for Sisyphus.
