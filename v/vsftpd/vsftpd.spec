Name: vsftpd
Version: 3.0.0
Release: alt1

Summary: File Transfer Protocol (FTP) server
License: GPLv2
Group: System/Servers
Url: https://security.appspot.com/vsftpd.html

# https://security.appspot.com/downloads/%name-%version.tar.gz
Source: %name-%version.tar
Source1: vsftpd.xinetd
Source2: vsftpd.pamd
Source3: vsftpd.logrotate
Source4: vsftpd.banner_fail
# The dia source to vsftpd.eps is available through the download link
# from http://www.openwall.com/presentations/Owl/
Source5: vsftpd.eps
Source6: vsftpd.socket
Source7: vsftpd@.service

Patch: vsftpd-%version-%release.patch

Requires: /var/empty
Provides: ftpserver

# Automatically added by buildreq on Mon Dec 17 2001
BuildRequires: libcap-devel libpam-devel pam_userpass-devel

%description
vsftpd is a File Transfer Protocol (FTP) server.  The "vs" stands for
Very Secure.  Obviously this is not a guarantee, but a reflection that
the entire codebase has been written with security in mind, and the
program has been carefully designed to be resilient to attack.

%prep
%setup
%patch -p1
install -p -m644 %_sourcedir/vsftpd.eps .
bzip2 -9k Changelog
bzip2 -9 vsftpd.eps

%build
%make_build \
	CFLAGS='%optflags -fPIE -Wall -W -Wshadow -Werror' \
	LIBS='-lcap -lpam -lpam_userpass' LINK=

%install
install -pD -m755 vsftpd %buildroot%_sbindir/vsftpd
mkdir -p %buildroot%_sysconfdir/vsftpd/user_conf
install -pD -m600 vsftpd.conf %buildroot%_sysconfdir/vsftpd/conf
ln -s vsftpd/conf %buildroot%_sysconfdir/vsftpd.conf
for f in %buildroot{%_sysconfdir/vsftpd/{banned_emails,chroot_list,user_list},%_logdir/vsftpd.log}; do
	install -pD -m600 /dev/null "$f"
done

install -pD -m640 %_sourcedir/vsftpd.xinetd \
	%buildroot%_sysconfdir/xinetd.d/vsftpd
install -pD -m640 %_sourcedir/vsftpd.pamd \
	%buildroot%_sysconfdir/pam.d/vsftpd
install -pD -m640 %_sourcedir/vsftpd.logrotate \
	%buildroot%_sysconfdir/logrotate.d/vsftpd
install -pD -m600 %_sourcedir/vsftpd.banner_fail \
	%buildroot%_sysconfdir/vsftpd/banner_fail

install -pD -m644 %_sourcedir/vsftpd@.service \
	%buildroot%systemd_unitdir/vsftpd@.service
install -pD -m644 %_sourcedir/vsftpd.socket \
	%buildroot%systemd_unitdir/vsftpd.socket

install -pD -m644 vsftpd.conf.5 %buildroot%_man5dir/vsftpd.conf.5
install -pD -m644 vsftpd.8 %buildroot%_man8dir/vsftpd.8

%post
umask 077
/usr/sbin/groupadd -r -f vsftpd
/usr/sbin/groupadd -r -f novsftpd
/usr/sbin/useradd -r -g vsftpd -d /var/ftp -s /dev/null -n vsftpd >/dev/null 2>&1 ||:
/usr/sbin/useradd -r -g novsftpd -d /dev/null -s /dev/null -n novsftpd >/dev/null 2>&1 ||:
touch %_logdir/vsftpd.log

