Name: fetchmail
Version: 6.3.26
Release: alt4

Summary: Full-featured POP/IMAP/ETRN mail retrieval daemon
Group: Networking/Mail
License: GPL

Url: http://www.fetchmail.info

Source0: %name-%version.tar.xz
Source1: %name.init
Source2: %name.service
Source3: fetchmailrc.example
Source10: fetchmailconf-large.png
Source11: fetchmailconf-mini.png
Source12: fetchmailconf.png
Source13: fetchmailconf.desktop
Source100: fetchmail.watch

Patch1: %name-5.6.2-contrib.patch
Patch2: %name-6.3.0-fetchmailconf.patch
Patch3: %name-6.3.3-nopermcheck.patch

Requires: %_sbindir/sendmail
Requires: setup >= 2.1.9-ipl15mdk
Requires: service >= 0.5.28-alt1

BuildPreReq: rpm-build-python
%_python_set_noarch

BuildPreReq: flex libssl-devel python-dev

%define rtdir %_runtimedir/%name

%package -n %{name}conf
Summary: A utility for graphically configuring your %name preferences
Group: System/Configuration/Networking
BuildArch: noarch
Requires: %name = %version-%release, tkinter

%package daemon
Summary: SySV init script for demonize %name for sucking emails
Group: System/Servers
PreReq: %name = %version-%release
PreReq: shadow-utils, chkconfig
BuildArch: noarch

%package contrib
Summary: Various contributed software designed to work with %name
Group: System/Base
Requires: %name = %version-%release
BuildArch: noarch

%package locales
Summary: %name localization
Group: System/Internationalization
Requires: %name = %version-%release
BuildArch: noarch

%description
Fetchmail is a free, full-featured, robust, and well-documented
remote mail retrieval and forwarding utility intended to be used
over on-demand TCP/IP links (such as SLIP or PPP connections).

It retrieves mail from remote mail servers and forwards it to
your local (client) machine's delivery system, so it can then be
read by normal mail user agents such as Mutt, Elm, Pine,
(X)Emacs/Gnus or Mailx.

Fetchmail supports every remote-mail protocol currently in use on
the Internet (POP2, POP3, RPOP, APOP, KPOP, all IMAPs, ESMTP
ETRN) for retrieval.  Then Fetchmail forwards the mail through
SMTP or a mail delivery agent (MDA) program of your choice, so
you can read it through your normal mail client.

You may also want to install and configure a local SMTP server,
such as postfix-smtpd, as that's what fetchmail uses for delivery
by default.

%description -n %{name}conf
Fetchmailconf is a TCL/TK application for graphically configuring
your ~/.%{name}rc preferences file.

Fetchmail has many options which can be daunting to the new user.

This utility takes some of the guesswork and hassle out of
setting up %name.

%description daemon
SySV init script for demonize %name for sucking emails.

%description contrib
Various contributed software designed to work with %name.

%description locales
As there were problems with %name localization, it was disabled;
this package can be used to re-add message translations if deemed
neccessary.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
cp -a %SOURCE3 fetchmailrc.example

%build
export ac_cv_path_procmail=%_bindir/procmail
export ac_cv_path_sendmail=%_sbindir/sendmail
export ac_cv_lib_intl_gettext=no
export CPPFLAGS=-I%_includedir/krb5
%configure \
	--enable-fallback=sendmail \
	--enable-RPA \
	--enable-NTLM \
	--enable-SDPS \
	--with-ssl \
	--with-gssapi \
	--with-kerberos5 \
	--without-kerberos
%make_build

%install
%makeinstall

