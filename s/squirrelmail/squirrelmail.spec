##
%define apachedir /var/www/html
%define statedir %_localstatedir/squirrelmail
%define spooldir %_var/spool/squirrelmail
%define locale_stamp 20080128
%define locale_version 1.4.13

Summary: SquirrelMail -- PHP-based webmail client with IMAP access
Name: squirrelmail
Version: 1.4.22
Release: alt1
License: GPL
URL: http://www.squirrelmail.org/
Group: Networking/Mail
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://heanet.dl.sourceforge.net/sourceforge/squirrelmail/%name-webmail-%version.tar.bz2
Source1: http://heanet.dl.sourceforge.net/sourceforge/squirrelmail/all_locales-%locale_version-%locale_stamp.tar.bz2

BuildArch: noarch
Requires: webserver, apache-mod_php5, perl, aspell, webserver-common
#Requires: webserver, mod_php, perl, aspell, php-mbstring
requires: MTA
#Requires: IMAPD, MTA
#Requires: /usr/sbin/sendmail, /usr/sbin/imapd

#BuildRequires: rpm-build-compat >= 0.95

%description
SquirrelMail is a standards-based webmail package written in PHP. It
includes built-in pure PHP support for the IMAP and SMTP protocols, and
all pages render in pure HTML 4.0 (with no Javascript) for maximum
compatibility across browsers.  It has very few requirements and is very
easy to configure and install. SquirrelMail has all the functionality
you would want from an email client, including strong MIME support,
address books, and folder manipulation.

%package i18n
Summary:        SquirrelMail Localization Package
Group:          Networking/Mail
Requires:       %{name} = %{version}-%{release}

%description i18n
This add-on package provides interface translations for Squirrelmail.

#------------------------------------------------------------------------------

%prep
%setup -q -n %name-webmail-%version
# Handle the locales package
%__tar xjf %{SOURCE1}
%__rm -f locale/README.locales
%__rm -f plugins/make_archive.pl

# Rearrange the documentation
#__mv AUTHORS ChangeLog COPYING INSTALL README UPGRADE doc/
#__mv ReleaseNotes doc/ReleaseNotes.txt
%__mv themes/README.themes doc/
for f in `find plugins -name "README*" -or -name INSTALL \
		   -or -name CHANGES -or -name HISTORY`; do
    %__mkdir_p doc/`dirname $f`
    %__mv $f $_
