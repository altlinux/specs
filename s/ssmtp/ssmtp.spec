Name: ssmtp
Summary: ssmtp - extremely simple MTA to get mail off the system to a mail hub
Version: 2.64
Release: alt6
License: GPL-2.0-or-later
Group: System/Servers
BuildRequires: libssl-devel
Url: https://packages.debian.org/stable/mail/ssmtp
VCS: https://salsa.debian.org/debian/ssmtp.git
Source: %name-%version.tar
Patch1: ssmtp-2.64-fedora-md5auth-non-rsa.patch
Patch2: ssmtp-2.64-fedora-garbage_writes.patch
Patch3: ssmtp-2.64-fedora-authpass.patch
Patch4: ssmtp-2.64-fedora-aliases.patch
Patch5: ssmtp-2.64-fedora-remote-addr.patch
Patch6: ssmtp-2.64-fedora-validate-TLS-server-cert.patch
Patch7: ssmtp-2.64-defaultvalues.patch
Patch8: ssmtp-2.64-fedora-c99.patch
Patch9: ssmtp-2.64-fedora-configure-c99.patch
Conflicts: sendmail sendmail-submit
Conflicts: postfix
Conflicts: masqmail
Conflicts: exim exim-common
Provides: MTA
Requires: ssmtp-common = %version-%release

%description
extremely simple MTA to get mail off the system to a mail hub
A secure, effective and simple way of getting mail off a system to your
mail hub. It contains no suid-binaries or other dangerous things - no mail
spool to poke around in, and no daemons running in the background. Mail is
simply forwarded to the configured mailhost. Extremely easy configuration.
WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.


%package common
Summary: ssmtp - common files
Group: System/Servers
Conflicts: exim-common
Requires: sendmail-common %_sbindir/mailq %_sbindir/newaliases
Requires: ssmtp-tools = %EVR

%description common
extremely simple MTA to get mail off the system to a mail hub
A secure, effective and simple way of getting mail off a system to your
mail hub. It contains no suid-binaries or other dangerous things - no mail
spool to poke around in, and no daemons running in the background. Mail is
simply forwarded to the configured mailhost. Extremely easy configuration.
WARNING: the above is all it does; it does not receive mail, expand aliases
or manage a queue. That belongs on a mail hub with a system administrator.

%package tools
Summary: ssmtp - ssmtp and ssmtp-ssl executables
Group: System/Servers

%description tools
ssmtp-tools contains ssmtp and ssmtp-ssl executables.

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


%prep
%setup
%autopatch -p1

%build
%configure --enable-ssl --enable-md5suth  --enable-inet6
%make_build

%install
mkdir -p %buildroot{%_sbindir,%_sysconfdir/%name,%_man8dir}
install %name %buildroot%_sbindir/%name
install -m 644 %name.conf %buildroot%_sysconfdir/%name
install -m 644 revaliases %buildroot%_sysconfdir/%name
install -m 644 %name.8 %buildroot%_man8dir
ln -sf %_sbindir/%name %buildroot%_sbindir/sendmail

%files
%_sbindir/sendmail

%files tools
%_sbindir/%name
%_man8dir/*
%config(noreplace) %_sysconfdir/%name/%name.conf

%files common
%config(noreplace) %_sysconfdir/%name/revaliases

%files docs
%doc README TLS CHANGELOG_OLD INSTALL COPYING debian/changelog

%changelog
* Mon Feb 10 2025 Anton Farygin <rider@altlinux.ru> 2.64-alt6
- built from debian git tag 2.64
- built with fixes from Fedora
- removed ssl subpackage (ssl configuration now in main package)
- enabled ipv6 support
- updated homepage URL and License

* Tue Jun 25 2024 Aleksey Cheusov <cheusov@altlinux.org> 2.64-alt5
- Set correct License

* Mon Jun 24 2024 Aleksey Cheusov <cheusov@altlinux.org> 2.64-alt4
- Separate sbin/ssmtp and sbin/ssmtp-ssl into an individual package
  for using them as a standalone mail sender.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.64-alt3.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Nov 16 2012 Dmitry V. Levin <ldv@altlinux.org> 2.64-alt3
- %name-common: Removed %_sbindir/{mailq,newaliases},
  added sendmail-common requirements.

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