rm -rf contrib/RCS
chmod 644 contrib/*

install -pDm755 %SOURCE1 %buildroot%_initdir/%name
install -pDm644 %SOURCE2 %buildroot%_unitdir/%name.service
touch %buildroot%_sysconfdir/%{name}rc

install -pDm644 %SOURCE10 %buildroot%_liconsdir/%{name}conf.png
install -pDm644 %SOURCE11 %buildroot%_miconsdir/%{name}conf.png
install -pDm644 %SOURCE12 %buildroot%_niconsdir/%{name}conf.png
install -pDm644 %SOURCE13 %buildroot%_desktopdir/%{name}conf.desktop

mkdir -p %buildroot%rtdir

cat >README.%name-conf <<EOF
Fetchmailconf is a TCL/TK application for graphically configuring your
~/.fetchmailrc preferences file.

Fetchmail has many options which can be daunting to the new user.

This utility takes some of the guesswork and hassle out of setting up
fetchmail.
EOF

%find_lang %name

%pre -n %name-daemon
%_sbindir/groupadd -f %name ||:
%_sbindir/useradd -r -n -M -g %name -d %rtdir -s /dev/null %name &>/dev/null ||:

%triggerpostun -n %name-daemon -- fetchmail-daemon <= 6.3.9-alt1
usermod -d %rtdir %name ||:

%post -n %name-daemon
%post_service %name

%preun -n %name-daemon
%preun_service %name
%files
%_bindir/%name
%_man1dir/%name.*
%doc COPYING FAQ FEATURES NEWS NOTES README README.SSL TODO *.html *.txt
%doc fetchmailrc.example

%files -n %{name}conf
%_bindir/%{name}conf
%python_sitelibdir/*
%_desktopdir/*.desktop
%_niconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png
%_man1dir/%{name}conf.*

%files daemon
%_initdir/%name
%_unitdir/%name.service
%attr(640,root,%name) %config(noreplace,missingok) %_sysconfdir/%{name}rc
%attr(775,root,%name) %rtdir

%files contrib
%doc contrib/*

%files -f %name.lang locales
%changelog
* Mon Jan 22 2018 Terechkov Evgenii <evg@altlinux.org> 6.3.26-alt4
- Fix fetchmail-daemon startup with service-0.5.28-alt1

* Wed May  4 2016 Terechkov Evgenii <evg@altlinux.org> 6.3.26-alt3
- Drop etcnet requirement for fetchmail-daemon (i.e. for systemd-networkd-only setups)

* Thu Jun  4 2015 Terechkov Evgenii <evg@altlinux.org> 6.3.26-alt2
- Systemd unit added (ALT#31049) to daemon subpackage

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 6.3.26-alt1
- new version (watch file uupdate)
- build reverted to srpm again

* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 6.3.23-alt2
- fetchmail-daemon made noarch

* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 6.3.23-alt1
- 6.3.23

* Sat Sep 08 2012 Michael Shigorin <mike@altlinux.org> 6.3.22-alt2
- merge gears repo

* Sat Sep 08 2012 Michael Shigorin <mike@altlinux.org> 6.3.22-alt1
- 6.3.22: security fixes for:
  + CVE-2012-3482: potential DoS/data theft in NTLM auth
  + CVE-2011-3389: disabled SSL attack countermeasures

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.3.21-alt1.1
- Rebuild with Python-2.7

* Mon Aug 22 2011 Michael Shigorin <mike@altlinux.org> 6.3.21-alt1
- 6.3.21

* Tue Jun 07 2011 Michael Shigorin <mike@altlinux.org> 6.3.20-alt1
- 6.3.20
  + fixes CVE-2011-1947: STARTTLS denial of service vulnerability
    (thanks ldv@ for heads-up)

* Sun Jan 16 2011 Michael Shigorin <mike@altlinux.org> 6.3.19-alt1
- 6.3.19

* Mon Oct 11 2010 Michael Shigorin <mike@altlinux.org> 6.3.18-alt1
- 6.3.18 fixes:
  + a regression of the rcfile parser
  + a security bug in debug output (memory exhaustion and abort)
  + SSL usability
- built against libssl-1.0.0a

* Sun May 09 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.3.17-alt1
- 6.3.17
  + CVE-2010-1167: DoS in debug mode with multichar locales

* Thu Apr 15 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.3.16-alt1
- 6.3.16

* Tue Mar 30 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.3.15-alt1
- 6.3.15

* Sat Mar 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 6.3.14-alt1
- 6.3.14
  + CVE-2010-0562: heap overrun in verbose SSL cert' info display
- package COPYING
- remove Packager:
- fix buildreqs
- fix configure warnings about GSSAPI headers
- fix using optflags

* Sun Jan 17 2010 Michael Shigorin <mike@altlinux.org> 6.3.13-alt5
- rebuilt for Sisyphus (thanks real@, see also #22596)

* Sat Jan 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.13-alt4.1
- Built fetchmailconf as noarch

* Fri Jan 15 2010 Michael Shigorin <mike@altlinux.org> 6.3.13-alt4
- made contrib and locales subpackages noarch (overlooked before)
- minor spec cleanup

* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 6.3.13-alt3
- introduced %name-locales subpackage (see also 6.3.8-alt5)
- spec cleanup

* Thu Jan 14 2010 Michael Shigorin <mike@altlinux.org> 6.3.13-alt2
- merged repocop NMU properly (due to pre-existing error in related
  spec file part which was fixed in git _after_ 6.3.13-alt1)

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 6.3.13-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for fetchmail
  * postclean-05-filetriggers for spec file

* Fri Jan 01 2010 Afanasov Dmitry <ender@altlinux.org> 6.3.13-alt1
- 6.3.13
  + new "softbounce" global option;
  + CVE-2009-2666: improper SSL/TLS X.509 certificates validation (fixed
    in 6.3.11);
  + translation updates;
  see NEWS for details.

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.9-alt3.qa1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 6.3.9-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for fetchmail
  * postclean-05-filetriggers for spec file

* Mon Dec 29 2008 Afanasov Dmitry <ender@altlinux.org> 6.3.9-alt3
- silently replace initscript
- fix some repocop warnings (e.g. iconsdir)

* Wed Dec 24 2008 Afanasov Dmitry <ender@altlinux.org> 6.3.9-alt2
- change home directory to /var/run/fetchmail and update init script
  with pidfile option (Closes: #18137)

* Mon Dec 01 2008 Afanasov Dmitry <ender@altlinux.org> 6.3.9-alt1
- 6.3.9
  + CVE-2007-4565: Denial of service
  + CVE-2008-2711: Denial of service
  + close memory leak when SSL connection fails
  and other
- remove obsolete update_menus/clean_menus macroses

* Fri Oct 03 2008 Roman Savochenko <rom_as@altlinux.org> 6.3.8-alt6.1.2
- Creation fetchmail user and group made full for correct starting from global config /etc/fetchmailrc

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 6.3.8-alt6.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 6.3.8-alt6.1
- Rebuilt with python-2.5.

* Sat Nov 10 2007 Michael Shigorin <mike@altlinux.org> 6.3.8-alt6
- replaced /dev/null pseudouser home with /var/empty
  (should fix #11874)

* Sat Nov 10 2007 Michael Shigorin <mike@altlinux.org> 6.3.8-alt5
- disabled localization as it seems to be rather harmful ATM
  (#7891 must be fixed by now)
- NB: the package is de facto semi-orphaned

* Wed Sep 05 2007 Michael Shigorin <mike@altlinux.org> 6.3.8-alt4
- added patch from fetchmail-SA-2007-02 fixing CVE-2007-4565:
  NULL pointer dereference trigged by outside circumstances

* Mon May 28 2007 Michael Shigorin <mike@altlinux.org> 6.3.8-alt3
- force LC_MESSAGES=C in initscript (#7891)

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 6.3.8-alt2
- disabled service by default (#11865)

* Sat Apr 07 2007 Michael Shigorin <mike@altlinux.org> 6.3.8-alt1
- 6.3.8
  + APOP was strengthened to make the CVE-2007-1558 attack harder
  + crash when opening the BSMTP output file failed was fixed
  + other fixes and improvements

* Mon Jan 08 2007 Michael Shigorin <mike@altlinux.org> 6.3.6-alt1
- 6.3.6: minor security update (CVE-2006-5867, CVE-2006-5974)
- replaced Debian menufile with Freedesktop one
- spec macro abuse cleanup
- NB: added Packager: but I don't use %name for quite a while

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 6.3.5-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun Oct 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 6.3.5-alt1
- Release 6.3.5
- Patch6 dropped

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 6.3.4-alt1
- Release 6.3.4

* Fri Mar 31 2006 Mikhail Zabaluev <mhz@altlinux.ru> 6.3.3-alt1
- Release 6.3.3
- Updated Patch3
- New URL

* Sun Jan 22 2006 Mikhail Zabaluev <mhz@altlinux.ru> 6.3.2-alt1
- 6.3.2
- Updated Patch3

* Thu Jan 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 6.3.1-alt1
- 6.3.1

* Thu Dec 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 6.3.0-alt1
- Updated to 6.3.0
- Removed /var/lib/fetchmail
- Removed RH config stuff (bug 8387)
- Added gssapi
- RH patches are all gone
- Updated Patch2 and Patch3

* Fri Oct 28 2005 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.5.2-alt1
- Changed URL
- Updated to 6.2.5.2
- Update fetchmailconf 1.4.32 which fixes CVE-2005-3088
- Patch17 went upstream

* Sun Jul 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.5-alt2
- Applied some patches from Fedora rpm 6.2.5-9

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 6.2.5-alt1.1.1
- Rebuilt with openssl-0.9.7d.

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 6.2.5-alt1.1
- Rebuild against libkrb5-1.3.1-alt3

* Thu Oct 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.5-alt1
- New upstream release
- Patch0 gone upstream
- Updated Patch3

* Wed Oct 08 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.4-alt2
- Security fix: CAN-2003-0790 [Patch0]

* Tue Sep 30 2003 Alexander Bokovoy <ab@altlinux.ru> 6.2.4-alt1.1
- Rebuild with krb5-1.3.1-alt2

* Thu Aug 14 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.4-alt1
- New version

* Fri Jul 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.3-alt1
- New version
- Patch0 obsoleted
- Enabled Kerberos 5 support since libkrb5 is in da house now
- Configure Kerberos 5 against krb5-config [Patch4]
- Revamped the daemon init script for start_daemon/stop_daemon

* Thu Apr 03 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.2-alt3
- Enabled /usr/sbin/sendmail fallback, added it to Requires
- Removed MTA, MDA from Requires
- Provided an example fetchmailrc
- --syslog option in daemon init script

* Tue Mar 25 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.2-alt2
- Corrected the init script to run only in daemon mode
- Abolished the useless sysconfig file
- Mention ETRN in the summary

* Sun Mar 02 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.2-alt1
- 6.2.2

* Fri Feb 07 2003 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.1-alt1
- 6.2.1

* Tue Dec 17 2002 Dmitry V. Levin <ldv@altlinux.org> 6.2.0-alt2
- Fixed to build with any version of gettext.

* Tue Dec 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.2.0-alt1
- 6.2.0
- BuildRequires on a fresh gettext, build broke with previous versions

* Thu Nov 28 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.3-alt1
- 6.1.3

* Sun Nov 03 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.2-alt2
- fix permissions for icons

* Fri Nov 01 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.2-alt1
- 6.1.2

* Wed Oct 23 2002 Dmitry V. Levin <ldv@altlinux.org> 6.1.1-alt3
- Precache gettext, procmail and sendmail parameters for %%configure.

* Tue Oct 22 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.1-alt2
- Explicitly use autoconf 2.5x

* Sat Oct 19 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.1-alt1
- 6.1.1

* Thu Oct 03 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.0-alt2
- Patch by Sunil Shetye fixing a bug with skipping emails for POP3

* Wed Sep 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 6.1.0-alt1
- 6.1.0
- Unconditionally remove the lockfile on stop, because fetchmails might get
  killed off by hand

* Wed Jun 05 2002 Mikhail Zabaluev <mhz@altlinux.ru> 5.9.12-alt1
- 5.9.12
- Patch by ldv: the init script now honors UID_MIN from /etc/login.defs,
  but, sadly enough, duplicates part of the code that is in daemon()

* Sun May 19 2002 Mikhail Zabaluev <mhz@altlinux.ru> 5.9.11-alt2
- Fixed the nopermcheck code: uidlist file always needs to be checked.

* Sun May 19 2002 Mikhail Zabaluev <mhz@altlinux.ru> 5.9.11-alt1
- 5.9.11. After all that time, someone's looking after it
- Renewed fetchmailconf patch
- More clean nopermcheck patch
- Synced with 5.9.11-6mdk, many a patch added from there, icons as well.
- Removed MANIFEST from docs

* Mon Aug 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.9.0-alt1
- 5.9.0

* Thu Aug 09 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.17-alt1
- 5.8.17

* Mon Aug 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.16-alt1
- 5.8.16

* Wed Aug 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.15-alt1
- 5.8.15

* Tue Jul 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.14-alt1
- 5.8.14

* Wed Jul 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.13-alt1
- 5.8.13

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 5.8.10-alt2
- Rebuilt with python-2.1

* Tue Jun 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.10-alt1
- 5.8.10

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.8-alt1
- 5.8.8

* Mon Jun 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.7-alt1
- 5.8.7

* Wed Jun 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.6-alt1
- 5.8.6

* Wed May 30 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.5-alt1
- 5.8.5
- New server macros.

* Tue May 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.4-alt1
- 5.8.4

* Thu May 09 2001 Rider <rider@altlinux.ru> 5.8.2-alt1
- 5.8.2

* Wed Apr 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.8.1-alt1
- 5.8.1

* Tue Apr  1 2001 Rider <rider@altlinux.ru> 5.8.0-alt1
- 5.8.0

* Thu Mar 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.7.7-alt1
- 5.7.7

* Tue Mar 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.7.6-alt1
- 5.7.6

* Tue Mar 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.7.4-ipl1mdk
- 5.7.4

* Mon Mar 12 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> 5.7.2-ipl3mdk
- Fetchmail grabs ~/.fetchmailrc's for now

* Tue Mar 06 2001 Dmitry V. Levin <ldv@fandra.org> 5.7.2-ipl1mdk
- 5.7.2

* Sat Mar 03 2001 Dmitry V. Levin <ldv@fandra.org> 5.7.0-ipl1mdk
- 5.7.0

* Fri Feb 23 2001 Dmitry V. Levin <ldv@fandra.org> 5.6.8-ipl1mdk
- 5.6.8

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 5.6.7-ipl1mdk
- 5.6.7

* Mon Feb 19 2001 Dmitry V. Levin <ldv@fandra.org> 5.6.6-ipl1mdk
- 5.6.6

* Wed Jan 31 2001 Dmitry V. Levin <ldv@fandra.org> 5.6.2-ipl2mdk
- Fixed Requires.

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 5.6.2-ipl1mdk
- RE adaptions.
- Moved contrib stuff to its own subpackage.
- Modified %name-daemon to run fetchmail daemon as non-root.

* Mon Nov 27 2000 Geoffrey lee <snailtalk@mandrakesoft.com> 5.6.0-1mdk
- new and shiny source bumped into cooker.

* Mon Nov 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.5.6-1mdk
- new and shiny release.

* Wed Oct 18 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 5.5.5-1mdk
- shiny new version.
- use %%package daemon instead of with the -n flag, an old A.Skwar desire ..

* Wed Oct 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.5.2-6mdk
- requires MailTransportAgent smtpdaemon instead of smtpdaemon thus
  enabling fetchmail to be installed with only procmail.

* Tue Oct 10 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.5.2-5mdk
- fix bad iconizifaction and menufication from daouda

* Wed Oct 04 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.5.2-4mdk
- fix status report in /etc/init.d/ script

* Wed Oct 04 2000 Daouda Lo <daouda@mandrakesoft.com> 5.5.2-3mdk
- provide all icons
- menu is in spec file

* Thu Sep 28 2000 Daouda Lo <daouda@mandrakesoft.com> 5.5.2-2mdk
- set /etc/fetchmailrc permission to 600
- add 32*32 icon to fetchmailconf

* Thu Sep 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.5.2-1mdk
- new release (security fix) :  this is a 3 one-liner patch (2 more includes
  and an bad crypt function call

* Mon Sep 18 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.5.1-2mdk
- s!-f!-s so that fetchmail-daemon is disabled on first boot until a valid
  config file is provided.

* Mon Aug 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.5.1-1mdk
- new release (maily bug fixes)

* Fri Aug 18 2000 David BAUDENS <baudens@mandrakesoft.com> 5.4.5-2mdk
- Fix menu entry
- Remove locales %%Description (need to be in po, not in spec)

* Mon Aug 07 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.5-1mdk
- new release

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 5.4.4-4mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.4-3mdk
- re enable ssl :-) as we can now provide it :-)

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.4-2mdk
- disable ssl as we cannot provide it

* Mon Jul 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.4-1mdk
- new release
- spec cleaning

* Fri Jul 14 2000 Christian Zoffoli <czoffoli@linux-mandrake.com> 5.4.3-4mdk
- fixed fetchmailrc permission
- removed _sysconfdir

* Wed Jul 12 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.3-3mdk
- fix fetchamil-dameon group, invalid directories permissions, config files,
  ... and make rpmlint a lot happier :-)
- Christian Zoffoli <czoffoli@linux-mandrake.com>
	* macroszifications
	* cleanup in spec
	* daemon package
	* RPA protocol support
	* NTLM authentication support
	* SDPS protocol support
	* SSL support
	* IPv6 support disabled  --> instable

* Thu Jul 06 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.3-2mdk
- add pablo stuff for compatibility with bogus distro

* Tue Jul 04 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.3-1mdk
- reenable NLS
- use new macros
- From Christian Zoffoli <czoffoli@linux-mandrake.com> :
	* new release
	* enable IPv6

* Fri Jun 30 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.2-1mdk
- new release

* Mon Jun 19 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 5.4.1-1mdk
- 5.4.1 that corrects a bug which was causing hangs
  (thanks to Christian Zoffoli <czoffoli@littlepenguin.org>)
- changed copyright to GPL
  (thanks to Geoffrey Lee <snailtalk@linux-mandrake.com>)
- added url

* Thu Jun 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.4.0-1mdk
- new release

* Thu May 11 2000 Pixel <pixel@mandrakesoft.com> 5.3.8-4mdk
- remove lang

* Thu May 11 2000 Pixel <pixel@mandrakesoft.com> 5.3.8-3mdk
- *much* cleanup

* Fri Apr 28 2000 Daouda Lo <daouda@mandrakesoft.com> 5.3.8-2mdk
- menu entry only for fetchmail conf .
- fix an odd bug: fetchmail didn't see .fetchmailrc at all

* Thu Apr 27 2000 Daouda Lo <daouda@mandrakesoft.com> 5.3.8-1mdk
- release 5.3.8 -> fix seg faults happening in some case (maurizio )!
- add menu entry and icons to fetchmailconf
- SMP build /check
- full support for internationalisation.

* Mon Apr 17 2000 Daouda Lo <daouda@mandrakesoft.com> 5.3.7-1mdk
- release  5.3.7

* Sun Apr 09 2000 Daouda Lo <daouda@mandrakesoft.com> 5.3.6-1mdk
- new release 5.3.6
- french internationalization updated.
- make rpmlint happy !
- now support for BeOs.

* Mon Apr 03 2000 Daouda Lo <daouda@mandrakesoft.com> 5.3.5-1mdk
- new release
- cleanup spec
- rpmlint run smoothly without any warnings or errors (first time it happens to
  me :-)

* Wed Mar 22 2000 Daouda Lo <daouda@mandrakesoft.com> 5.3.3-2mdk
- fix group for both fetchmail and fetchmailconf

* Tue Mar 14 2000 Daouda LO <daouda@mandrakesoft.com> 5.3.3-1mdk
- 5.3.3
- adjust group

* Mon Mar 06 2000 Daouda LO <daouda@mandrakesoft.com>
- 5.3.1

* Sat Feb 05 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 5.2.6-1mdk
- Update to 5.2.6

* Thu Dec 09 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- fix wrong man-pages soft links

* Thu Dec 02 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- build release for Oxygen

* Thu Sep 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 5.1.0 (security fixes)

* Mon Sep 06 1999 Daouda LO <daouda@mandrakesoft.com>
-5.0.7
-add manifest in doc section ;->

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 5.0.3
- Mandrake adaptions

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- 5.0.0

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- subpackage for fetchmailconf

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- version 4.7.0
- build against glibc 2.1

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- correct typo in dangling symlink fix.

* Wed Sep 09 1998 Cristian Gafton <gafton@redhat.com>
- update to 4.5.8

* Wed Jul 22 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.5.3.

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- fixed spelung eror in the decsriptoin

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- new version 4.4.4 fixes a lot of bugs

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 4.4.1
- buildroot

* Thu Oct 23 1997 Michael Fulbright <msf@redhat.com>
- Updated to 4.3.2 using SRPM from Eric Raymond

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