done
%__mv doc/plugins/squirrelspell/doc/README doc/plugins/squirrelspell
%__rm -rf doc/plugins/squirrelspell/doc
%__mv plugins/squirrelspell/doc/* doc/plugins/squirrelspell
%__rm -f doc/plugins/squirrelspell/index.php
%__rm -rf plugins/squirrelspell/doc

# Fixup various files
echo "left_refresh=300" >> data/default_pref
for f in contrib/RPM/squirrelmail.cron contrib/RPM/config.php.redhat; do
    %__subst "s|__ATTDIR__|%spooldir/attach/|g" $f
    %__subst "s|__PREFSDIR__|%statedir/prefs/|g" $f
done

%install
%__mkdir_p -m 755 %buildroot%_sysconfdir/squirrelmail
%__mkdir_p -m 755 %buildroot%statedir/prefs
%__mkdir_p -m 755 %buildroot%spooldir/attach
%__mkdir_p -m 755 %buildroot%apachedir/squirrelmail/config
#new location?#%__mkdir_p -m 755 %buildroot%_datadir/squirrelmail/config
%__mkdir_p -m 755 %buildroot%_sysconfdir/cron.daily

# install default_pref
%__install -m 644 data/default_pref %buildroot%_sysconfdir/squirrelmail/
%__ln_s %_sysconfdir/squirrelmail/default_pref \
    %buildroot%statedir/prefs/

# install the config files
%__install -m 644 contrib/RPM/config.php.redhat \
    %buildroot%_sysconfdir/squirrelmail/config.php
%__ln_s %_sysconfdir/squirrelmail/config.php \
    %buildroot%apachedir/squirrelmail/config/config.php
%__install -m 644 config/config_local.php \
    %buildroot%_sysconfdir/squirrelmail/config_local.php
%__ln_s %_sysconfdir/squirrelmail/config_local.php \
    %buildroot%apachedir/squirrelmail/config/config_local.php
%__rm -f config/config_local.php config/config.php
%__install -m 644 config/*.php %buildroot%apachedir/squirrelmail/config/
%__install -m 755 config/*.pl  %buildroot%apachedir/squirrelmail/config/

# install index.php
%__install -m 644 index.php %buildroot%apachedir/squirrelmail/

# Copy over the rest
for DIR in class functions help images include locale plugins src themes; do
    %__cp -rp $DIR %buildroot%apachedir/squirrelmail/
done

# install the cron script
%__install -m 755 contrib/RPM/squirrelmail.cron \
    %buildroot/%_sysconfdir/cron.daily/

%files
%config %dir %_sysconfdir/squirrelmail
%config(noreplace) %_sysconfdir/squirrelmail/*
%doc doc/*
%dir %apachedir/squirrelmail
%apachedir/squirrelmail/index.php
%apachedir/squirrelmail/class
%apachedir/squirrelmail/functions
#apachedir/squirrelmail/help
%apachedir/squirrelmail/images

%exclude %apachedir/squirrelmail/images/sec_remove_*_*.png
%exclude %apachedir/squirrelmail/images/sec_remove_ug.png

%apachedir/squirrelmail/include
%apachedir/squirrelmail/locale
%apachedir/squirrelmail/src
%apachedir/squirrelmail/themes
%apachedir/squirrelmail/config
%dir %apachedir/squirrelmail/plugins
%apachedir/squirrelmail/plugins/*
%dir %statedir
%dir %spooldir
%attr(0770, root, _webserver) %dir %statedir/prefs
%attr(0730, root, _webserver) %dir %spooldir/attach
%statedir/prefs/default_pref
%config(noreplace) %_sysconfdir/cron.daily/squirrelmail.cron

%files i18n
%apachedir/squirrelmail/locale
%apachedir/squirrelmail/images/sec_remove_*_*.png
%apachedir/squirrelmail/images/sec_remove_ug.png
%apachedir/squirrelmail/help
%exclude %apachedir/squirrelmail/locale/timezones.cfg
%exclude %apachedir/squirrelmail/help/en_US

#------------------------------------------------------------------------------

%changelog
* Tue Aug 16 2011 Ilya Mashkin <oddity@altlinux.ru> 1.4.22-alt1
- 1.4.22

* Sun Jul 25 2010 Ilya Mashkin <oddity@altlinux.ru> 1.4.21-alt1
- 1.4.21
- fix requires (Closes: #20495)

* Tue Mar 16 2010 Ilya Mashkin <oddity@altlinux.ru> 1.4.20-alt1
- 1.4.20

* Tue Jun 02 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.19-alt0.M40.1
- Build for ALT Linux 4.0

* Sun May 31 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.19-alt0.M41.1
- Build for ALT Linux 4.1

* Tue May 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.19-alt0.M50.1
- Build for ALT Linux 5.0

* Sat May 23 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.19-alt1
- 1.4.19 (Closes: #20135)
- Fixed:
  + CVE-2009-1579

* Fri May 22 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.18-alt0.M40.1
- Build for ALT Linux 4.0 (Closes: #20130)

* Wed May 20 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.18-alt0.M41.1
- Build for ALT Linux 4.1

* Wed May 13 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.18-alt1
- 1.4.18 (closes ALT#20020)
- Fixed:
  + CVE-2009-1578
  + CVE-2009-1579
  + CVE-2009-1580
  + CVE-2009-1581
- change default group from apache to _webserver (closes ALT#18528, ALT#15392)

* Mon Dec 29 2008 Vladimir V. Kamarzin <vvk at altlinux.org> 1.4.17-alt0.M40.1
- Rebuild for 4.0
- Security fixes since 1.4.13-alt1:
       + CVE-2008-2379
       + CVE-2008-3663

* Tue Dec 09 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.17-alt1
- 1.4.17

* Mon Oct 05 2008 Ilya Mashkin <oddity@altlinux.ru> 1.4.16-alt1
- 1.4.16

* Mon Jan 28 2008 Taras Ablamsky <atl at altlinux.ru> 1.4.13-alt1
- New version 1.4.13

* Wed Sep 12 2007 Taras Ablamsky <atl at altlinux.ru> 1.4.10-alt1
- New version 1.4.10a
- Locale version 1.4.9-20070106
- Build with apache2 and php5

* Fri Jan 12 2007 Taras Ablamsky <atl at altlinux.ru> 1.4.9-alt2
- Locale version 1.4.9-20070106

* Wed Dec 27 2006 Taras Ablamsky <atl at altlinux.ru> 1.4.9-alt1
- New version 1.4.9a. Locale version 1.4.8-20060903

* Fri Jul 07 2006 Taras Ablamsky <atl at altlinux.ru> 1.4.7-alt1
- New version

* Sun Feb 26 2006 Taras Ablamsky <atl at altlinux.ru> 1.4.6-alt1
- New version

* Fri Jul 15 2005 Taras Ablamsky <atl at altlinux.ru> 1.4.5-alt2
- New version

* Thu Jun 23 2005 Fr. Br. George <george@altlinux.ru> 1.4.5-alt1
- Double version upping (4.5rc1 is used due to security flaws in 4.4)

* Sat Jan 29 2005 Fr. Br. George <george@altlinux.ru> 1.4.4-alt1
- New version
- IMAP dependency removed so one can point SM to different imap server

* Sun Nov 14 2004 Fr. Br. George <george@altlinux.ru> 1.4.3a-alt2
- Security patch applied
- Anatoly Matyakh patch removed, it produces unpredictable behaviour
- No-content-recode misfeature still remains
- mbstring dependency added

* Fri Jun 04 2004 Fr. Br. George <george@altlinux.ru> 1.4.3a-alt1
- Version update, Anatoly Matyakh patch is still actual

* Thu Jan 22 2004 Fr. Br. George <george@altlinux.ru> 1.4.2-alt3
- Dummy tmpwatch version dependence removed

* Thu Nov 27 2003 Fr. Br. George <george@altlinux.ru> 1.4.2-alt2
- Anatoly Matyakh patch applied (yet another encoging/charset bug)

* Mon Oct 27 2003 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Upping version number
- Previous patches are applied by upstream

* Fri Jul 04 2003 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- AltLinux build

* Tue Mar 26 2003 Konstantin Riabitsev <icon@duke.edu> 1.4.0-1
- Build for 1.4.0

* Thu Feb 13 2003 Konstantin Riabitsev <icon@duke.edu> 1.4.0-0.2pre
- Initial release for 1.4.0 prerelease

* Tue Feb 04 2003 Konstantin Riabitsev <icon@duke.edu> 1.2.11-1
- Upping version number.

* Tue Oct 29 2002 Konstantin Riabitsev <icon@duke.edu> 1.2.9-1
- Upping version number.

* Sat Sep 14 2002 Konstantin Riabitsev <icon@duke.edu> 1.2.8-1
- adopted RH's spec file so we don't duplicate effort. 
- Removed rh'ized splash screen.
- Adding fallbacks for building rhl7 version as well with the same 
  specfile. Makes the spec file not as clean, but hey.
- remove workarounds for #68669 (rh bugzilla), since 1.2.8 works with
  register_globals = Off.
- Hardwiring localhost into the default config file. Makes sense.
- No more such file MIRRORS.
- Adding aspell as one of the req's, since squirrelspell is enabled by
  default
- Added Vendor: line to distinguish ourselves from RH.
- Doing the uglies with the release numbers.

* Tue Aug  6 2002 Preston Brown <pbrown@redhat.com> 1.2.7-4
- replacement splash screen.

* Mon Jul 22 2002 Gary Benson <gbenson@redhat.com> 1.2.7-3
- get rid of long lines in the specfile.
- remove symlink in docroot and use an alias in conf.d instead.
- work with register_globals off (#68669)

* Tue Jul 09 2002 Gary Benson <gbenson@redhat.com> 1.2.7-2
- hardwire the hostname (well, localhost) into the config file (#67635)

* Mon Jun 24 2002 Gary Benson <gbenson@redhat.com> 1.2.7-1
- hardwire the locations into the config file and cron file.
- install squirrelmail-cleanup.cron as squirrelmail.cron.
- make symlinks relative.
- upgrade to 1.2.7.
- more dependency fixes.

* Fri Jun 21 2002 Gary Benson <gbenson@redhat.com>
- summarize the summary, fix deps, and remove some redundant stuff.
- tidy up the prep section.
- replace directory definitions with standard RHL ones.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.2.6-3
- automated rebuild

* Wed Jun 19 2002 Preston Brown <pbrown@redhat.com> 1.2.6-2
- adopted Konstantin Riabitsev <icon@duke.edu>'s package for Red Hat
  Linux.  Nice job Konstantin!