%files
%_sbindir/vsftpd
%_sysconfdir/vsftpd.conf
%attr(700,root,root) %dir %_sysconfdir/vsftpd
%attr(700,root,root) %dir %_sysconfdir/vsftpd/user_conf
%config(noreplace,missingok) %ghost %_sysconfdir/vsftpd/banned_emails
%config(noreplace,missingok) %ghost %_sysconfdir/vsftpd/chroot_list
%config(noreplace,missingok) %ghost %_sysconfdir/vsftpd/user_list
%config(noreplace) %_sysconfdir/vsftpd/banner_fail
%config(noreplace) %_sysconfdir/vsftpd/conf
%config(noreplace) %_sysconfdir/xinetd.d/vsftpd
%config(noreplace) %_sysconfdir/pam.d/vsftpd
%config(noreplace) %_sysconfdir/logrotate.d/vsftpd
%systemd_unitdir/vsftpd@.service
%systemd_unitdir/vsftpd.socket
%ghost %_logdir/vsftpd.log
%_mandir/man?/*
%doc AUDIT BENCHMARKS BUGS Changelog.bz2 EXAMPLE FAQ LICENSE
%doc README README.security REWARD SECURITY SIZE SPEED TODO TUNING
%doc vsftpd.eps.bz2

%changelog
* Fri Apr 27 2012 Dmitry V. Levin <ldv@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.
- Build vsftpd as a PIE.

* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 2.3.5-alt1
- Updated to 2.3.5.
- Added systemd support files (by Alexey Shabalin; closes: #25653).

* Wed Mar 02 2011 Dmitry V. Levin <ldv@altlinux.org> 2.3.4-alt1
- Updated to 2.3.4 (fixes CVE-2011-0762).

* Fri Sep 03 2010 Dmitry V. Levin <ldv@altlinux.org> 2.3.2-alt1
- Updated to 2.3.2.

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt2
- /etc/pam.d/vsftpd: Changed to use common-login.

* Tue Dec 15 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt1
- Updated to 2.2.2.

* Wed Nov 11 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt2
- Fixed regression in LFS support introduced in previous release
  (thanks to Sergey Vlasov; closes: #22128).

* Mon Oct 26 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.

* Sun Sep 20 2009 Dmitry V. Levin <ldv@altlinux.org> 2.2.0-alt1
- Updated to 2.2.0.
- vsftpd.conf: Added comment about anonftp (Michael Shigorin; closes: #3560).

* Thu May 28 2009 Dmitry V. Levin <ldv@altlinux.org> 2.1.1-alt1
- Updated to 2.1.1.

* Tue Apr 07 2009 Dmitry V. Levin <ldv@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Tue Apr 07 2009 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt2
- vsftpd.conf: Added comment about chroot_local_user (closes: #13228).
- vsftpd.pamd:
  + Added pam_loginuid.so to the session stack.
  + Moved system-auth to the bottom of the auth stack.

* Tue Feb 03 2009 Dmitry V. Levin <ldv@altlinux.org> 2.0.7-alt1
- Updated to 2.0.7.
- Updated EXAMPLE/VIRTUAL_USERS/vsftpd.pam to something usable
  (Alexey Borisenkov; closes: #18489).

* Fri Mar 21 2008 Dmitry V. Levin <ldv@altlinux.org> 2.0.6-alt1
- Updated to 2.0.6.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.5-alt3
- /etc/xinetd.d/vsftpd:
  Increased default virtual memory limit from 16M to 64M.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.5-alt2
- Switched source packaging model to use .gear-tags.

* Thu Sep 14 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.5-alt1
- Updated to 2.0.5.

* Tue May 23 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt2
- Deal with compilation warnings generated by new gcc compiler.

* Mon Jan 09 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0.4-alt1
- Updated to 2.0.4.

* Sun Nov 27 2005 Dmitry V. Levin <ldv@altlinux.org> 2.0.3-alt1
- Updated to 2.0.3.
- Rediffed patches.
- Synced with 2.0.3-owl1.

* Sat Jun 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt3
- vsftpd.conf(5): note that session_support is disabled by default.
- vsftpd.pamd: set default session management rule.

* Mon May 31 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt2
- Corrected pam config and documentation.

* Tue Apr 27 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Sat Jan 17 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1, see Changelog for details.
- Updated patches.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt3
- PAM configuration policy enforcement.

* Sat Apr 12 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt2
- Fixed few typos in comments for default config and manpages.
- Built with libpam_userpass.so.1.

* Thu Oct 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.2-alt1
- 1.1.2:
  + Add per-IP connection limits in standalone mode.
  + Add logging of refused connect due to global or IP connection limits.
    (Many thanks for testing and suggestions from Rob van Nieuwkerk
    robn@verdi.et.tudelft.nl> and Adrian Reber <adrian@lisas.de>.
  + Make connection limit exceeded messages nonblocking.
  + Don't exit the listener if fork fails.
- Added flow control diagram
  (from Owl CanSecWest/core02 / NordU2002 presentation slides).

* Tue Oct 08 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt1
- 1.1.1:
  + Fix port_promiscuous, oops! Thanks to Bjørn-Ove Heimsund
    <bjornoh@mi.uib.no>.
  + Fix to support umasks which create executable files. Reported by
    "Martin, Andreas" <AMartin@hegau-klinikum.de>.
  + Make the messages more.. professional :( Thanks to Steven G. Taylor
    <staylor@redhat.com>.
  + Allow anon users to append to files if they can delete files! Suggestion
    from Michael Leuchtenburg <michael@slashhome.org>.
  + Hopefully fix Solaris build (-lresolv)
  + Replace atoll() with a homebrew - modern FreeBSD, OpenBSD lack it.
  + Different solution for a umask which creates executable files:
    file_open_mode.
  + First attempt at Tru64 build, working with <Sulla17@aol.com>.
  + A few minor FAQ additions.
  + Change date format in the log from Sep 09 -> Sep  9. Avoids breaking some
    broken log parsers.
  + Make "INSTALL" better and clearer.
  + Fix passwd_chroot_enable, reported by James Jones <james@richland.edu>.
  + Finish Tru64 building :-)
  + Add tunable_no_anon_password as asked for by Stephen Quinney
    <stephen.quinney@computing-services.oxford.ac.uk>.
- Updated URL.

* Wed Aug 07 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt1
- 1.1.0:
  + Use the seemingly more portable setreuid() and setregid(), poxy HP.
  + Use status 550 instead of 500 for known but disabled commands.
  + Rename "dirchange.[ch]" to "banner.[ch]".
  + Multiline connect banner support via "banner_file" config option.
  + Minor error message changes.
  + Add more FAQ entries.
  + Add patch to specify PASV address - thanks to Mike McLean <mikem@redhat.com>.
  + Drop the 2.4.0 kernel warning file
  + Rudimentary standalone listener support - to be expanded in a later release.
  + If sendfile() returns EINVAL just fall back to normal routines - handles
    non-pagecache backed files.
  + Add "port_promiscuous" setting - should help enabling FXP.
  + Modify anon_root and local_root to change directory _before_ applying the
    chroot().
  + Open all files O_NONBLOCK to avoid pipes blocking on open.
  + Support wu-ftpd style per-user chroot() via /./ in /etc/passwd HOMEDIR.
  + Add SIGHUP support to new built in listener.
  + Per-user config overrides, via "user_config_dir" - woohoo!
  + Warning fixes, i.e. change "index" to "indexx" thanks to Olaf Kirch <okir@suse.de>.
  + Make sure the standalone daemon doesn't leak zombies!
  + Supposedly fix kernel messages about MSG_PEEK race - thanks to advice from
    Alexey <kuznet@ms2.inr.ac.ru>.
  + Add global client limit for standalone mode.
  + Add username that failed when we die with str_getpwnam.
  + Add a bunch of documentation under EXAMPLES.
  + Add large file (>2Gb) support.
- Added %_sysconfdir/vsftpd/banner_fail config file.
- Fixed vsftpd(8) (#0001113).

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0.2-alt0.1pre3
- 1.0.2pre3 (added options: use_localtime, hide_ids).
- Set hide_ids to YES.
- logrotate config: s/nocompress/delaycompress/.

* Mon Dec 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt2
- Added pam_userpass support (derived from Owl's patch).

* Mon Dec 03 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt1
- 1.0.1 (Nothing changed except version number).

* Thu Nov 29 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.0-alt2
- Fixed typo in manpage.
- Create logfile in %%post script.

* Thu Nov 15 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.0-alt1
- 1.0.0 (added options: anon_root, local_root; updated: BENCHMARKS, README).
- Added more examples to default config file.

* Wed Nov 07 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.9.3-alt1
- Initial revision. ALT specific adaptions are:
  + all config files have been moved into %_sysconfdir/vsftpd;
  + default guest, anonymous and nobody users are: vsftpd, vsftpd, novsftpd;
  + default config defines bsd-compatible passive min/max ports;
  + default secure_chroot_dir set to /var/empty;
  + xinetd config: disable = yes, rlimit_as = 16M;
  + pamd config: use pam_stack(system-auth), pam_nologin;
  + compile/link options cleanup.
