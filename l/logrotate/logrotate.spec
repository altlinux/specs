Name: logrotate
Version: 3.9.1
Release: alt4

Summary: Rotates, compresses, and mails system logs
License: GPLv2+
Group: File tools
Url: https://fedorahosted.org/logrotate/

# https://fedorahosted.org/releases/l/o/logrotate/%name-%version.tar.gz
Source: logrotate-%version.tar
Source1: logrotate.cron

Patch1: logrotate-alt-config.patch
Patch2: logrotate-alt-file_type.patch
Patch3: logrotate-alt-taboo.patch
Patch4: logrotate-alt-insecure-permissions.patch
Patch5: logrotate-upstream-gcc6.patch
Patch6: logrotate-upstream-configure.patch

Provides: /etc/logrotate.d

%def_with selinux

BuildRequires: libacl-devel libpopt-devel
%{?_with_selinux:BuildPreReq: libselinux-devel}

%description
The logrotate utility is designed to simplify the administration of log
files on a system which generates a lot of log files.  logrotate allows
for the automatic rotation, compression, removal and mailing of log files.
logrotate can be set to handle a log file daily, weekly, monthly or
when the log file gets to a certain size.  Normally, logrotate runs as
a daily cron job.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
touch AUTHORS ChangeLog NEWS README
%autoreconf
%configure %{subst_with selinux}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/etc/logrotate.d

install -pD -m640 examples/logrotate-default %buildroot/etc/logrotate.conf
install -pD -m755 %_sourcedir/logrotate.cron %buildroot/etc/cron.daily/logrotate
install -pD -m644 /dev/null %buildroot%_localstatedir/logrotate/status

%check
make test

%post
if [ ! -s %_localstatedir/logrotate/status -a -s %_localstatedir/logrotate.status ]; then
	mv -f %_localstatedir/logrotate.status %_localstatedir/logrotate/status
fi

%files
%_sbindir/*
%config(noreplace) /etc/cron.daily/logrotate
%config(noreplace) /etc/logrotate.conf
%_mandir/man?/*
%attr(750,root,root) %dir /etc/logrotate.d
%attr(700,root,root) %dir %_localstatedir/logrotate
%attr(644,root,root) %verify(not size md5 mtime) %config(noreplace) %_localstatedir/logrotate/status
%doc CHANGES

%changelog
* Tue Nov 28 2017 Dmitry V. Levin <ldv@altlinux.org> 3.9.1-alt4
- Applied upstream LFS fix (closes: #34140).

* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.9.1-alt3
- Fixed build with gcc-6.

* Tue Dec 15 2015 Dmitry V. Levin <ldv@altlinux.org> 3.9.1-alt2
- Apply ALT Secure Packaging Policy (closes: #31623).

* Sun Dec 13 2015 Dmitry V. Levin <ldv@altlinux.org> 3.9.1-alt1
- Updated to 3.9.1 (closes: #12593, #29681, #31616).

* Thu Jul 21 2011 Dmitry V. Levin <ldv@altlinux.org> 3.7.9-alt3
- Dropped unused /var/run/logrotate directory (closes: #25583).

* Mon Oct 18 2010 Dmitry V. Levin <ldv@altlinux.org> 3.7.9-alt2
- Really enabled SELinux support (patch by vvk@; closes: #24350).

* Tue Aug 24 2010 Dmitry V. Levin <ldv@altlinux.org> 3.7.9-alt1
- Updated to 3.7.9.
- Enabled SELinux support.

* Fri Sep 28 2007 Stanislav Ievlev <inger@altlinux.org> 3.7.6-alt1
- 3.6.7

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 3.6.2-alt4
- Unhardcoded script directory for non-root processes,
  thus allowed unprivileged users to use logrotate (#9959).

* Wed Jun 09 2004 Dmitry V. Levin <ldv@altlinux.org> 3.6.2-alt3
- Rebuilt in new environment (#3523).

* Wed Sep 25 2002 Dmitry V. Levin <ldv@altlinux.org> 3.6.2-alt2
- Provides: /etc/logrotate.d

* Sat Mar 23 2002 Dmitry V. Levin <ldv@altlinux.org> 3.6.2-alt1
- 3.6.2.
- Removed readState patch (merged upstream).
- Marked %_localstatedir/logrotate/status ad %%config(noreplace).
- Added %%post script to handle logrotate/status move.

* Sun Jan 20 2002 Dmitry V. Levin <ldv@altlinux.org> 3.6-alt3
- Optimized cron script.

* Fri Dec 28 2001 Dmitry V. Levin <ldv@altlinux.org> 3.6-alt2
- Fixed taboo patch.

* Wed Dec 26 2001 Dmitry V. Levin <ldv@altlinux.org> 3.6-alt1
- 3.6, updated our patches.
- Fixed typo in readState error check.
- Merged fchmod/fchown race (owl).

* Mon Jun 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.5.4-alt1
- 3.5.4 (some fixes went to mainstream).
- Added ".number" taboo suffix.

* Sun Dec 31 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.2-ipl1mdk
- 3.5.2.
- Updated all patches for new version.

* Tue Sep 19 2000 Dmitry V. Levin <ldv@fandra.org> 3.3-ipl10mdk
- Moved %_localstatedir/logrotate.status --> %_localstatedir/logrotate/status
  (and fixed perms).
- Automatically added BuildRequires.

* Thu Sep 14 2000 Dmitry V. Levin <ldv@fandra.org> 3.3-ipl9mdk
- Patched config handling to support taboo suffixes.

* Mon Sep 11 2000 Dmitry V. Levin <ldv@fandra.org> 3.3-ipl8mdk
- Rewritten runScript function in secure manner.
- Merged with MDK.

* Wed Nov 10 1999 Dmitry V. Levin <ldv@fandra.org>
- update to 3.3
- Fandra adaptions

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- update to 2.1.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
