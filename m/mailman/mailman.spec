# Features/TODO:
#	add systemd init support
#       use xz for large archives in /usr/share/mailman/cron/nightly_gzip
Name: mailman
Version: 2.1.21
Release: alt3.rc2
Epoch: 5
Packager: Grigory Batalov <bga@altlinux.ru>

%define mm_user %name
%define mm_group %name

%define crontabdir %_sysconfdir/cron.d
%define logrotate %_sysconfdir/logrotate.d
%define ngxconfdir %_sysconfdir/nginx/sites-enabled.d
%define confdir %_sysconfdir/%name
%define _prefix /usr/share/%name
%define _exec_prefix %_libdir/%name
%define _var_prefix %_localstatedir/%name

Summary: Mailing list manager with built in web access
License: GPL
Group: System/Servers
Url: http://www.list.org/

# http://prdownloads.sourceforge.net/%name/%name-%version.tar.tgz
Source: %name-%{version}rc2.tar
# ALT Linux cummulative patch
Patch:  %name-%{version}rc2-%release-alt.patch

PreReq: mktemp, setup, shadow-utils, sendmail-common, vixie-cron
Requires: python, webserver-common, MTA
BuildRequires: python-devel python-module-dns

BuildRequires(pre): python
AutoProv: yes, nopython

BuildRequires(pre): rpm-macros-webserver-common
BuildRequires(pre): rpm-macros-apache
BuildRequires(pre): rpm-macros-apache2

%add_python_req_skip Defaults Mailman mm_config
%define _python_compile_include %_datadir/%name

%description
Mailman, the GNU Mailing List Management System, is a mailing list
management system written mostly in Python. Features:

- Web based list administration for nearly all tasks.  Web based
  subscriptions and user configuration management. A customizable
  "home page" for each mailing list.
- Privacy features such as moderation, open and closed list
  subscription policies, private membership rosters, and sender-based
  filters.
- Automatic web based archiving built-in with support for private
  and public archives, and hooks for external archivers.
- Per-user configuration optional digest delivery for either
  MIME-compliant or RFC 1153 style "plain text" digests.
- Integrated mail/Usenet gateways.
- Integrated auto-replies.
- Majordomo-style email based commands.
- Integrated bounce detection within an extensible framework.
- Integrated spam detection, and MIME-based content filtering.
- An extensible mail delivery pipeline.
- Support for virtual domains.

See the Mailman home site for current status, including new releases
and known problems: %url

%package apache
Group: System/Servers
Summary: Mailman configuration for Apache
BuildArch: noarch
Requires: %name = %version-%release
Requires: apache-base
Obsoletes: %name <= 2.1.21-alt0.1rc2
Conflicts: %name <= 2.1.21-alt0.1rc2

%description apache
Mailman configuration files for Apache

%package apache2
Group: System/Servers
Summary: Mailman configuration for Apache2
BuildArch: noarch
Requires: %name = %version-%release
Requires: apache2-base

%description apache2
Mailman configuration files for Apache2

%package nginx
Group: System/Servers
Summary: Mailman configuration for nginx
BuildArch: noarch
Requires: %name = %version-%release
Requires: nginx

%description nginx
Mailman configuration files for nginx

%package docs
Group: System/Servers
Summary: Mailing list manager with built in web access
BuildArch: noarch

%description docs
Documentation for mailman

%prep
%setup -q -n %name-%{version}rc2
# ALT Linux cummulative patch
%patch -p1

install -pD -m644 alt-linux/mm_cfg.py Mailman/mm_cfg.py.dist.in
install -pD -m644 alt-linux/README.ALT README.ALT

sed -i -e 's,@LOCKFILE@,%_lockdir/%name/master-qrunner,g' cron/crontab.in.in

# Debian patches
# see http://packages.qa.debian.org/m/mailman.html
for patch in \
10_wrapper_uid.patch \
16_update_debian.patch \
51_nocompile.pyc.patch \
52_check_perms_lstat.patch \
53_disable_addons.patch \
63_update_default_server_language.patch \
66_donot_let_cache_html_pages.patch \
79_archiver_slash.patch \
90_gettext_errors.patch
do
	echo "Patch ($patch):"
	patch -s -p1 < debian/patches/$patch
done

touch src/*.c

%build
%autoreconf
%configure \
	--with-var-prefix=%_var_prefix \
	--with-config-dir=%confdir \
	--with-lock-dir=%_lockdir/%name \
	--with-log-dir=%_logdir/%name \
	--with-pid-dir=%_var/run/%name \
	--with-queue-dir=%_spooldir/%name \
	--with-python=%__python \
	--with-mail-groupfile=%confdir/mail.groups \
	--with-cgi-groupfile=%confdir/cgi.groups \
	--with-mailhost=localhost.localdomain \
	--with-urlhost=localhost.localdomain \
	--without-permcheck

# rebuild mailman.pot
%make -C messages potfile

%make_build OPT="$RPM_OPT_FLAGS"

%install
find bin -type f -print0 |
	xargs -r0 grep -Zl '%__python$' |
	xargs -r0 subst 's|%__python$|%__python -O|g'

%make_install doinstall \
	DESTDIR=%buildroot \
	prefix=%prefix \
	exec_prefix=%_exec_prefix \
	var_prefix=%_var_prefix

chmod -R go-w %buildroot{%prefix,%_exec_prefix}
find %buildroot{%prefix,%_exec_prefix} -type d -print0 |
	xargs -r0 chmod a-s,o-r
chmod a-s,go-r %buildroot%_var_prefix

# Create directories we'll use for log and spool files. Create links
install -d -m3771 %buildroot%_logdir/%name
install -d -m2770 %buildroot%_spooldir/%name
install -d -m2771 %buildroot%_spooldir/%name/{archive,bounces,commands,in,news,out,qfiles,retry,shunt,virgin}

ln -s ../../log/%name %buildroot%_var_prefix/logs
ln -s ../../spool/%name %buildroot%_var_prefix/qfiles

# Copy an icons into the web server's icons directory.
mkdir -p %buildroot%webserver_iconsdir
cp -a %buildroot%prefix/icons/* %buildroot%webserver_iconsdir

# Install a logrotate control file.
install -pD -m644 alt-linux/%name.logrotate \
	%buildroot%logrotate/%name

# Install the httpd configuration file.
install -pD -m644 /dev/null %buildroot%apache_modconfdir/%name.conf
sed -e 's|@CODEDIR@|%_exec_prefix|g;s|@DATADIR@|%_var_prefix|g' \
	alt-linux/%name-httpd.conf > %buildroot%apache_modconfdir/%name.conf

# Install the httpd2 configuration file.
install -d %buildroot%apache2_mods_start
install -d %buildroot%apache2_sites_available
install -d %buildroot%apache2_sites_start
install -d %buildroot%apache2_ports_start
install -p -m644 alt-linux/apache2.mods-start %buildroot%apache2_mods_start/%name.conf
install -p -m644 alt-linux/apache2.sites-start %buildroot%apache2_sites_start/%name.conf
install -p -m644 alt-linux/apache2.ports-start %buildroot%apache2_ports_start/%name.conf
sed -e 's|@CODEDIR@|%_exec_prefix|g;s|@DATADIR@|%_var_prefix|g' \
	alt-linux/apache2.sites-available > %buildroot%apache2_sites_available/%name.conf

# Install the nginx configuration file.
install -pD -m644 /dev/null %buildroot%ngxconfdir/%name.conf
sed -e 's|@CODEDIR@|%_exec_prefix|g;s|@DATADIR@|%_var_prefix|g' \
	alt-linux/%name-nginx.conf > %buildroot%ngxconfdir/%name.conf

# Install crontab file
install -pD -m644 cron/crontab.in %buildroot%crontabdir/%name

# Install init script
install -pD -m755 misc/mailman %buildroot%_initdir/%name

# Install config files for postfix
install -pD -m644 alt-linux/mm_config.py %buildroot%confdir/mm_config.py
touch %buildroot%confdir/{aliases,virtual-mailman}
touch %buildroot%confdir/{aliases,virtual-mailman}.cdb

cat <<EOF > %buildroot%confdir/mail.groups
mail
postman
%mm_group
EOF

cat <<EOF > %buildroot%confdir/cgi.groups
apache
apache2
_spawn_fcgi
EOF

# Install man pages
install -m755 -pd %buildroot%_man8dir
install -m644 debian/manpages/*.8 %buildroot%_man8dir/

# Install lockdir and piddir
install -m755 -pd %buildroot%_lockdir/%name
install -m755 -pd %buildroot%_var/run/%name

# Remove unused files
rm -f %buildroot%confdir/sitelist.cfg
rm -rf %buildroot%_datadir/%name/tests

%pre
/usr/sbin/groupadd -rf %mm_group ||:
/usr/sbin/useradd -M -r -s /dev/null -c "GNU Mailing List Manager" \
	-d %_var_prefix -g %mm_group %mm_user &>/dev/null ||:

%post
%post_service mailman
# Fix file permissions
if [ -f %_localstatedir/%name/data/last_mailman_version ]; then
	chown %mm_user:%mm_group %_localstatedir/%name/data/last_mailman_version ||:
	chmod 644 %_localstatedir/%name/data/last_mailman_version ||:
	echo "Update mailman's database:"
	%_prefix/bin/update ||:
else
	%_prefix/bin/update &> /dev/null ||:
fi

%post apache
%post_apacheconf

%post apache2
%apache2_sbindir/a2chkconfig
%post_apache2conf

%postun apache
%postun_apacheconf

%postun apache2
%apache2_sbindir/a2chkconfig
%postun_apache2conf

%preun
%preun_service mailman

%triggerin -- postfix
# Generate aliases
%_prefix/bin/genaliases

%triggerpostun -- mailman = 5:2.1.12-alt2.1.1
echo "WARNING! Upgrading from legacy version!"
echo "Please check README.ALT for possible"
echo "problems and solutions."

%triggerun -- mailman < 5:2.1.9-alt2
if [ $1 != 0 ]; then
# Move old configs and passwords and change group
	for file in aliases virtual-mailman mm_config.py; do
		if [ -f %_localstatedir/%name/etc/$file ]; then
			mv %_localstatedir/%name/etc/$file %confdir/$file ||:
			chgrp %mm_group %confdir/$file ||:
		fi
	done
	for file in adm.pw creator.pw; do
		if [ -f %_localstatedir/%name/data/$file ]; then
			mv %_localstatedir/%name/data/$file %confdir/$file ||:
			chgrp %mm_group %confdir/$file ||:
		fi
	done
# Change paths in Postfix config
	if [ -f %_sysconfdir/postfix/main.cf ]; then
		sed  -i -e 's,%_localstatedir/%name/etc/aliases,%confdir/aliases,g' \
			-e 's,%_localstatedir/%name/etc/virtual-mailman,%confdir/virtual-mailman,g' \
			%_sysconfdir/postfix/main.cf ||:
	fi
# Move lockfiles and pidfile
	for file in %_localstatedir/%name/locks/*; do
		[ -f $file ] && mv $file %_lockdir/%name/ ||:
	done
	[ -f %_localstatedir/%name/data/master-qrunner.pid ] && \
		mv -f %_localstatedir/%name/data/master-qrunner.pid %_var/run/%name/ ||:
fi
# Restart mailman again with configs at the new place
%post_service mailman

%files
%config(noreplace) %logrotate/%name
%config(noreplace) %crontabdir/%name
%attr(0755,root,root) %_initdir/%name
%webserver_iconsdir/*
%dir %prefix
%prefix/bin
%prefix/cron
%prefix/Mailman
%prefix/messages
%prefix/pythonlib
%prefix/scripts
%prefix/templates
%doc ACKNOWLEDGMENTS BUGS FAQ INSTALL NEWS README* STYLEGUIDE.txt TODO UPGRADING
%doc misc/sitelist.cfg tests
%doc %_man8dir/*
%dir %attr(0770,root,%mm_group) %_lockdir/%name
%dir %attr(0770,root,%mm_group) %_var/run/%name

%defattr(-,root,%mm_group,-)
%_exec_prefix
%dir %attr(0751,root,%mm_group) %_var_prefix
%dir %_var_prefix/archives
%dir %_var_prefix/archives/*
%dir %_var_prefix/spam
%dir %_var_prefix/lists
%dir %_var_prefix/data
%dir %attr(2771,root,%mm_group) %confdir
%config(noreplace) %attr(0664,root,%mm_group) %confdir/mm_config.*
%config(noreplace) %attr(0664,root,%mm_group) %confdir/aliases
%config(noreplace) %attr(0664,root,%mm_group) %confdir/virtual-mailman
%config(noreplace) %attr(0664,root,%mm_group) %confdir/*groups
%ghost %attr(644,root,root) %config(missingok) %verify(not md5 mtime size) %confdir/*.cdb
%_var_prefix/logs
%_var_prefix/qfiles
%_logdir/%name
%dir %_spooldir/%name
%dir %_spooldir/%name/*

%files apache
%config(noreplace) %apache_modconfdir/%name.conf

%files apache2
%config(noreplace) %apache2_mods_start/%name.conf
%config(noreplace) %apache2_sites_available/%name.conf
%config(noreplace) %apache2_sites_start/%name.conf
%config(noreplace) %apache2_ports_start/%name.conf

%files nginx
%config(noreplace) %ngxconfdir/%name.conf

%files docs
%doc doc

%changelog
* Sun Feb 21 2016 L.A. Kostis <lakostis@altlinux.ru> 5:2.1.21-alt3.rc2
- Updated README.ALT (small style fixes).

* Fri Feb 19 2016 L.A. Kostis <lakostis@altlinux.ru> 5:2.1.21-alt2.rc2
- Updated README.ALT (add upgrade notes).
- Added trigger to show a warning after upgrade from 2.1.12.

* Wed Feb 17 2016 L.A. Kostis <lakostis@altlinux.ru> 5:2.1.21-alt1.rc2
- .spec cleanup:
  + use existing rpm-macros instead hardcoded values;
  + update buildreq (added MTA);
  + split out web configuration to separate packages
    (apache/apache2/nginx);
  + fix access rights for logdir to make logrotate happy.

* Fri Feb 05 2016 L.A. Kostis <lakostis@altlinux.ru> 5:2.1.21-alt0.1.rc2
- Updated to 2.1.21rc2.
- Security fixes:
  + CVE-2015-2775 (path traversal vulnerability);
  + DMARC support.
- Sync debian patches up to 1:2.1.20-1.

* Wed Oct 17 2012 L.A. Kostis <lakostis@altlinux.ru> 5:2.1.15-alt0.2
- New upstream release (2.1.15).
- Security fixes:
  + CVE-2011-0707,
  + many fixes in web interface against XSS attacks,
  + web admin interface has been hardened against CSRF attacks.
- Re-merge debian patches.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5:2.1.12-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5:2.1.12-alt2.1
- Rebuilt with python 2.6

* Tue Mar 24 2009 Grigory Batalov <bga@altlinux.ru> 5:2.1.12-alt2
- Fix message translations building.
- Typo in Russian template corrected.

* Mon Mar 23 2009 Grigory Batalov <bga@altlinux.ru> 5:2.1.12-alt1
- New upstream release (2.1.12).

* Thu May 22 2008 Grigory Batalov <bga@altlinux.ru> 5:2.1.10-alt1
- New upstream release (2.1.10 final).
- README.ALT updated by vvk@ .

* Mon Mar 03 2008 Grigory Batalov <bga@altlinux.ru> 5:2.1.10-alt0.3.1
- Update broken translation list.
- Don't depend on python version.

* Sat Feb 23 2008 Grigory Batalov <bga@altlinux.ru> 5:2.1.10-alt0.3
- New upstream release (2.1.10 beta 3).
- Contains CVE-2008-0564 fix.

* Fri Mar 30 2007 Grigory Batalov <bga@altlinux.ru> 5:2.1.9-alt6
- Make _exec_prefix arch-dependent.

* Thu Mar 29 2007 Grigory Batalov <bga@altlinux.ru> 5:2.1.9-alt5
- Be silent on the very first install.

* Fri Mar 23 2007 Grigory Batalov <bga@altlinux.ru> 5:2.1.9-alt4
- Switch to mailman user while updating database as root.
- Make last_mailman_version file group writable.
- Move lockfiles and pidfile during package upgrade.
- Check lockfile before service stop.

* Fri Mar 09 2007 Grigory Batalov <bga@altlinux.ru> 5:2.1.9-alt3
- Update and fix fuzzy Russian translations.

* Mon Mar 05 2007 Grigory Batalov <bga@altlinux.ru> 5:2.1.9-alt2
- Move configs and passwords to %%_sysconfdir/%%name.
- Store allowed groups in %%_sysconfdir/%%name/cgi.groups
  and %%_sysconfdir/%%name/mail.groups.
- Check Postfix config with 'postconf' during alias update.
- Update alias maps on upgrade/install.
- Custom fix_bounce.py script.
- Import a lot of Debian patches from mailman_2.1.9-5.diff.
- Add Debian manpages.
- Extra public/private option for list_lists utility.
- Japanese and Korean codecs disabled.
- Remove pidfile on 'maimanctl stop'.
- Check master-qrunner lockfile in crontab.
- Update python requires/provides.
- Compile .pyo files.
- Filter out some python warnings.
- Workaround for several Russian charsets.
- Update Russian translation.
- New packager.

* Thu Nov 23 2006 Igor Muratov <migor@altlinux.org> 5:2.1.9-alt1
- nev version
- fix for #10226 (thanks to Slava Dubrovskiy)
- patches cleanup
- various patches from debian

* Wed Sep 06 2006 Igor Muratov <migor@altlinux.org> 4:2.1.9rc1-alt1
- Security fix
- Email package updated to email-2.5.8

* Wed Apr 19 2006 Igor Muratov <migor@altlinux.org> 4:2.1.8-alt1
- New version with bug fix CVE-2006-1712
- Email package updated to email-2.5.7

* Wed Apr 05 2006 Igor Muratov <migor@altlinux.org> 4:2.1.7-alt3
- Fix provides (thanks to Vitaly Lipatov)

* Mon Mar 27 2006 Igor Muratov <migor@altlinux.org> 4:2.1.7-alt2
- Fix for missed files

* Thu Mar 09 2006 Igor Muratov <migor@altlinux.org> 4:2.1.7-alt1
- New version

* Fri Dec 09 2005 Igor Muratov <migor@altlinux.org> 4:2.1.6-alt2
- Fix for file permissions
- Patches for CVE-2005-3573

* Tue Jun 07 2005 Igor Muratov <migor@altlinux.org> 4:2.1.6-alt1
- New version release

* Wed Apr 27 2005 Igor Muratov <migor@altlinux.org> 3:2.1.6rc2-alt1
- New version
- Fix for #6569 bug

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3:2.1.5-alt4.1
- Rebuilt with python-2.4.

* Mon Feb 07 2005 Dmitry V. Levin <ldv@altlinux.org> 3:2.1.5-alt4
- NMU by ALT Security Team:
  + applied fixes for CAN-2004-1177 and CAN-2005-0202.

* Fri May 28 2004 Igor Muratov <migor@altlinux.org> 3:2.1.5-alt3
- Fixed a bug #2821 for restart method

* Mon May 24 2004 Igor Muratov <migor@altlinux.org> 3:2.1.5-alt2
- Fix dependencies
- Spec cleanup

* Thu May 20 2004 Igor Muratov <migor@altlinux.org> 3:2.1.5-alt1
- New version

* Tue Mar 23 2004 Igor Muratov <migor@altlinux.org> 3:2.1.4-alt4
- Rebuild with python23
- Spec cleanup

* Mon Mar 22 2004 Igor Muratov <migor@altlinux.org> 3:2.1.4-alt3
- Start/stop mailman with wrapper script

* Sat Mar 13 2004 Igor Muratov <migor@altlinux.ru> 3:2.1.4-alt2
- mm_cfg.py file moved to /var/lib/mailman/etc/mm_config.py
- fix permissions for /usr/share/mailman/*
- fix permissions for /var/lib/mailman
- fix permissions for /var/lib/mailman/etc/*
- fix initscript
- remove dependency to himself
- remove dependency to kernel headers
- remove old post- and pre- scripts
- remove alias_database at postfix config
- remove old patches
- add patch12
- add patch13
- add README.ALT

* Thu Jan 15 2004 Igor Muratov <migor@altlinux.ru> 3:2.1.4-alt1
- Fixed a XSS error in the admin script
- Fixed a bug 818752 Changing option via email not work
- Fixed a bug 826775 Change URL for submit buttons
- Translation to russian language by fattie

* Fri Nov 11 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.3-alt2
- Fix illegal links in admin web-interface
- Fix crash when illegal charset in header detected
- Fix crash when illegal coding in header detected

* Fri Aug 17 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.3-alt1
- New version
- Removed patch for defaults
- Removed patch for absolute url fix
- Added Scrubber patch 670167

* Wed Aug  6 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.2-alt2
- spec cleanup
- add condstart/condstop to init

* Sat Aug  2 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.2-alt1
- new version
- spec cleanup
- patch to fix absolute url
- base64 patch replaced by email patch
- patch 667026 - HyperArch.py unicode substitution
- patch 755045 - Discard_All button for pending posts administration
- update mm_cfg.py file

* Thu Mar  4 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.1-alt3
- fix mailman site list defaults at mm_cfg.py

* Sat Mar  1 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.1-alt2
- fix comment at %post script

* Mon Feb 10 2003 Igor Muratov <migor@altlinux.ru> 3:2.1.1-alt1
- build new version
- Closed a cross-site scripting vulnerability in the user options page.
- Restore the ability to control which headers show up in messages
  included in plaintext and MIME digests. See the variables
  PLAIN_DIGEST_KEEP_HEADERS and MIME_DIGEST_KEEP_HEADERS in
  Defaults.py.
- Messages included in the plaintext digests are now sent through
  the scrubber to remove (and archive) attachments.  Otherwise,
  attachments would screw up plaintext digests. MIME digests
  include the attachments inline.

* Tue Feb 06 2003 Igor Muratov <migor@altlinux.ru> 3:2.1-alt1
- build new version
- Added initscript
- Added symlink to logs
- Added symlink to spool
- Moved httpd addon config to /etc/httpd/conf/addon-modules/
- Moved crontab to /etc/cron.d
- Removed symlink /etc/smrsh/wrapper
- Patch for postfix virtual maps
- Patch for email library

* Mon Nov 18 2002 Rider <rider@altlinux.ru> 3:2.0.13-alt2
- rebuild

* Thu Aug 15 2002 Dmitry V. Levin <ldv@altlinux.org> 3:2.0.13-alt1
- 2.0.13
- Relocated log directory from %_var_prefix/logs to %_logdir/%name.
- Relocated queue directory from %_var_prefix/qfiles to %_spooldir/%name/qfiles.
- Added logrotate script.
- Added %%httpdconfdir/%%name.conf, updated INSTALL instructions.
- Added more READMEs.

* Fri Aug 09 2002 Dmitry V. Levin <ldv@altlinux.org> 3:2.0.12-alt2
- Rebuilt to fix perms.

* Wed Jul 17 2002 Dmitry V. Levin <ldv@altlinux.org> 3:2.0.12-alt1
- 2.0.12

* Thu May 23 2002 Dmitry V. Levin <ldv@altlinux.org> 3:2.0.11-alt1
- 2.0.11

* Tue Apr 30 2002 Dmitry V. Levin <ldv@alt-linux.org> 3:2.0.10-alt1
- 2.0.10
- Added one more check for postman user.

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 3:2.0.9-alt1
- Updated code to 2.0.9
- Set explicit versioned provides on setup which defines group "postman".
- Added special check for postman group at %%pre stage.

* Wed Feb 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 3:2.0.8-alt5
- Changed mail_group from nobody to postman (#0000607).
- Set explicit versioned dependence on postfix.
- Set more strict permissions on %prefix and %_exec_prefix subdirectories.

* Tue Jan 29 2002 Stanislav Ievlev <inger@altlinux.ru> 3:2.0.8-alt4
- rebuilt with new python

* Thu Dec 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 3:2.0.8-alt1
- 2.0.8 (security fix release to prevent cross-site scripting exploits.)

* Thu Nov 15 2001 Dmitry V. Levin <ldv@alt-linux.org> 3:2.0.7-alt1
- 2.0.7

* Wed Jun 27 2001 Stanislav Ievlev <inger@altlinux.ru> 2.0.5-alt3
- Rebuilt with python-2.1

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.5-alt2
- Fixed broken symlink /etc/smrsh/wrapper (#27).

* Mon May 07 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Thu Apr 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.4-alt1
- 2.0.4
- Updated install hints.

* Tue Mar 13 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.3-ipl1
- 2.0.3

* Fri Mar 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.2-ipl1
- 2.0.2
- Enhanced FHSification.

* Fri Feb 02 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.1-ipl2
- Fixed %%post script.

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.1-ipl1
- 2.0.1

* Sat Dec 16 2000 Dmitry V. Levin <ldv@fandra.org> 2.0-ipl2
- Updated description (MDK).
- Patched Defaults.py.
- Rebuild with new brp-python policy.

* Thu Nov 23 2000 Dmitry V. Levin <ldv@fandra.org> 2.0-ipl1
- 2.0 release.

* Thu Sep 28 2000 Dmitry V. Levin <ldv@fandra.org> 2.0beta6-ipl1
- 2.0beta6.

* Thu Sep 07 2000 Dmitry V. Levin <ldv@fandra.org> 2.0beta5-ipl1
- RE adaptions

* Thu Aug  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- add note about adding FollowSymlinks so that archives work

* Wed Aug  2 2000 Nalin Dahyabhai <nalin@redhat.com>
- make the default owner root again so that root owns the docs
- update to 2.0beta5, which fixes a possible security vulnerability
- add smrsh symlink

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Wed Jul 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to beta4
- change uid/gid to apache.apache to match apache (#13593)
- properly recompile byte-compiled versions of the scripts (#13619)
- change mailman alias from root to postmaster

* Sat Jul  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to beta3
- drop bugs and arch patches (integrated into beta3)

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- move web files to reside under %%contentdir
- move files from /usr/share to %%_datadir
- integrate spot-fixes from mailman lists via gnome.org

* Mon Jun 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild for Power Tools

* Wed May 23 2000 Nalin Dahyabhai <nalin@redhat.com>
- Update to 2.0beta2 to pick up security fixes.
- Change Requires: python to list >= 1.5.2

* Mon Nov  8 1999 Bernhard Rosenkränzer <bero@redhat.com>
- 1.1

* Tue Sep 14 1999 Preston Brown <pbrown@redhat.com>
- 1.0 final.

* Tue Jun 15 1999 Preston Brown <pbrown@redhat.com>
- security fix for cookies
- moved to /usr/share/mailman

* Fri May 28 1999 Preston Brown <pbrown@redhat.com>
- fix up default values.

* Fri May 07 1999 Preston Brown <pbrown@redhat.com>
- modifications to install scripts

* Thu May 06 1999 Preston Brown <pbrown@redhat.com>
- initial RPM for SWS 3.0
